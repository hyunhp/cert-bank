// Mock exam mode for the certification question bank.
// Draws a timed exam from one certification's pool, stratified by the official domain weights and
// preferring questions not yet seen in earlier mock exams. Answers are hidden until submission.
// State lives in localStorage so a reload resumes the running exam.

const KEY_ACTIVE = "aws_qbank_mock_active_v1";
const KEY_HISTORY = "aws_qbank_mock_history_v1";
const KEY_SEEN = "aws_qbank_mock_seen_v1";
const KEY_RECENT = "aws_qbank_mock_recent_v1";   // per exam: ids of the last RECENT_KEEP drawn mocks; survives "Reset seen questions"
const RECENT_KEEP = 2;
const SHORT_N = 20;
const SECTION_N = 40;   // "Full section": up to this many questions of one exam domain
const HISTORY_MAX = 200;

let qb = null;           // helpers passed from index.html
let root = null;
let onExit = null;
let specs = null;        // data/exam-specs.json
let domainMap = null;    // data/exam-domains.json
let state = null;        // running or finished exam
let view = "setup";
let setupExam = null;
let tick = null;
let reviewFilter = "incorrect";
let lastOpts = null;     // remembered so the error screen can retry a full open

// ---------- storage ----------
const load = (k, d) => { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } };
const save = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* quota or private mode */ } };
const drop = (k) => { try { localStorage.removeItem(k); } catch (e) {} };
// Stored values can be missing, from an older version, or hand-edited; never trust their shape.
const isObj = (v) => v && typeof v === "object" && !Array.isArray(v);
function loadHistory() {
  const v = load(KEY_HISTORY, []);
  return Array.isArray(v) ? v.filter(h => isObj(h) && typeof h.exam === "string" && Number.isFinite(h.correct) && Number.isFinite(h.total) && h.total > 0) : [];
}
function loadSeen() {
  const v = load(KEY_SEEN, {});
  if (!isObj(v)) return {};
  const out = {};
  Object.entries(v).forEach(([k, arr]) => { if (Array.isArray(arr)) out[k] = arr.filter(x => typeof x === "string"); });
  return out;
}
function loadRecent() {
  const v = load(KEY_RECENT, {});
  if (!isObj(v)) return {};
  const out = {};
  Object.entries(v).forEach(([k, runs]) => { if (Array.isArray(runs)) out[k] = runs.filter(Array.isArray).map(r => r.filter(x => typeof x === "string")).slice(0, RECENT_KEEP); });
  return out;
}
export function resetAllMockData() { [KEY_ACTIVE, KEY_HISTORY, KEY_SEEN, KEY_RECENT].forEach(drop); }

// ---------- helpers ----------
const esc = (s) => (s == null ? "" : String(s)).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const LETTERS = "ABCDEFGH";
const nf = (n) => Number(n).toLocaleString("en-US");
// Uniform integer in [0, n) from the browser's crypto source (rejection sampling, so no modulo bias); Math.random only as a fallback.
function randInt(n) {
  const c = globalThis.crypto;
  if (c && c.getRandomValues) {
    const lim = Math.floor(0x100000000 / n) * n, b = new Uint32Array(1);
    do { c.getRandomValues(b); } while (b[0] >= lim);
    return b[0] % n;
  }
  return Math.floor(Math.random() * n);
}
export function shuffle(a) { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = randInt(i + 1); [a[i], a[j]] = [a[j], a[i]]; } return a; }
// Priority tiers for a draw: never seen and not in the last mocks, then recent-but-unseen (only after a reset), then seen and not recent, then the rest.
const tierOf = (id, seen, recent) => (seen.has(id) ? 2 : 0) + (recent.has(id) ? 1 : 0);
function byTier(ids, seen, recent) {
  const tiers = [[], [], [], []];
  ids.forEach(id => tiers[tierOf(id, seen, recent)].push(id));
  return tiers.flatMap(shuffle);
}
function fmtTime(sec) {
  sec = Math.max(0, Math.round(sec));
  const h = Math.floor(sec / 3600), m = Math.floor((sec % 3600) / 60), s = sec % 60;
  return (h ? h + ":" + String(m).padStart(2, "0") : String(m)) + ":" + String(s).padStart(2, "0");
}
function examName(code) { const e = (qb.EXAMS || []).find(([c]) => c === code); return e ? e[1] : code; }

export function domainOf(q, exam, map) {
  if (!q.examCodes || q.examCodes[0] === exam) return q.domainCode;
  return (map && map[q.id] && map[q.id][exam]) || q.domainCode;
}

// Largest-remainder allocation of n questions over domains by weight, capped by supply.
export function allocate(n, domains, supply) {
  const total = domains.reduce((s, d) => s + d.weight, 0);
  const alloc = {}, rema = [];
  let used = 0;
  for (const d of domains) {
    const exact = (n * d.weight) / total;
    alloc[d.code] = Math.min(Math.floor(exact), supply[d.code] || 0);
    used += alloc[d.code];
    rema.push({ code: d.code, r: exact - Math.floor(exact), w: d.weight });
  }
  // hand out the remainder, largest fractional part first, then by weight, respecting supply
  let left = n - used;
  while (left > 0) {
    const cand = rema.filter(x => alloc[x.code] < (supply[x.code] || 0)).sort((a, b) => (b.r - a.r) || (b.w - a.w));
    if (!cand.length) break;
    for (const c of cand) { if (left <= 0) break; alloc[c.code]++; left--; c.r -= 1; }
  }
  return alloc;
}

// Section-only draw: n questions of one domain, unseen first, final order shuffled.
export function drawFocused(exam, n, docs, domain, map, seenIds, recentIds) {
  const seen = new Set(seenIds || []), recent = new Set(recentIds || []);
  const pool = docs.filter(q => domainOf(q, exam, map) === domain).map(q => q.id);
  return shuffle(byTier(pool, seen, recent).slice(0, n));
}

// Draw n question ids: stratified by domain, unseen first, then final order shuffled.
export function draw(exam, n, docs, spec, map, seenIds, recentIds) {
  const seen = new Set(seenIds || []), recent = new Set(recentIds || []);
  const groups = {};
  for (const d of spec.domains) groups[d.code] = [];
  for (const q of docs) {
    const g = groups[domainOf(q, exam, map)];
    if (!g) continue;              // question tagged with a domain this exam doesn't have
    g.push(q.id);
  }
  const supply = {};
  for (const k in groups) supply[k] = groups[k].length;
  const alloc = allocate(n, spec.domains, supply);
  let picked = [];
  for (const k in groups) picked = picked.concat(byTier(groups[k], seen, recent).slice(0, alloc[k] || 0));
  return shuffle(picked);
}

function timeFor(spec, n) { return Math.ceil((spec.minutes * n) / spec.questions) * 60; }

// Practice targets sit a margin above the official pass mark: AWS scaled scores are not percentages, so
// AWS and Azure (scaled 700/1000 or more) use 80% (Foundational/Associate) or 85% (Professional/Expert/Specialty); vendors that publish a percent
// pass mark (Palantir: 70%) use that mark + 10. Google Cloud publishes no pass mark (pass/fail only): same 80/85% targets.
// The score that counts as comfortably ready: 10 points over a published percent pass mark, else 80% (85% for professional-level exams).
export function targetPct(spec) {
  const level = spec && spec.level;
  return (spec && spec.passingPct) ? Math.min(100, spec.passingPct + 10)
    : (level === "professional" || level === "expert" || level === "specialty") ? 85 : 80;
}
export function verdictFor(spec, pct, mode) {
  const hi = targetPct(spec);
  const mid = (spec && spec.passingPct) ? spec.passingPct : hi - 10;
  if (pct === 100) return { key: "ready", label: "Perfect score", note: mode === "short" ? "Every question correct. Try a full exam or another section to keep testing yourself." : "Every question correct. Keep the edge with questions you have not seen yet." };
  if (pct >= hi) return { key: "ready", label: "Pass-ready", note: `${hi}%+ on first attempts is a comfortable margin.` };
  if (pct >= mid) return { key: "border", label: "Borderline", note: `Aim for ${hi}%+ before booking the exam.` };
  return { key: "work", label: "Needs work", note: `Focus on the weakest domains below, then retake.` };
}

// Readiness: each of the latest READY_RUNS full exams must be timed, finished in time, drawn mostly from questions not seen
// before, reach the target score, and reach DOMAIN_FLOOR% in every domain (checked per exam, not summed).
// Short practice and section drills do not count.
// An exam submitted with fewer than 25% of its questions answered was set up, not taken: it is not saved to the history
// and its questions are not marked as seen.
export const EMPTY_ATTEMPT = 0.25;
export function isEmptyAttempt(answers, ids) {
  const done = ids.filter(id => ((answers || {})[id] || []).length).length;
  return ids.length > 0 && done / ids.length < EMPTY_ATTEMPT;
}
export const READY_RUNS = 3, DOMAIN_FLOOR = 70, FRESH_MIN = 0.8;
export function readiness(spec, hist) {
  const target = targetPct(spec);
  const pctOf = h => Math.round((h.correct / h.total) * 100);
  const runs = hist.filter(h => h.mode === "full" && !h.domain).slice(-READY_RUNS).map(h => {
    const weak = spec.domains.map(d => { const v = (h.dom || {})[d.code]; return v && v[1] ? { code: d.code, pct: Math.round((v[0] / v[1]) * 100) } : null; })
      .filter(d => d && d.pct < DOMAIN_FLOOR);
    const why = !h.timed ? "untimed" : h.auto ? "ran out of time" : (h.fresh != null && h.fresh / h.total < FRESH_MIN) ? "mostly repeated questions" : null;
    return { pct: pctOf(h), why, scoreOk: !why && pctOf(h) >= target, domOk: !why && weak.length === 0, weak };
  });
  const streak = key => { let n = 0; for (let i = runs.length - 1; i >= 0 && runs[i][key]; i--) n++; return n; };
  const scoreStreak = streak("scoreOk"), domStreak = streak("domOk");
  return { target, need: READY_RUNS, floor: DOMAIN_FLOOR, scoreStreak, domStreak, runs, ready: scoreStreak >= READY_RUNS && domStreak >= READY_RUNS };
}
function readinessHTML(r, exam) {
  const li = (ok, main, sub) => `<li class="${ok ? "ok" : ""}"><span class="mark" aria-hidden="true">${ok ? "✓" : "○"}</span><div>${main}${sub ? `<div class="meta">${sub}</div>` : ""}</div></li>`;
  const score = r.runs.length ? "Latest: " + r.runs.map(x => `${x.pct}%${x.why ? ` (${x.why})` : x.scoreOk ? "" : " (below target)"}`).join(" · ") : "No full exam yet.";
  const dom = r.runs.length ? "Latest: " + r.runs.map(x => x.why ? `(${x.why})` : x.weak.length ? x.weak.map(d => `${d.code} ${d.pct}%`).join(", ") : "✓").join(" · ") : "";
  return `<div class="panel readiness"><div class="dhead"><b>Exam readiness · ${esc(exam)}</b><span class="meta ${r.ready ? "v-ready" : ""}">${r.ready ? "Ready to book" : "Not yet"}</span></div>
    <ul class="rdy">
      ${li(r.scoreStreak >= r.need, `${r.target}%+ on ${r.need} full exams in a row <b>${r.scoreStreak}/${r.need}</b>`, score)}
      ${li(r.domStreak >= r.need, `Every domain ${r.floor}%+ in each of those exams <b>${r.domStreak}/${r.need}</b>`, dom)}
    </ul>
    <div class="meta">Counts full timed exams finished in time with mostly unseen questions. Short practice and section drills do not count.</div></div>`;
}

function passMarkNote(spec) {
  if (spec.passingPct) {
    return `The official pass mark is ${spec.passingPct}% correct.` +
      (spec.weightsAssumed ? " Official domain weights are not published, so this mock samples every domain equally." : "");
  }
  if (spec.passMarkUnpublished) return "The official pass mark is not published; results are pass or fail only.";
  return `Percent correct is not the scaled score; the official pass mark is ${spec.passingScore}/1000.`;
}

function passMarkMeta(spec) {
  return spec.passingPct ? `official pass mark ${spec.passingPct}% correct`
    : spec.passMarkUnpublished ? "pass mark not published" : `official pass mark ${spec.passingScore}/1000`;
}

// ---------- styles ----------
function injectStyles() {
  if (document.getElementById("mock-styles")) return;
  const s = document.createElement("style");
  s.id = "mock-styles";
  s.textContent = `
.mk{max-width:760px;margin:0 auto;padding:calc(env(safe-area-inset-top,0px) + 16px) 0 80px}
.mk h2{font-size:1.3rem;margin:4px 0 6px}
.mk .sub{color:var(--muted);font-size:.9rem;margin:0 0 14px}
.mk .panel{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px;box-shadow:var(--shadow);margin-bottom:12px}
.mk label.row{display:flex;gap:10px;align-items:center;font-size:.92rem;margin:6px 0}
.mk select{font:inherit;font-size:.95rem;padding:7px 10px;border-radius:8px;border:1px solid var(--line);background:var(--surface);color:var(--ink);width:100%}
.mk .modes{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.mk .mode{border:1px solid var(--line);border-radius:10px;padding:12px;cursor:pointer;background:var(--surface);text-align:left;font:inherit;color:var(--ink)}
.mk .mode.on{border-color:var(--accent);background:var(--accent-bg)}
.mk .mode b{display:block;font-size:.95rem}
.mk .mode span{font-size:.8rem;color:var(--muted)}
.mk .btn{font:inherit;font-size:.9rem;font-weight:600;padding:9px 16px;border-radius:9px;border:1px solid var(--accent);background:var(--accent);color:var(--surface);cursor:pointer}
.mk .btn.ghost{background:var(--surface);color:var(--accent-ink);border-color:var(--line)}
.mk .btn.warn{background:var(--bad);border-color:var(--bad)}
.mk .btn:disabled{opacity:.45;cursor:default}
.mk .support{margin:22px 0 0;font-size:.85rem;color:var(--muted);text-align:center;word-break:keep-all}
.mk .support a{color:var(--accent);font-weight:600;white-space:nowrap}
.mk .btnrow{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.mk .meta{font-size:.82rem;color:var(--muted)}
.mk .linkbtn{background:none;border:none;color:var(--accent);font:inherit;font-size:.85rem;cursor:pointer;padding:0}
.mk table{width:100%;border-collapse:collapse;font-size:.84rem}
.mk td,.mk th{padding:6px 4px;border-bottom:1px solid var(--line);text-align:left}
.mk th{color:var(--muted);font-weight:500}
.mk .v-ready{color:var(--good)} .mk .v-border{color:var(--amber)} .mk .v-work{color:var(--bad)}
.mkbar{position:sticky;top:0;z-index:15;background:var(--bg);border-bottom:1px solid var(--line);padding:calc(env(safe-area-inset-top,0px) + 8px) 0 8px;margin-bottom:12px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.mkbar .code{font-family:"IBM Plex Mono","IBM Plex Sans KR",monospace;font-weight:600;font-size:.82rem}
.mkbar .mkfill{position:absolute;left:0;bottom:-1px;height:3px;border-radius:2px;background:var(--accent);transition:width .2s}
.mkbar .prog{font-size:.85rem;color:var(--muted)}
.mkbar .timer{font-family:"IBM Plex Mono","IBM Plex Sans KR",monospace;font-weight:600;font-size:.95rem;margin-left:auto;font-variant-numeric:tabular-nums}
.mkbar .timer.low{color:var(--bad)}
.mkbar .btn{padding:6px 12px;font-size:.8rem}
.mk .qnum{font-size:.8rem;color:var(--muted);margin-bottom:6px;display:flex;align-items:center;gap:8px}
.mk .flag{margin-left:auto;font:inherit;font-size:.8rem;border:1px solid var(--line);background:var(--surface);color:var(--muted);border-radius:7px;padding:4px 10px;cursor:pointer}
.mk .flag.on{border-color:var(--amber);color:var(--amber);background:var(--amber-bg)}
.mk .flagmark{color:var(--amber);font-weight:600}
.mk .selnote{font-size:.8rem;color:var(--amber);margin:-4px 0 10px;font-weight:600}
/* Prev / Flag / Next stay pinned to the bottom of the screen, so a long question can be flagged without scrolling back up. */
.mk .nav{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:8px;margin-top:8px;position:sticky;bottom:0;z-index:14;background:var(--bg);border-top:1px solid var(--line);padding:5px 0 calc(5px + env(safe-area-inset-bottom,0px))}
.mk .nav .btn{padding:6px 14px;font-size:.85rem}
.mk .nav .btn:first-child{justify-self:start}
.mk .nav .btn:last-child{justify-self:end}
.mk .nav .flag{margin-left:0;padding:6px 12px;font-size:.85rem;font-weight:600;border-radius:9px}
.mk .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(44px,1fr));gap:6px;margin:10px 0}
.mk .cell{font:inherit;font-size:.82rem;font-family:"IBM Plex Mono","IBM Plex Sans KR",monospace;padding:8px 0;border-radius:7px;border:1px solid var(--line);background:var(--surface);color:var(--muted);cursor:pointer;position:relative}
.mk .cell.ans{background:var(--accent-bg);color:var(--accent-ink);border-color:var(--accent)}
.mk .cell.flg::after{content:"";position:absolute;top:3px;right:3px;width:7px;height:7px;border-radius:50%;background:var(--amber)}
.mk .cell.cur{outline:2px solid var(--ink);outline-offset:1px}
.mk .legend{display:flex;gap:14px;flex-wrap:wrap;font-size:.78rem;color:var(--muted);align-items:center}
.mk .legend .sw{display:inline-block;width:12px;height:12px;border-radius:3px;border:1px solid var(--line);background:var(--surface);vertical-align:-2px;margin-right:4px;position:relative}
.mk .legend .sw.ans{background:var(--accent-bg);border-color:var(--accent)}
.mk .legend .sw.cur{border:2px solid var(--ink)}
.mk .legend .sw.flg::after{content:"";position:absolute;top:1px;right:1px;width:5px;height:5px;border-radius:50%;background:var(--amber)}
/* Results: review choices as one even row, then the two way-out buttons side by side. */
.mk .btnrow.reviewrow{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}
.mk .btnrow.exitrow{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}
.mk .btnrow.reviewrow .btn,.mk .btnrow.exitrow .btn{padding-inline:8px;text-align:center}
.mk .confirm{border:1px solid var(--bad-line);background:var(--bad-bg);border-radius:10px;padding:12px;margin-top:10px;font-size:.9rem}
.mk .scorerow{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.mk .score{font-size:2.6rem;font-weight:700;font-variant-numeric:tabular-nums;line-height:1.1}
.mk .score.v-ready{color:var(--good)} .mk .score.v-border{color:var(--amber)} .mk .score.v-work{color:var(--bad)}
.mk .verdict{font-weight:700;font-size:.85rem;padding:3px 10px;border-radius:999px;border:1px solid currentColor}
.mk .verdict.v-ready{background:var(--good-bg)} .mk .verdict.v-border{background:var(--amber-bg)} .mk .verdict.v-work{background:var(--bad-bg)}
.mk .statchips{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0 8px}
.mk .statchips span{font-size:.8rem;padding:3px 9px;border-radius:7px;background:var(--surface-2);color:var(--ink);font-variant-numeric:tabular-nums}
.mk p.meta{margin:4px 0}
.mk .passnote{font-size:.78rem;padding-top:6px;border-top:1px solid var(--line);margin-top:8px}
.mk .notsaved{color:var(--amber);font-weight:600}
.mk .dhead{display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap}
.mk .delhist{font:inherit;font-size:1.1rem;line-height:1;color:var(--muted);background:none;border:none;cursor:pointer;padding:2px 8px;border-radius:6px}
@media (hover:hover){.mk .delhist:hover{color:var(--bad);background:var(--bad-bg)}}
.mk .rdy{list-style:none;margin:8px 0;padding:0}
.mk .rdy li{display:flex;gap:10px;margin:10px 0;font-size:.9rem}
.mk .rdy .mark{flex:none;width:22px;height:22px;border-radius:50%;border:1px solid var(--line);display:grid;place-items:center;font-size:.78rem;color:var(--muted)}
.mk .rdy li.ok .mark{background:var(--good-bg);border-color:var(--good-line);color:var(--good)}
.mk .readiness>.meta{margin-top:6px}
.mk .rvlabel{font-size:.72rem;text-transform:uppercase;letter-spacing:.04em;font-weight:600;color:var(--muted);margin:14px 0 6px 2px}
.mk .btn.ghost.emph{border-color:var(--accent);color:var(--accent-ink);background:var(--accent-bg)}
.mk .dom{margin:8px 0}
.mk .dom .top{display:flex;justify-content:space-between;align-items:flex-start;font-size:.84rem;gap:8px}
.mk .dom .top span:last-child{white-space:nowrap;flex:none}
.mk .practice{margin-top:10px;font-weight:600}
.mk .dom .bar{height:7px;border-radius:4px;background:var(--surface-2);overflow:hidden;margin-top:4px}
.mk .dom .fill{height:100%;background:var(--accent)}
.mk .dom.weak .fill{background:var(--bad)}
.mk .tabs{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0 12px}
.mk .tab{font:inherit;font-size:.8rem;padding:5px 11px;border-radius:999px;border:1px solid var(--line);background:var(--surface);color:var(--muted);cursor:pointer}
.mk .tab.on{border-color:var(--accent);color:var(--accent-ink);background:var(--accent-bg)}
.mk .rv{margin-bottom:12px}
.mk .rvhead{display:flex;align-items:center;gap:8px;font-size:.8rem;color:var(--muted);margin-bottom:8px}
.mk .rvdom{font-family:"IBM Plex Mono","IBM Plex Sans KR",monospace;font-size:.72rem;padding:1px 6px;border-radius:5px;background:var(--surface-2);color:var(--muted)}
.mk .rvexp summary{cursor:pointer;font-size:.85rem;font-weight:600;color:var(--accent-ink);margin:8px 0}
.mk .yours{font-size:.75rem;font-weight:600;color:var(--muted);white-space:nowrap}
.mk .rvhead .ok{color:var(--good);font-weight:700} .mk .rvhead .no{color:var(--bad);font-weight:700}
@media (max-width:480px){.mk .modes{grid-template-columns:1fr}}
.mk select + select{margin-top:8px}
@media (max-width:520px){.mk .startbtn{width:100%;padding:12px 16px}.mkbar{gap:8px}.mkbar .prog .lbl{display:none}}
`;
  document.head.appendChild(s);
}

// ---------- data ----------
async function ensureData() {
  if (!specs) {
    const [s, m] = await Promise.all([
      fetch("./data/exam-specs.json", { cache: "no-cache" }).then(r => { if (!r.ok) throw new Error("exam-specs.json " + r.status); return r.json(); }),
      fetch("./data/exam-domains.json", { cache: "no-cache" }).then(r => r.ok ? r.json() : {}).catch(() => ({})),
    ]);
    specs = s; domainMap = m;
  }
}
let setupTimed = true;    // timer checkbox survives re-renders of the setup screen
let setupDomain = null;   // null = whole exam by official weights, else one domain code
function domainDocs(docs) { return setupDomain ? docs.filter(q => domainOf(q, setupExam, domainMap) === setupDomain) : docs; }
async function docsFor(exam) { return (await qb.loadExam(exam)) || []; }

// ---------- lifecycle ----------
export async function open(opts) {
  lastOpts = opts;
  qb = opts.qb; root = opts.root; onExit = opts.onExit;
  injectStyles();
  state = null; view = "setup";
  try {
    await ensureData();
    const active = await validActive(load(KEY_ACTIVE, null));
    setupExam = (opts.exam && specs[opts.exam]) ? opts.exam : (active && active.exam) || "SAA-C03";
    setupDomain = opts.domain && specs[setupExam].domains.some(d => d.code === opts.domain) ? opts.domain : null;
    if (active) { state = active; view = "exam"; await startTicking(); }
  } catch (err) {
    showError(specs ? err : new Error("Could not load exam settings. Check your connection and reload. (" + (err && err.message) + ")"));
    return;
  }
  await render();
}

// A saved in-progress exam can go stale (question bank updated, storage edited, older app version).
// Keep whatever still matches the current pool; discard it only if nothing usable is left.
async function validActive(active) {
  if (!active || active.submitted || typeof active !== "object") return null;
  if (!specs[active.exam] || !Array.isArray(active.ids)) { drop(KEY_ACTIVE); return null; }
  const docs = await docsFor(active.exam);
  // No questions usually means the download failed (offline, reload mid-request): keep the saved
  // exam untouched and report the problem instead of discarding the user's progress.
  if (!docs.length) throw new Error(`Could not load ${active.exam} questions. Check your connection and reload.`);
  const byId = new Map(docs.map(q => [q.id, q]));
  const ids = active.ids.filter(id => byId.has(id));
  if (!ids.length) { drop(KEY_ACTIVE); return null; }
  if (ids.length !== active.ids.length) {
    const keep = new Set(ids);
    active.ids = ids;
    active.answers = Object.fromEntries(Object.entries(active.answers || {}).filter(([k]) => keep.has(k)));
    active.flags = (active.flags || []).filter(k => keep.has(k));
  }
  active.order = active.order || {};
  ids.forEach(id => {
    const keys = (byId.get(id).choices || []).map(c => c.key);
    const o = active.order[id];
    if (!Array.isArray(o) || o.length !== keys.length || !o.every(k => keys.includes(k))) active.order[id] = shuffle(keys);
  });
  active.answers = active.answers || {};
  active.flags = active.flags || [];
  active.cur = Math.min(Math.max(0, active.cur | 0), ids.length - 1);
  save(KEY_ACTIVE, active);
  return active;
}

function exit(extra) {
  stopTicking();
  const ex = (state && state.exam) || setupExam;
  if (onExit) onExit(ex, extra);
}

function persist() { if (state && !state.submitted) save(KEY_ACTIVE, state); }

async function startExam(mode, timed) {
  const spec = specs[setupExam];
  const docs = await docsFor(setupExam);
  const pool = domainDocs(docs);
  const n = mode === "short" ? Math.min(SHORT_N, pool.length) : Math.min(setupDomain ? SECTION_N : spec.questions, pool.length);
  const seenAll = loadSeen(), recentAll = loadRecent();
  const recentIds = (recentAll[setupExam] || []).flat();
  const ids = setupDomain ? drawFocused(setupExam, n, docs, setupDomain, domainMap, seenAll[setupExam], recentIds)
                          : draw(setupExam, n, docs, spec, domainMap, seenAll[setupExam], recentIds);
  if (!ids.length) return;
  // Remember this draw at once (even if the exam is abandoned) so the next one steers clear of it.
  recentAll[setupExam] = [ids].concat(recentAll[setupExam] || []).slice(0, RECENT_KEEP);
  save(KEY_RECENT, recentAll);
  const byId = new Map(docs.map(q => [q.id, q]));
  const order = {};
  ids.forEach(id => { order[id] = shuffle((byId.get(id).choices || []).map(c => c.key)); });
  const dur = timeFor(spec, ids.length);
  const seenBefore = new Set(seenAll[setupExam] || []);
  state = {
    v: 1, exam: setupExam, domain: setupDomain, mode, ids, order, answers: {}, flags: [], cur: 0, fresh: ids.filter(id => !seenBefore.has(id)).length,
    startedAt: Date.now(), duration: dur, timed: !!timed, deadline: timed ? Date.now() + dur * 1000 : null,
    submitted: false,
  };
  persist();
  view = "exam";
  await startTicking();
  render();
  window.scrollTo(0, 0);
}

async function startTicking() {
  stopTicking();
  if (!state || !state.timed || state.submitted) return;
  tick = setInterval(() => {
    const left = (state.deadline - Date.now()) / 1000;
    const el = root.querySelector(".mkbar .timer");
    if (el) { el.textContent = fmtTime(left); el.classList.toggle("low", left < 300); }
    if (left <= 0) submit(true);
  }, 1000);
  if (state.deadline - Date.now() <= 0) await submit(true);
}
function stopTicking() { if (tick) { clearInterval(tick); tick = null; } }

async function submit(auto) {
  if (!state || state.submitted) return;
  stopTicking();
  const docs = await docsFor(state.exam);
  const byId = new Map(docs.map(q => [q.id, q]));
  const spec = specs[state.exam];
  const dom = {};
  spec.domains.forEach(d => { dom[d.code] = [0, 0]; });
  let correct = 0;
  const results = {};
  for (const id of state.ids) {
    const q = byId.get(id);
    if (!q) continue;
    const want = new Set(q.correctKeys || []);
    const got = new Set(state.answers[id] || []);
    const ok = got.size === want.size && [...got].every(k => want.has(k));
    results[id] = ok;
    if (ok) correct++;
    const d = domainOf(q, state.exam, domainMap);
    if (dom[d]) { dom[d][1]++; if (ok) dom[d][0]++; }
  }
  const used = Math.min(state.duration, Math.round((Date.now() - state.startedAt) / 1000));
  state.submitted = true;
  state.auto = !!auto;
  state.results = results;
  state.summary = { correct, total: state.ids.length, dom, used };
  // history + seen
  state.notSaved = isEmptyAttempt(state.answers, state.ids);
  if (!state.notSaved) {
    const hist = loadHistory();
    hist.push({ exam: state.exam, domain: state.domain || null, mode: state.mode, at: Date.now(), correct, total: state.ids.length, dom, used, timed: state.timed, auto: state.auto, fresh: state.fresh, answered: state.ids.filter(id => (state.answers[id] || []).length).length });
    save(KEY_HISTORY, hist.slice(-HISTORY_MAX));
    const seen = loadSeen();
    seen[state.exam] = Array.from(new Set((seen[state.exam] || []).concat(state.ids)));
    save(KEY_SEEN, seen);
  }
  drop(KEY_ACTIVE);
  view = "results";
  reviewFilter = correct < state.ids.length ? "incorrect" : "all";
  render();
  window.scrollTo(0, 0);
}

// ---------- rendering ----------
function render() {
  if (!root) return Promise.resolve();
  const fn = { setup: renderSetup, exam: renderExam, grid: renderGrid, results: renderResults, review: renderReview }[view];
  return Promise.resolve().then(() => fn && fn()).catch(showError);
}

// Shown instead of a blank screen when anything goes wrong; works without help from index.html.
function showError(err) {
  stopTicking();
  console.warn("Mock exam error", err);
  const msg = (err && (err.message || String(err))) || "unknown error";
  root.innerHTML = `<div class="mk"><button class="linkbtn" data-act="exit">← Question bank</button>
    <h2>Mock exam could not be displayed</h2>
    <div class="panel"><p>Saved mock exam data in this browser seems to be damaged or from an older version.</p>
    <p>Resetting clears this browser's mock exam progress, history, and seen-question list. Bookmarks are not affected.</p>
    <div class="btnrow"><button class="btn" data-act="resetall">Reset mock exam data</button></div>
    <div class="meta">Details: ${esc(msg)}</div></div></div>`;
  root.onclick = (e) => {
    const t = e.target.closest("[data-act]");
    if (!t) return;
    if (t.dataset.act === "exit") { state = null; view = "setup"; exit(); }
    else if (t.dataset.act === "resetall") { resetAllMockData(); state = null; view = "setup"; if (lastOpts) open(lastOpts); }
  };
}

// Same store as the question bank's notice: closed in either place, closed in both.
const KEY_NOTICE = "aws_qbank_notice_closed_v1";
function noticeClosed(exam, text) { return (load(KEY_NOTICE, {}) || {})[exam] === text; }
function closeNotice(exam, text) { const m = load(KEY_NOTICE, {}) || {}; m[exam] = text; save(KEY_NOTICE, m); }

async function renderSetup(extra) {
  const spec = specs[setupExam];
  const docs = await docsFor(setupExam);
  if (setupDomain && !spec.domains.some(d => d.code === setupDomain)) setupDomain = null;
  const seen = new Set(loadSeen()[setupExam] || []);
  const pool = domainDocs(docs);
  const unseen = pool.filter(q => !seen.has(q.id)).length;
  const fullN = Math.min(setupDomain ? SECTION_N : spec.questions, pool.length);
  const shortN = Math.min(SHORT_N, pool.length);
  const perDomain = {};
  docs.forEach(q => { const d = domainOf(q, setupExam, domainMap); perDomain[d] = (perDomain[d] || 0) + 1; });
  const wLabel = spec.weightsAssumed ? "equal weights (official weights not published)" : "official weights";
  const domOpts = `<option value="">All sections · ${wLabel}</option>` + spec.domains.filter(d => perDomain[d.code])
    .map(d => `<option value="${d.code}"${d.code === setupDomain ? " selected" : ""}>${d.code} · ${esc(d.name)} (${perDomain[d.code]})</option>`).join("");
  const domName = setupDomain ? (spec.domains.find(d => d.code === setupDomain) || {}).name : "";
  const hist = loadHistory().filter(h => h.exam === setupExam).slice(-10).reverse();
  const optHtml = ([c, n]) => `<option value="${c}"${c === setupExam ? " selected" : ""}>${c} · ${esc(n)}</option>`;
  const liveExams = (qb.EXAMS || []).filter(([c]) => specs[c]), oldExams = liveExams.filter(e => e[2] === "archive");
  const opts = liveExams.filter(e => e[2] !== "archive").map(optHtml).join("") + (oldExams.length ? `<optgroup label="Archive (retired exams)">${oldExams.map(optHtml).join("")}</optgroup>` : "");
  const mode = (extra && extra.mode) || root.dataset.mode || "full";
  root.dataset.mode = mode;
  root.innerHTML = `<div class="mk">
    <button class="linkbtn" data-act="exit">← Question bank</button>
    <h2>Mock Exam</h2>
    <p class="sub">${setupDomain ? `Timed, answers hidden until you submit. Only questions from ${setupDomain} · ${esc(domName)}; ones you haven't seen in earlier mock exams come first.`
      : `Timed, answers hidden until you submit. Questions follow the ${spec.weightsAssumed ? "domains equally (official weights are not published)" : "official domain weights"}, and ones you haven't seen in earlier mock exams come first.`}</p>
    ${spec.update && !noticeClosed(setupExam, spec.update) ? `<div class="examnotice closable" role="note">${esc(spec.update)}<button class="noticeclose" data-act="closenotice" type="button" aria-label="Close this notice" title="Close">×</button></div>` : ""}
    <div class="panel">
      <select id="mkExam" aria-label="Certification">${opts}</select>
      <select id="mkDomain" aria-label="Section">${domOpts}</select>
      <div class="modes">
        <button class="mode${mode === "full" ? " on" : ""}" data-mode="full" type="button"><b>${setupDomain ? "Full section" : "Full exam"}</b><span>${fullN} questions · ${Math.round(timeFor(spec, fullN) / 60)} min</span></button>
        <button class="mode${mode === "short" ? " on" : ""}" data-mode="short" type="button"><b>Short practice</b><span>${shortN} questions · ${Math.round(timeFor(spec, shortN) / 60)} min</span></button>
      </div>
      <label class="row"><input type="checkbox" id="mkTimed"${setupTimed ? " checked" : ""}> Timer (auto-submits at 0:00)</label>
      <div class="meta">Pool: ${nf(pool.length)} questions${setupDomain ? " in this section" : ""} · ${nf(unseen)} not yet seen in mock exams · ${passMarkMeta(spec)}${setupDomain ? " (whole exam)" : ""}</div>
      ${unseen < (mode === "short" ? shortN : fullN) ? `<div class="meta" style="color:var(--amber)">Fewer unseen questions than needed, so some repeats will be included.</div>` : ""}
      <div class="btnrow"><button class="btn startbtn" data-act="start">Start exam</button>
      ${seen.size ? `<button class="linkbtn" data-act="resetseen">Reset seen questions for ${setupExam}</button>` : ""}</div>
    </div>
    ${readinessHTML(readiness(spec, loadHistory().filter(h => h.exam === setupExam)), setupExam)}
    <div class="panel"><b>Recent attempts · ${setupExam}</b>
      ${hist.length ? `<table><tr><th>Date</th><th>Mode</th><th>Score</th><th>Result</th><th></th></tr>${hist.map(h => {
        const pct = Math.round((h.correct / h.total) * 100); const v = verdictFor(spec, pct);
        return `<tr><td>${new Date(h.at).toLocaleDateString()}</td><td>${h.mode === "short" ? "Short" : "Full"}${h.domain ? " · " + esc(h.domain) : ""}</td><td>${h.correct}/${h.total} (${pct}%)</td><td class="v-${v.key}">${v.label}</td><td><button class="delhist" data-delhist="${h.at}" type="button" aria-label="Remove this attempt from the history" title="Remove this attempt">×</button></td></tr>`;
      }).join("")}</table>` : `<div class="meta">No attempts yet.</div>`}
    </div></div>`;
  root.onclick = async (e) => {
    const t = e.target.closest("[data-act],.mode[data-mode],[data-delhist]");   // not the root itself: it carries data-mode too
    if (!t) return;
    if (t.dataset.mode) { renderSetup({ mode: t.dataset.mode }); return; }
    if (t.dataset.delhist) {   // drop one attempt, e.g. an exam that was only set up and never taken
      if (window.confirm("Remove this attempt from your history?")) { save(KEY_HISTORY, loadHistory().filter(h => !(h.exam === setupExam && String(h.at) === t.dataset.delhist))); renderSetup(); }
      return;
    }
    const act = t.dataset.act;
    if (act === "exit") exit();
    else if (act === "start") startExam(root.dataset.mode, root.querySelector("#mkTimed").checked);
    else if (act === "resetseen") { const s = loadSeen(); delete s[setupExam]; save(KEY_SEEN, s); renderSetup(); }
    else if (act === "closenotice") { closeNotice(setupExam, spec.update); t.closest(".examnotice").remove(); }
  };
  root.querySelector("#mkTimed").onchange = (e) => { setupTimed = e.target.checked; };
  root.querySelector("#mkExam").onchange = (e) => { setupExam = e.target.value; setupDomain = null; renderSetup(); };
  root.querySelector("#mkDomain").onchange = (e) => { setupDomain = e.target.value || null; renderSetup(); };
}

async function renderExam() {
  const docs = await docsFor(state.exam);
  const byId = new Map(docs.map(q => [q.id, q]));
  const id = state.ids[state.cur];
  const q = byId.get(id);
  if (!q) {  // should not happen after validActive(), but never leave a blank screen
    state.ids = state.ids.filter(x => byId.has(x));
    if (!state.ids.length) { drop(KEY_ACTIVE); state = null; view = "setup"; return render(); }
    state.cur = Math.min(state.cur, state.ids.length - 1); persist(); return renderExam();
  }
  const n = state.ids.length;
  const answered = Object.keys(state.answers).filter(k => (state.answers[k] || []).length).length;
  const multi = (q.correctKeys || []).length > 1;
  const picked = new Set(state.answers[id] || []);
  const flagged = state.flags.includes(id);
  const choiceByKey = new Map((q.choices || []).map(c => [c.key, c]));
  const left = state.timed ? (state.deadline - Date.now()) / 1000 : null;
  root.innerHTML = `<div class="mk">
    <div class="mkbar"><i class="mkfill" style="width:${Math.round(answered / n * 100)}%"></i><span class="code">${state.exam}</span><span class="prog">${answered}/${n}<span class="lbl"> answered</span></span>
      <span class="timer${left !== null && left < 300 ? " low" : ""}">${left !== null ? fmtTime(left) : "untimed"}</span>
      <button class="btn" data-act="grid">Review &amp; finish</button></div>
    <div class="qcard">
      <div class="qnum">Question ${state.cur + 1} of ${n}${multi ? ' · <span class="badge multi">Multiple Answers</span>' : ""}${flagged ? ' · <span class="flagmark">⚑ Flagged</span>' : ""}</div>
      <div class="stem">${esc(q.stem)}</div>
      ${multi ? `<div class="selnote">Select ${q.correctKeys.length}.</div>` : ""}
      <div class="choices">${state.order[id].map((k, i) => {
        const c = choiceByKey.get(k);
        return `<div class="choice${picked.has(k) ? " picked" : ""}" role="button" tabindex="0" data-key="${esc(k)}"><span class="bubble"></span><span><span class="key">${LETTERS[i]}.</span> ${esc(c ? c.text : "")}</span></div>`;
      }).join("")}</div>
    </div>
    <div class="nav"><button class="btn ghost" data-act="prev"${state.cur === 0 ? " disabled" : ""}>← Previous</button>
      <button class="flag${flagged ? " on" : ""}" data-act="flag" type="button" aria-pressed="${flagged}">${flagged ? "⚑ Flagged" : "⚐ Flag"}</button>
      ${state.cur < n - 1 ? `<button class="btn" data-act="next">Next →</button>` : `<button class="btn" data-act="grid">Review &amp; submit</button>`}</div>
  </div>`;
  root.onclick = (e) => {
    const ch = e.target.closest(".choice");
    if (ch) {
      const k = ch.dataset.key;
      let cur = new Set(state.answers[id] || []);
      if (multi) { cur.has(k) ? cur.delete(k) : cur.add(k); }
      else cur = new Set([k]);
      state.answers[id] = [...cur];
      persist(); renderExam(); return;
    }
    const t = e.target.closest("[data-act]");
    if (!t || t.disabled) return;
    const act = t.dataset.act;
    if (act === "flag") { state.flags = flagged ? state.flags.filter(x => x !== id) : state.flags.concat(id); persist(); renderExam(); }
    else if (act === "prev") { state.cur = Math.max(0, state.cur - 1); persist(); renderExam(); window.scrollTo(0, 0); }
    else if (act === "next") { state.cur = Math.min(n - 1, state.cur + 1); persist(); renderExam(); window.scrollTo(0, 0); }
    else if (act === "grid") { view = "grid"; render(); window.scrollTo(0, 0); }
  };
  root.onkeydown = (e) => { if ((e.key === "Enter" || e.key === " ") && e.target.closest(".choice")) { e.preventDefault(); e.target.click(); } };
}

function renderGrid(confirming) {
  const n = state.ids.length;
  const unanswered = state.ids.filter(id => !(state.answers[id] || []).length).length;
  const left = state.timed ? (state.deadline - Date.now()) / 1000 : null;
  root.innerHTML = `<div class="mk">
    <div class="mkbar"><span class="code">${state.exam}</span><span class="prog">${n - unanswered}/${n}<span class="lbl"> answered</span></span>
      <span class="timer${left !== null && left < 300 ? " low" : ""}">${left !== null ? fmtTime(left) : "untimed"}</span></div>
    <div class="panel"><b>Review</b>
      <div class="legend"><span><i class="sw ans"></i>answered ${n - unanswered}</span><span><i class="sw"></i>unanswered ${unanswered}</span><span><i class="sw flg"></i>flagged ${state.flags.length}</span><span><i class="sw cur"></i>current</span></div>
      <div class="grid">${state.ids.map((id, i) => `<button class="cell${(state.answers[id] || []).length ? " ans" : ""}${state.flags.includes(id) ? " flg" : ""}${i === state.cur ? " cur" : ""}" data-go="${i}" type="button">${i + 1}</button>`).join("")}</div>
      <div class="btnrow"><button class="btn ghost" data-act="back">Return to question ${state.cur + 1}</button><button class="btn" data-act="ask">Submit exam</button></div>
      ${confirming ? `<div class="confirm">${unanswered ? `<b>${unanswered} unanswered</b> question${unanswered > 1 ? "s" : ""} will be marked wrong. ` : ""}Submit now? You can't change answers afterwards.
        <div class="btnrow"><button class="btn warn" data-act="submit">Yes, submit</button><button class="btn ghost" data-act="back">Keep going</button></div></div>` : ""}
    </div></div>`;
  root.onclick = (e) => {
    const g = e.target.closest("[data-go]");
    if (g) { state.cur = +g.dataset.go; persist(); view = "exam"; render(); window.scrollTo(0, 0); return; }
    const t = e.target.closest("[data-act]");
    if (!t) return;
    if (t.dataset.act === "back") { view = "exam"; render(); }
    else if (t.dataset.act === "ask") renderGrid(true);
    else if (t.dataset.act === "submit") submit(false);
  };
}

function renderResults() {
  const spec = specs[state.exam];
  const { correct, total, dom, used } = state.summary;
  const pct = total ? Math.round((correct / total) * 100) : 0;
  const v = verdictFor(spec, pct, state.mode);
  const wrong = total - correct;
  const nflag = state.flags.length;
  const scored = spec.domains.map(d => ({ code: d.code, c: (dom[d.code] || [0, 0])[0], t: (dom[d.code] || [0, 0])[1] })).filter(d => d.t > 0 && d.c / d.t < 0.7);
  const worst = scored.sort((a, b) => a.c / a.t - b.c / b.t)[0];
  root.innerHTML = `<div class="mk">
    <button class="linkbtn" data-act="exit">← Question bank</button>
    <h2>${state.exam} · ${state.mode === "short" ? "Short practice" : "Full mock exam"}</h2>
    <p class="sub">${esc(examName(state.exam))}${state.auto ? " · submitted automatically when time ran out" : ""}</p>
    <div class="panel">
      <div class="scorerow"><div class="score v-${v.key}">${pct}%</div><div class="verdict v-${v.key}">${v.label}</div></div>
      <div class="statchips"><span>${correct} of ${total} correct</span><span>${wrong} incorrect</span><span>time ${fmtTime(used)}${state.timed ? " of " + fmtTime(state.duration) : ""}</span></div>
      <p class="meta">${esc(v.note)}</p>
      <p class="meta passnote">${esc(passMarkNote(spec))}</p>
      ${state.notSaved ? `<p class="meta notsaved">Not saved: fewer than ${Math.round(EMPTY_ATTEMPT * 100)}% of the questions were answered, so this attempt is left out of your history, seen questions and readiness.</p>` : ""}
    </div>
    <div class="panel"><div class="dhead"><b>By domain</b><span class="meta">Below 70% shows in red</span></div>
      ${spec.domains.map(d => {
        const [c, t] = dom[d.code] || [0, 0]; const p = t ? Math.round((c / t) * 100) : null;
        return `<div class="dom${p !== null && p < 70 ? " weak" : ""}"><div class="top"><span>${d.code} ${esc(d.name)}</span><span>${t ? `${c}/${t} · ${p}%` : "—"}</span></div><div class="bar"><div class="fill" style="width:${p || 0}%"></div></div></div>`;
      }).join("")}
      ${worst ? `<button class="linkbtn practice" data-practice="${worst.code}" type="button">Practice ${worst.code} (weakest) in the question bank →</button>` : ""}
    </div>
    ${readinessHTML(readiness(spec, loadHistory().filter(h => h.exam === state.exam)), state.exam)}
    <div class="rvlabel">Review answers</div>
    <div class="btnrow reviewrow">
      <button class="btn ghost${wrong ? " emph" : ""}" data-review="incorrect"${wrong ? "" : " disabled"}>Incorrect (${wrong})</button>
      <button class="btn ghost" data-review="flagged"${nflag ? "" : " disabled"}>Flagged (${nflag})</button>
      <button class="btn ghost" data-review="all">All (${total})</button>
    </div>
    <div class="btnrow exitrow"><button class="btn" data-act="new">New mock exam</button><button class="btn ghost" data-act="exit">Question bank</button></div>
    <p class="support">${(navigator.language || "").toLowerCase().startsWith("ko")
      ? `도움이 되셨나요? 후원은 선택이며, 모든 문제는 계속 무료입니다. <a href="support.html">☕ Support this site</a>`
      : `Found this useful? Support is optional, and all questions stay free. <a href="support.html">☕ Support this site</a>`}</p>
  </div>`;
  root.onclick = (e) => {
    const pr = e.target.closest("[data-practice]");
    if (pr) return exit({ domain: pr.dataset.practice });
    const r = e.target.closest("[data-review]");
    if (r && !r.disabled) { reviewFilter = r.dataset.review; view = "review"; render(); window.scrollTo(0, 0); return; }
    const t = e.target.closest("[data-act]");
    if (!t) return;
    if (t.dataset.act === "exit") exit();
    else if (t.dataset.act === "new") { setupExam = state.exam; state = null; view = "setup"; render(); window.scrollTo(0, 0); }
  };
}

async function renderReview() {
  const docs = await docsFor(state.exam);
  if (qb.ensureExplanations) await qb.ensureExplanations(docs);
  const byId = new Map(docs.map(q => [q.id, q]));
  const list = state.ids.map((id, i) => ({ id, i })).filter(({ id }) =>
    reviewFilter === "all" ? true : reviewFilter === "flagged" ? state.flags.includes(id) : !state.results[id]);
  const counts = { incorrect: state.ids.filter(id => !state.results[id]).length, flagged: state.flags.length, all: state.ids.length };
  root.innerHTML = `<div class="mk">
    <button class="linkbtn" data-act="results">← Results</button>
    <h2>Review · ${state.exam}</h2>
    <div class="tabs">${["incorrect", "flagged", "all"].map(f => `<button class="tab${f === reviewFilter ? " on" : ""}" data-filter="${f}">${f[0].toUpperCase() + f.slice(1)} (${counts[f]})</button>`).join("")}</div>
    ${list.length ? "" : `<div class="empty">Nothing to show here.</div>`}
    ${list.map(({ id, i }) => {
      const q = byId.get(id); if (!q) return "";
      const want = new Set(q.correctKeys || []);
      const got = new Set(state.answers[id] || []);
      const ok = state.results[id];
      const choiceByKey = new Map((q.choices || []).map(c => [c.key, c]));
      const letters = state.order[id].map((k, j) => want.has(k) ? LETTERS[j] : null).filter(Boolean).join(", ");
      const bm = qb.isBookmarked(id);
      return `<div class="qcard rv" data-qid="${esc(id)}">
        <div class="rvhead"><span>#${i + 1}</span><span class="mono">${esc(id)}</span><span class="${ok ? "ok" : "no"}">${ok ? "✓ Correct" : got.size ? "✗ Incorrect" : "✗ Unanswered"}</span><span class="rvdom">${esc(domainOf(q, state.exam, domainMap))}</span>${state.flags.includes(id) ? "<span>⚑ flagged</span>" : ""}
          <button class="bookmark-btn${bm ? " active" : ""}" data-bm="${esc(id)}" type="button" aria-label="Bookmark this question">${bm ? "★" : "☆"}</button></div>
        <div class="stem">${esc(q.stem)}</div>
        <div class="choices">${state.order[id].map((k, j) => {
          const c = choiceByKey.get(k);
          const cls = want.has(k) ? "correct" : got.has(k) ? "incorrect" : "dim";
          return `<div class="choice locked ${cls}${got.has(k) ? " picked" : ""}"><span class="bubble"></span><span><span class="key">${LETTERS[j]}.</span> ${esc(c ? c.text : "")}${got.has(k) ? ' <span class="yours">· your answer</span>' : ""}</span></div>`;
        }).join("")}</div>
        <details class="rvexp"${ok ? "" : " open"}><summary>${ok ? "Show explanation" : "Explanation"}</summary>
        <div class="explain show ${ok ? "" : "wrong"}" id="mk-explain-${esc(id)}"><div class="ans-line">Answer: ${letters}</div>${qb.explainHtml ? qb.explainHtml(q.explanation, Object.fromEntries(state.order[id].map((k, j) => [k, LETTERS[j]]))) : `<div class="exp-body">${esc(q.explanation)}</div>`}</div></details>
        <div class="remarks"><span class="tags">#${i + 1} · ${esc(id)}</span>
          <button class="bookmark-foot${bm ? " active" : ""}" data-bm="${esc(id)}" type="button" aria-label="Bookmark this question" title="Bookmark this question">${bm ? "★" : "☆"}</button></div>
      </div>`;
    }).join("")}
    <div class="btnrow"><button class="btn ghost" data-act="results">Back to results</button></div>
  </div>`;
  list.forEach(({ id }) => { const el = document.getElementById(`mk-explain-${id}`); if (el && qb.attachDiagram) qb.attachDiagram(id, el); });
  root.onclick = (e) => {
    const f = e.target.closest("[data-filter]");
    if (f) { reviewFilter = f.dataset.filter; renderReview(); return; }
    const b = e.target.closest("[data-bm]");
    if (b) {
      const on = qb.toggleBookmark(b.dataset.bm);
      // the top and bottom stars of a review card stay in step
      b.closest(".rv").querySelectorAll("[data-bm]").forEach(x => { x.classList.toggle("active", on); x.textContent = on ? "★" : "☆"; });
      return;
    }
    const t = e.target.closest("[data-act]");
    if (t && t.dataset.act === "results") { view = "results"; render(); window.scrollTo(0, 0); }
  };
}
