// Study guide (study.html): one exam's day-by-day plan from data/study/<EXAM>.json.
// URL: #exam=SAA-C03&day=3. Progress (studied days, last day opened) lives in StudyStore.
"use strict";

// [code, name, level, vendor] in display order: vendor tabs, then level segments, then exam chips.
const STUDY_EXAMS = [
  ["CLF-C02", "Cloud Practitioner", "foundational"], ["AIF-C01", "AI Practitioner", "foundational"],
  ["AIB-C01", "AI Business Strategist", "foundational"],
  ["SAA-C03", "Solutions Architect – Associate", "associate"], ["DVA-C02", "Developer – Associate", "associate"],
  ["DVA-C03", "Developer – Associate (new)", "associate"],
  ["SOA-C03", "CloudOps Engineer – Associate", "associate"], ["DEA-C01", "Data Engineer – Associate", "associate"],
  ["MLA-C01", "Machine Learning Engineer – Associate", "associate"],
  ["SAP-C02", "Solutions Architect – Professional", "professional"],
  ["SAP-C03", "Solutions Architect – Professional (new)", "professional"], ["DOP-C02", "DevOps Engineer – Professional", "professional"],
  ["AIP-C01", "Generative AI Developer – Professional", "professional"],
  ["ANS-C01", "Advanced Networking – Specialty", "specialty"], ["SCS-C03", "Security – Specialty", "specialty"],
  ["PLTR-DE", "Data Engineer – Associate", "associate", "palantir"], ["PLTR-AIE", "AI Engineer – Associate", "associate", "palantir"],
  ["PLTR-APD", "Application Developer – Associate", "associate", "palantir"],
  ["AZ-900", "Azure Fundamentals", "foundational", "azure"],
  ["AZ-104", "Azure Administrator – Associate", "associate", "azure"],
  ["AI-901", "Azure AI Fundamentals", "foundational", "azure"],
  ["AI-103", "Azure AI Apps and Agents Developer – Associate", "associate", "azure"],
  ["AZ-305", "Azure Solutions Architect – Expert", "expert", "azure"],
  ["SC-900", "Security, Compliance, and Identity Fundamentals", "foundational", "azure"],
].map(([code, name, level, vendor]) => [code, name, level, vendor || "aws"]);
const VENDORS = [["aws", "AWS"], ["palantir", "Palantir"], ["azure", "Azure"]];
const vendorOf = code => (STUDY_EXAMS.find(([c]) => c === code) || [])[3];
const isNewVersion = name => / \(new\)$/.test(name);
const shortName = name => name.replace(/ – (Associate|Professional|Expert|Specialty)( \(new\))?$/, "");
const LEVELS = [["foundational", "Foundational"], ["associate", "Associate"], ["professional", "Professional"], ["expert", "Expert"], ["specialty", "Specialty"]];
const levelOf = code => (STUDY_EXAMS.find(([c]) => c === code) || [])[2];
// Exams with a published guide (listed in exams-index.json); all of them if the index is missing.
const available = () => STUDY_EXAMS.filter(([c]) => !dataIndex || !dataIndex.study || c in dataIndex.study);

// Progress store. Today it is localStorage only; the shape mirrors the planned server records
// (one PROG#<exam> item per user: {done, lastDay, updatedAt}; plus lastExam on the profile) so a later sync can push and pull
// it as is. Every read and write goes through here — keep it that way so the backend swap stays
// local to this object. Key keeps the site's aws_qbank_ prefix like the other stored data.
const StudyStore = {
  KEY: "aws_qbank_study_v1",
  _read() {
    try {
      const v = JSON.parse(localStorage.getItem(this.KEY) || "null");
      if (v && v.v === 1 && v.exams) return v;
    } catch (e) { /* storage blocked or corrupt: start empty */ }
    return { v: 1, exams: {} };
  },
  _write(state) {
    try { localStorage.setItem(this.KEY, JSON.stringify(state)); } catch (e) { /* private mode: keep in memory only */ }
  },
  _norm(p = {}) {
    return { done: Array.isArray(p.done) ? p.done : [], lastDay: p.lastDay || null, updatedAt: p.updatedAt || null };
  },
  get(exam) { return this._norm(this._read().exams[exam]); },
  _update(exam, fn) {
    const state = this._read();
    const p = this._norm(state.exams[exam]);
    fn(p);
    p.updatedAt = new Date().toISOString();
    state.exams[exam] = p;
    this._write(state);
    return p;
  },
  setLastDay(exam, day) { return this._update(exam, p => { p.lastDay = day; }); },
  lastExam() { return this._read().lastExam || null; },
  setLastExam(exam) { const state = this._read(); state.lastExam = exam; this._write(state); },
  toggleDone(exam, day) {
    return this._update(exam, p => {
      p.done = p.done.includes(day) ? p.done.filter(d => d !== day) : [...p.done, day].sort((a, b) => a - b);
    });
  },
};

let dataIndex = null;   // data/exams-index.json
let specs = null;       // data/exam-specs.json (domain names)
let glossary = null;    // data/glossary.json: {terms:[{id, term, full, match, en, ko, exams}]}
let glossaryReady = Promise.resolve();
const guides = {};      // exam -> {exam, days}
let current = { exam: null, day: 1, vendor: null, level: null };   // vendor/level: what was picked, if not the current exam's

const $ = sel => document.querySelector(sel);
const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const text = s => esc(s);

// Glossary terms. Each term is marked only in the exams it was chosen for, and only at its first
// appearance in a day (concepts, then exam points, then recap) — few marks keep them useful.
// Quiz text is never marked: tapping a choice answers it.
const termRegex = {};   // exam -> {re, byText}
function termsFor(exam) {
  if (!glossary) return null;
  if (!(exam in termRegex)) {
    const byText = new Map();
    for (const t of glossary.terms) if (t.exams.includes(exam)) for (const m of t.match) byText.set(m, t);
    const alts = [...byText.keys()].sort((a, b) => b.length - a.length).map(m => m.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
    termRegex[exam] = alts.length ? { re: new RegExp(`(?<![\\w-])(${alts.join("|")})(?![\\w-])`, "g"), byText } : null;
  }
  return termRegex[exam];
}
function withTerms(s, seen) {
  const tr = termsFor(current.exam);
  if (!tr) return esc(s);
  let out = "", last = 0;
  for (const m of s.matchAll(tr.re)) {
    const t = tr.byText.get(m[0]);
    if (seen.has(t.id)) continue;
    seen.add(t.id);
    out += esc(s.slice(last, m.index)) + `<button type="button" class="term" data-term="${esc(t.id)}" aria-expanded="false">${esc(m[0])}</button>`;
    last = m.index + m[0].length;
  }
  return out + esc(s.slice(last));
}

function parseHash() {
  const p = new URLSearchParams(location.hash.replace(/^#/, ""));
  const exam = p.get("exam");
  const day = parseInt(p.get("day"), 10);
  return { exam: STUDY_EXAMS.some(([c]) => c === exam) ? exam : null, day: day > 0 ? day : null };
}

async function loadIndex() {
  const res = await fetch("./data/exams-index.json", { cache: "no-cache" });
  if (!res.ok) throw new Error("exams-index.json " + res.status);
  dataIndex = await res.json();
  const v = dataIndex.files && dataIndex.files["exam-specs.json"];
  const sres = await fetch(`./data/exam-specs.json${v ? "?v=" + v : ""}`);
  if (!sres.ok) throw new Error("exam-specs.json " + sres.status);
  specs = await sres.json();
}

async function loadGlossary() {
  const v = dataIndex && dataIndex.files && dataIndex.files["glossary.json"];
  try {
    const res = await fetch(`./data/glossary.json${v ? "?v=" + v : ""}`);
    if (res.ok) glossary = await res.json();
  } catch (e) { /* no glossary: text renders unmarked */ }
}

async function loadGuide(exam) {
  if (!guides[exam]) {
    const v = dataIndex && dataIndex.study && dataIndex.study[exam];
    const res = await fetch(`./data/study/${exam}.json${v ? "?v=" + v : ""}`);
    if (!res.ok) throw new Error(`study data for ${exam}: HTTP ${res.status}`);
    guides[exam] = await res.json();
  }
  return guides[exam];
}

// Domain names come from exam-specs.json, or from the guide itself for an exam the question bank
// does not cover.
function domainName(exam, code) {
  const list = (specs && specs[exam] && specs[exam].domains) || (guides[exam] && guides[exam].domains) || [];
  const d = list.find(x => x.code === code);
  return d ? d.name : code;
}

function renderExamRow() {
  const all = available();
  const vendor = current.vendor || vendorOf(current.exam) || (all[0] || [])[3];
  const exams = all.filter(e => e[3] === vendor);
  const levels = LEVELS.filter(([l]) => exams.some(e => e[2] === l));
  const level = current.level && levels.some(([l]) => l === current.level) ? current.level
    : vendorOf(current.exam) === vendor ? levelOf(current.exam) : (levels[0] || [])[0];
  const vendors = VENDORS.filter(([v]) => all.some(e => e[3] === v));
  $("#vendorRow").hidden = vendors.length < 2;
  $("#vendorRow").innerHTML = vendors.map(([v, label]) =>
    `<button class="vtab" role="tab" aria-selected="${v === vendor}" data-vendor="${v}">${label}<span class="cnt">${all.filter(e => e[3] === v).length}</span></button>`).join("");
  $("#levelRow").hidden = !levels.length;   // shown even for one level, so every vendor looks the same
  $("#levelRow").innerHTML = levels.map(([l, label]) =>
    `<button class="lseg" aria-pressed="${l === level}" data-level="${l}">${label}<span class="cnt">${exams.filter(e => e[2] === l).length}</span></button>`).join("");
  $("#examRow").innerHTML = exams.filter(e => e[2] === level).map(([code, name]) =>
    `<button class="chip${code === current.exam ? " active" : ""}" data-exam="${code}" title="${esc(name)}"><span class="cd">${code}${isNewVersion(name) ? `<span class="new">NEW</span>` : ""}</span><span class="nm">${esc(shortName(name))}</span></button>`).join("");
}

function dayListHTML(guide, progress) {
  const groups = [];
  for (const d of guide.days) {
    const key = d.domain || "final";
    if (!groups.length || groups[groups.length - 1].key !== key) groups.push({ key, days: [] });
    groups[groups.length - 1].days.push(d);
  }
  return groups.map(g => `<div class="daygroup"><h3>${g.key === "final" ? "Final review" : `${g.key} · ${esc(domainName(guide.exam, g.key))}`}</h3>` +
    g.days.map(d => `<button class="daylink${d.day === current.day ? " current" : ""}" data-day="${d.day}"><span class="n">Day ${d.day}</span><span>${esc(d.title)}</span>${progress.done.includes(d.day) ? '<span class="ck" aria-label="studied">✓</span>' : ""}</button>`).join("") +
    `</div>`).join("");
}

function quizHTML(quiz) {
  return quiz.map((q, qi) => `<div class="quiz-q" data-q="${qi}"><p class="q">${qi + 1}. ${text(q.q)}</p>` +
    q.choices.map((c, ci) => `<button class="choice" data-c="${ci}"><span class="k">${"ABCDE"[ci]}</span><span>${text(c)}</span></button>`).join("") +
    `<div class="explain-slot"></div></div>`).join("");
}

function renderDay() {
  const guide = guides[current.exam];
  const total = guide.days.length;
  const d = guide.days[current.day - 1];
  if ($("#dayBar")) {   // absent if a cached older study.html is paired with this script
    $("#dayBarCode").textContent = current.exam;
    $("#dayBarName").textContent = `Day ${d.day} / ${total} · ${d.title}`;
    $("#barPrev").disabled = d.day === 1;
    $("#barNext").disabled = d.day === total;
  }
  const progress = StudyStore.get(current.exam);
  const studied = progress.done.includes(d.day);
  const qbank = `./#exam=${current.exam}${d.domain ? "&d=" + d.domain : ""}&study=${d.day}`;   // &study: the bank offers a way back
  const seen = new Set();   // glossary terms already marked on this day
  const conceptsHTML = d.concepts.map(c => `<section class="concept"><h3>${esc(c.heading)}</h3><p>${withTerms(c.body, seen)}</p></section>`).join("");
  const pointsHTML = d.examPoints.map(p => `<li>${withTerms(p, seen)}</li>`).join("");
  const recapHTML = withTerms(d.recap, seen);
  $("#main").innerHTML = `
    <div class="daybar">
      <button class="navbtn" id="prevBtn" ${d.day === 1 ? "disabled" : ""} aria-label="Previous day">←<span class="t"> Prev</span></button>
      <details class="daynav" id="dayNav"><summary>Day ${d.day} / ${total} · ${progress.done.length} studied ▾</summary>
        <div class="daypanel">${dayListHTML(guide, progress)}</div></details>
      <button class="navbtn" id="nextBtn" ${d.day === total ? "disabled" : ""} aria-label="Next day"><span class="t">Next </span>→</button>
    </div>
    <article class="card">
      <div class="eyebrow"><span>${current.exam} · Day ${d.day} / ${total}</span>${d.domain ? `<span class="dbadge">${d.domain}</span><span>${esc(domainName(current.exam, d.domain))}</span>` : `<span class="dbadge">Final review</span>`}</div>
      <h2 class="daytitle">${esc(d.title)}</h2>
      <div class="svcs">${d.services.map(s => `<span class="svc">${esc(s)}</span>`).join("")}</div>
      <div class="label">Concepts</div>
      ${conceptsHTML}
      <div class="label">Exam angle</div>
      <ul class="points">${pointsHTML}</ul>
      <div class="label">Check yourself</div>
      ${quizHTML(d.quiz)}
      <div class="label">Recap</div>
      <p class="recap">${recapHTML}</p>
      <div class="dayfoot">
        <button class="donebtn" id="doneBtn" aria-pressed="${studied}">${studied ? "✓ Studied" : "Mark as studied"}</button>
        <a class="qblink" href="${qbank}">Practice ${d.domain ? d.domain + " " : ""}questions →</a>
      </div>
    </article>`;
}

function answer(qEl, picked) {
  const d = guides[current.exam].days[current.day - 1];
  const q = d.quiz[+qEl.dataset.q];
  const ok = picked === q.answer;
  qEl.querySelectorAll(".choice").forEach((b, i) => {
    b.disabled = true;
    b.classList.toggle("correct", i === q.answer);
    b.classList.toggle("incorrect", i === picked && !ok);
    b.classList.toggle("dim", i !== q.answer && i !== picked);
  });
  qEl.querySelector(".explain-slot").innerHTML =
    `<div class="explain${ok ? "" : " wrong"}"><b>${ok ? "Correct" : "Not quite — answer: " + "ABCDE"[q.answer]}</b>${text(q.explain)}</div><button class="retry">Try again</button>`;
}

async function show(exam, day) {
  hideTerm();
  current.exam = exam;
  current.vendor = current.level = null;
  renderExamRow();
  $("#main").innerHTML = `<div class="loading">Loading ${exam}…</div>`;
  let guide;
  try { [guide] = await Promise.all([loadGuide(exam), glossaryReady]); }
  catch (e) { $("#main").innerHTML = `<div class="empty">Could not load the ${exam} study guide.</div>`; return; }
  if (current.exam !== exam) return;   // another exam was picked while loading
  const total = guide.days.length;
  current.day = Math.min(Math.max(day || StudyStore.get(exam).lastDay || 1, 1), total);
  StudyStore.setLastDay(exam, current.day);
  StudyStore.setLastExam(exam);
  const want = `#exam=${exam}&day=${current.day}`;
  if (location.hash !== want) history.replaceState(null, "", want);
  document.title = `${exam} Day ${current.day} · Study Guide`;
  renderDay();
}

// Term popover: one shared element. Tap or click pins it open; on devices with a mouse, hovering
// also shows it. Escape, clicking elsewhere, scrolling or changing the day closes it.
const pop = { el: null, btn: null, pinned: false, y: 0 };
function showTerm(btn, pinned) {
  const t = glossary && glossary.terms.find(x => x.id === btn.dataset.term);
  if (!t) return;
  if (!pop.el) {
    pop.el = document.createElement("div");
    pop.el.className = "termpop"; pop.el.id = "termPop"; pop.el.setAttribute("role", "tooltip");
    document.body.appendChild(pop.el);
  }
  if (pop.btn && pop.btn !== btn) pop.btn.setAttribute("aria-expanded", "false");
  pop.btn = btn; pop.pinned = pinned; pop.y = scrollY;
  btn.setAttribute("aria-expanded", "true");
  btn.setAttribute("aria-describedby", "termPop");
  pop.el.innerHTML = `<div class="tp-head"><b>${esc(t.term)}</b>${t.full ? ` · ${esc(t.full)}` : ""}</div>` +
    `<p class="tp-en">${esc(t.en)}</p><p class="tp-ko" lang="ko">${esc(t.ko)}</p>`;
  pop.el.hidden = false;
  // Below the term if it fits, else above; clamped to the viewport with a 12px margin.
  const r = btn.getBoundingClientRect(), w = pop.el.offsetWidth, h = pop.el.offsetHeight;
  const left = Math.min(Math.max(12, r.left + r.width / 2 - w / 2), innerWidth - w - 12);
  const top = r.bottom + 8 + h <= innerHeight - 12 ? r.bottom + 8 : Math.max(12, r.top - 8 - h);
  pop.el.style.left = `${left}px`; pop.el.style.top = `${top}px`;
}
function hideTerm() {
  if (pop.el) pop.el.hidden = true;
  if (pop.btn) { pop.btn.setAttribute("aria-expanded", "false"); pop.btn.removeAttribute("aria-describedby"); }
  pop.btn = null; pop.pinned = false;
}
const canHover = matchMedia("(hover: hover)").matches;
document.addEventListener("mouseover", e => {
  if (!canHover) return;
  const b = e.target.closest(".term");
  if (b && b !== pop.btn) showTerm(b, false);
});
document.addEventListener("mouseout", e => {
  const b = e.target.closest(".term");
  if (!b) return;
  if (b === pop.btn && !pop.pinned && !b.contains(e.relatedTarget)) hideTerm();
});
// A real scroll closes it; the few pixels a tap or scroll-into-view can leave behind do not.
window.addEventListener("scroll", () => { if (pop.btn && Math.abs(scrollY - pop.y) > 40) hideTerm(); }, { passive: true });

function go(exam, day) {
  location.hash = `exam=${exam}${day ? "&day=" + day : ""}`;   // hashchange renders
}

document.addEventListener("click", e => {
  const t = e.target.closest("button");
  if (pop.btn && t !== pop.btn) hideTerm();
  if (!t) return;
  if (t.classList.contains("term")) return pop.btn === t && pop.pinned ? hideTerm() : showTerm(t, true);
  if (t.dataset.exam) return go(t.dataset.exam, null);
  if (t.dataset.vendor) { current.vendor = t.dataset.vendor; current.level = null; return renderExamRow(); }
  if (t.dataset.level) { current.level = t.dataset.level; return renderExamRow(); }
  if (t.id === "prevBtn" || t.id === "barPrev") return go(current.exam, current.day - 1);
  if (t.id === "nextBtn" || t.id === "barNext") return go(current.exam, current.day + 1);
  if (t.id === "toTop") return window.scrollTo({ top: 0, behavior: smooth ? "smooth" : "auto" });
  if (t.dataset.day) return go(current.exam, +t.dataset.day);
  if (t.id === "doneBtn") {
    const studied = StudyStore.toggleDone(current.exam, current.day).done.includes(current.day);
    t.setAttribute("aria-pressed", studied);
    t.textContent = studied ? "✓ Studied" : "Mark as studied";
    const nav = $("#dayNav");
    if (nav) nav.querySelector(".daypanel").innerHTML = dayListHTML(guides[current.exam], StudyStore.get(current.exam));
    if (nav) nav.querySelector("summary").textContent = `Day ${current.day} / ${guides[current.exam].days.length} · ${StudyStore.get(current.exam).done.length} studied ▾`;
    return;
  }
  const qEl = t.closest(".quiz-q");
  if (qEl && t.classList.contains("choice")) return answer(qEl, +t.dataset.c);
  if (qEl && t.classList.contains("retry")) {
    qEl.querySelectorAll(".choice").forEach(b => { b.disabled = false; b.classList.remove("correct", "incorrect", "dim"); });
    qEl.querySelector(".explain-slot").innerHTML = "";
  }
});

// Close the day list when clicking elsewhere or pressing Escape.
document.addEventListener("click", e => {
  const nav = $("#dayNav");
  if (nav && nav.open && !nav.contains(e.target)) nav.open = false;
});
document.addEventListener("keydown", e => {
  if (e.key === "Escape" && pop.btn) { const b = pop.btn; hideTerm(); b.focus(); return; }
  const nav = $("#dayNav");
  if (e.key === "Escape" && nav && nav.open) { nav.open = false; nav.querySelector("summary").focus(); }
});

// Compact day bar once the day navigation leaves the viewport; back-to-top after ~1.5 screens (as in the question bank).
const smooth = !matchMedia("(prefers-reduced-motion: reduce)").matches;
function updateScrollUi() {
  const nav = document.querySelector(".daybar");
  const bar = $("#dayBar"), top = $("#toTop");
  if (!bar || !top) return;
  const showBar = !!nav && nav.getBoundingClientRect().bottom < 0;
  bar.classList.toggle("show", showBar);
  bar.setAttribute("aria-hidden", showBar ? "false" : "true");
  bar.querySelectorAll("button, a").forEach(el => { el.tabIndex = showBar ? 0 : -1; });
  const showTop = scrollY > innerHeight * 1.5;
  top.classList.toggle("show", showTop);
  top.tabIndex = showTop ? 0 : -1;
}
window.addEventListener("scroll", updateScrollUi, { passive: true });
window.addEventListener("resize", updateScrollUi);

window.addEventListener("hashchange", () => {
  const h = parseHash();
  if (h.exam) show(h.exam, h.day).then(() => window.scrollTo(0, 0));
});

(async function init() {
  try { await loadIndex(); } catch (e) { /* index missing: fetch files without version */ }
  glossaryReady = loadGlossary();   // fetched alongside the first exam's guide
  const h = parseHash();
  if (h.exam) return show(h.exam, h.day);
  // No exam in the link: reopen the last exam studied, else the first one listed.
  const last = StudyStore.lastExam();
  const exams = available();
  const exam = exams.some(([c]) => c === last) ? last : exams.length ? exams[0][0] : null;
  if (exam) return show(exam, null);
  renderExamRow();
  $("#main").innerHTML = `<div class="empty">No study guides found.</div>`;
})();
