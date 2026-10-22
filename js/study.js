// Study guide (study.html): one exam's day-by-day plan from data/study/<EXAM>.json.
// URL: #exam=SAA-C03&day=3. Progress (studied days, last day opened) lives in StudyStore.
"use strict";

const STUDY_EXAMS = [
  ["AIF-C01", "AI Practitioner"], ["AIB-C01", "AI Business Strategist"],
  ["DEA-C01", "Data Engineer – Associate"], ["SAA-C03", "Solutions Architect – Associate"],
  ["DVA-C02", "Developer – Associate"], ["SOA-C03", "CloudOps Engineer – Associate"],
  ["MLA-C01", "Machine Learning Engineer – Associate"], ["SAP-C02", "Solutions Architect – Professional"],
  ["DOP-C02", "DevOps Engineer – Professional"], ["AIP-C01", "Generative AI Developer – Professional"],
  ["ANS-C01", "Advanced Networking – Specialty"], ["SCS-C03", "Security – Specialty"],
];

// Progress store. Today it is localStorage only; the shape mirrors the planned server records
// (one PROG#<exam> item per user: {done, lastDay, updatedAt}) so a later sync can push and pull
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
  toggleDone(exam, day) {
    return this._update(exam, p => {
      p.done = p.done.includes(day) ? p.done.filter(d => d !== day) : [...p.done, day].sort((a, b) => a - b);
    });
  },
};

let dataIndex = null;   // data/exams-index.json
let specs = null;       // data/exam-specs.json (domain names)
const guides = {};      // exam -> {exam, days}
let current = { exam: null, day: 1 };

const $ = sel => document.querySelector(sel);
const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
// Body text goes through here; the glossary (P3) will mark known terms at this point.
const text = s => esc(s);

function parseHash() {
  const p = new URLSearchParams(location.hash.replace(/^#/, ""));
  const exam = p.get("exam");
  const day = parseInt(p.get("day"), 10);
  return { exam: STUDY_EXAMS.some(([c]) => c === exam) ? exam : null, day: day > 0 ? day : null };
}

async function loadIndex() {
  const res = await fetch("./data/exams-index.json", { cache: "no-cache" });
  dataIndex = await res.json();
  const v = dataIndex.files && dataIndex.files["exam-specs.json"];
  specs = await (await fetch(`./data/exam-specs.json${v ? "?v=" + v : ""}`)).json();
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

function domainName(exam, code) {
  const d = specs && specs[exam] && specs[exam].domains.find(x => x.code === code);
  return d ? d.name : code;
}

function renderExamRow() {
  $("#examRow").innerHTML = STUDY_EXAMS.map(([code, name]) =>
    `<button class="chip${code === current.exam ? " active" : ""}" role="tab" aria-selected="${code === current.exam}" data-exam="${code}" title="${esc(name)}">${code}</button>`).join("");
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
  const progress = StudyStore.get(current.exam);
  const studied = progress.done.includes(d.day);
  const qbank = `./#exam=${current.exam}${d.domain ? "&d=" + d.domain : ""}`;
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
      ${d.concepts.map(c => `<section class="concept"><h3>${esc(c.heading)}</h3><p>${text(c.body)}</p></section>`).join("")}
      <div class="label">Exam angle</div>
      <ul class="points">${d.examPoints.map(p => `<li>${text(p)}</li>`).join("")}</ul>
      <div class="label">Check yourself</div>
      ${quizHTML(d.quiz)}
      <div class="label">Recap</div>
      <p class="recap">${text(d.recap)}</p>
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
  current.exam = exam;
  renderExamRow();
  $("#main").innerHTML = `<div class="loading">Loading ${exam}…</div>`;
  let guide;
  try { guide = await loadGuide(exam); }
  catch (e) { $("#main").innerHTML = `<div class="empty">Could not load the ${exam} study guide.</div>`; return; }
  if (current.exam !== exam) return;   // another exam was picked while loading
  const total = guide.days.length;
  current.day = Math.min(Math.max(day || StudyStore.get(exam).lastDay || 1, 1), total);
  StudyStore.setLastDay(exam, current.day);
  const want = `#exam=${exam}&day=${current.day}`;
  if (location.hash !== want) history.replaceState(null, "", want);
  document.title = `${exam} Day ${current.day} · Study Guide`;
  renderDay();
}

function go(exam, day) {
  location.hash = `exam=${exam}${day ? "&day=" + day : ""}`;   // hashchange renders
}

document.addEventListener("click", e => {
  const t = e.target.closest("button");
  if (!t) return;
  if (t.dataset.exam) return go(t.dataset.exam, null);
  if (t.id === "prevBtn") return go(current.exam, current.day - 1);
  if (t.id === "nextBtn") return go(current.exam, current.day + 1);
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
  const nav = $("#dayNav");
  if (e.key === "Escape" && nav && nav.open) { nav.open = false; nav.querySelector("summary").focus(); }
});

window.addEventListener("hashchange", () => {
  const h = parseHash();
  if (h.exam) show(h.exam, h.day).then(() => window.scrollTo(0, 0));
});

(async function init() {
  try { await loadIndex(); } catch (e) { /* index missing: fetch files without version */ }
  const h = parseHash();
  if (h.exam) return show(h.exam, h.day);
  current.exam = null;
  renderExamRow();
  $("#main").innerHTML = `<div class="empty">Pick an exam above to open its study plan.</div>`;
})();
