// Unit tests for mock exam drawing: node tools/mock_unit_test.mjs
import { draw, drawFocused, allocate, domainOf, shuffle, verdictFor, readiness, targetPct } from "../js/mock.js";
import fs from "fs";
const specs = JSON.parse(fs.readFileSync("data/exam-specs.json"));
const map = JSON.parse(fs.readFileSync("data/exam-domains.json"));
let fails = 0;
const ok = (name, cond, info = "") => { if (!cond) { fails++; console.log("FAIL", name, info); } };
for (const exam of Object.keys(specs).filter(k => !k.startsWith("_"))) {
  const spec = specs[exam];
  const docs = JSON.parse(fs.readFileSync(`data/${exam}.json`));
  const doms = new Set(spec.domains.map(d => d.code));
  const orphan = docs.filter(q => !doms.has(domainOf(q, exam, map))).map(q => q.id);
  ok(`${exam} every question maps to an exam domain`, orphan.length === 0, orphan.join(","));
  for (const n of [spec.questions, 20]) {
    const ids = draw(exam, n, docs, spec, map, []);
    ok(`${exam} n=${n} size`, ids.length === Math.min(n, docs.length), ids.length);
    ok(`${exam} n=${n} unique`, new Set(ids).size === ids.length);
    const byId = new Map(docs.map(q => [q.id, q]));
    const cnt = {}; ids.forEach(id => { const d = domainOf(byId.get(id), exam, map); cnt[d] = (cnt[d] || 0) + 1; });
    // weights are relative (Azure stores the midpoints of published ranges, which need not add up to 100)
    const total = spec.domains.reduce((s, o) => s + o.weight, 0);
    for (const d of spec.domains) {
      const supply = docs.filter(q => domainOf(q, exam, map) === d.code).length;
      const expect = n * d.weight / total;
      const got = cnt[d.code] || 0;
      // exact weight within rounding, unless the pool itself is short for this domain (then all of it is used);
      // when other domains are short the shortfall is redistributed, so a domain may exceed its weight (pilot pools)
      const othersShort = spec.domains.some(o => o.code !== d.code && docs.filter(q => domainOf(q, exam, map) === o.code).length < n * o.weight / total);
      ok(`${exam} n=${n} ${d.code} weight`, Math.abs(got - expect) <= 1 || (supply < expect && got === supply) || (othersShort && got >= Math.floor(expect) && got <= supply), `${got} vs ${expect.toFixed(1)} (supply ${supply})`);
      if (supply < expect) console.log(`  note: ${exam} ${d.code} pool (${supply}) is smaller than one full exam needs (${expect.toFixed(1)})`);
    }
  }
  // recent memory: even with nothing marked seen (after "Reset seen"), a draw avoids the last mocks while the pool allows
  {
    const a = draw(exam, spec.questions, docs, spec, map, [], []);
    const b = draw(exam, spec.questions, docs, spec, map, [], a);
    const supplyByDom = Object.fromEntries(spec.domains.map(d => [d.code, docs.filter(q => domainOf(q, exam, map) === d.code).length]));
    const allocA = allocate(spec.questions, spec.domains, supplyByDom);
    const forced = spec.domains.reduce((s, d) => s + Math.max(0, (allocA[d.code] || 0) - (supplyByDom[d.code] - (allocA[d.code] || 0))), 0);
    ok(`${exam} recent draw is avoided`, b.filter(id => a.includes(id)).length <= forced, `${b.filter(id => a.includes(id)).length} > ${forced}`);
  }
  // unseen preference: after one full exam, the next draws avoid those ids while unseen supply lasts
  const first = draw(exam, spec.questions, docs, spec, map, []);
  const second = draw(exam, spec.questions, docs, spec, map, first);
  const overlap = second.filter(id => first.includes(id)).length;
  const byId = new Map(docs.map(q => [q.id, q]));
  // expected minimum overlap: per domain, need beyond unseen supply
  let minOverlap = 0;
  const alloc = allocate(spec.questions, spec.domains, Object.fromEntries(spec.domains.map(d => [d.code, docs.filter(q => domainOf(q, exam, map) === d.code).length])));
  for (const d of spec.domains) {
    const unseenSupply = docs.filter(q => domainOf(q, exam, map) === d.code && !first.includes(q.id)).length;
    minOverlap += Math.max(0, alloc[d.code] - unseenSupply);
  }
  ok(`${exam} second exam prefers unseen`, overlap === minOverlap, `${overlap} vs min ${minOverlap}`);
  console.log(exam, "pool", docs.length, "full", spec.questions, "overlap on 2nd draw", overlap);
  // section-only draw: only that domain, unique, capped by the pool, unseen first
  for (const d of spec.domains) {
    const pool = docs.filter(q => domainOf(q, exam, map) === d.code);
    if (!pool.length) continue;
    const ids = drawFocused(exam, 20, docs, d.code, map, []);
    ok(`${exam} ${d.code} focused size`, ids.length === Math.min(20, pool.length), ids.length);
    ok(`${exam} ${d.code} focused only this domain`, ids.every(id => domainOf(byId.get(id), exam, map) === d.code));
    ok(`${exam} ${d.code} focused unique`, new Set(ids).size === ids.length);
    const seenIds = pool.slice(0, Math.max(0, pool.length - 5)).map(q => q.id);
    const next = drawFocused(exam, 5, docs, d.code, map, seenIds);
    ok(`${exam} ${d.code} focused prefers unseen`, next.every(id => !seenIds.includes(id)) || pool.length <= 5, next.join(","));
  }
}
// allocation edge cases
const a = allocate(10, [{ code: "D1", weight: 50 }, { code: "D2", weight: 50 }], { D1: 2, D2: 100 });
ok("allocate caps by supply and redistributes", a.D1 === 2 && a.D2 === 8, JSON.stringify(a));
// verdicts: a perfect score has its own wording; 99% keeps the generic pass-ready note
{
  const sp = { level: "associate" };
  ok("100% is a perfect score", verdictFor(sp, 100, "short").label === "Perfect score" && verdictFor(sp, 100, "full").label === "Perfect score");
  ok("perfect score note differs for short and full", verdictFor(sp, 100, "short").note !== verdictFor(sp, 100, "full").note);
  ok("99% is still pass-ready with the margin note", verdictFor(sp, 99).label === "Pass-ready" && /comfortable margin/.test(verdictFor(sp, 99).note));
  ok("perfect score never says 80%+ on first attempts", !/\d+%\+/.test(verdictFor(sp, 100, "full").note));
}
// readiness: 3 full timed exams in a row at the target, mostly unseen, finished in time, and every domain 70%+
{
  const sp = { level: "associate", domains: [{ code: "D1", name: "a", weight: 50 }, { code: "D2", name: "b", weight: 50 }] };
  const run = (pct, o = {}) => ({ exam: "X", mode: "full", domain: null, timed: true, auto: false, fresh: 65, total: 65, correct: Math.round(65 * pct / 100), dom: { D1: [pct, 100], D2: [pct, 100] }, ...o });
  ok("target: associate 80, professional 85, percent pass mark +10", targetPct(sp) === 80 && targetPct({ level: "professional" }) === 85 && targetPct({ passingPct: 70 }) === 80);
  ok("no history is not ready", !readiness(sp, []).ready && readiness(sp, []).streak === 0);
  ok("three qualifying exams are ready", readiness(sp, [run(82), run(85), run(81)]).ready);
  ok("two are not enough", readiness(sp, [run(82), run(85)]).streak === 2 && !readiness(sp, [run(82), run(85)]).ready);
  ok("a latest exam below target breaks the streak", readiness(sp, [run(85), run(85), run(70)]).streak === 0);
  ok("running out of time does not count", readiness(sp, [run(85), run(85), run(85, { auto: true })]).streak === 0);
  ok("untimed does not count", readiness(sp, [run(85), run(85), run(85, { timed: false })]).streak === 0);
  ok("mostly repeated questions do not count", readiness(sp, [run(85), run(85), run(85, { fresh: 20 })]).streak === 0);
  ok("unknown freshness (older history) still counts", readiness(sp, [run(85), run(85), run(85, { fresh: undefined })]).ready);
  ok("a weak domain blocks readiness", !readiness(sp, [run(85, { dom: { D1: [95, 100], D2: [20, 100] } }), run(85), run(85)]).ready);
  ok("short practice and section drills are ignored", readiness(sp, [run(85), run(85), run(85), run(10, { mode: "short" }), run(10, { domain: "D1" })]).ready);
}
// the shuffle is uniform: each of 4 items lands in each slot about 1/4 of the time
{
  const N = 40000, slots = Array.from({ length: 4 }, () => [0, 0, 0, 0]);
  for (let r = 0; r < N; r++) shuffle([0, 1, 2, 3]).forEach((item, pos) => slots[item][pos]++);
  const worst = Math.max(...slots.flat().map(c => Math.abs(c / N - 0.25)));
  ok("shuffle is uniform", worst < 0.01, worst);
  ok("shuffle keeps every item once", shuffle([1, 2, 3, 4, 5]).sort().join() === "1,2,3,4,5");
}
console.log(fails ? `${fails} FAILED` : "ALL PASS");
process.exit(fails ? 1 : 0);
