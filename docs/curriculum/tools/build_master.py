import re
import sys
import pathlib
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
D = pathlib.Path(__file__).resolve().parent.parent
BANDS = ["Foundations", "Building", "Connecting", "Expanding", "Mastery"]
EX_PER_LESSON, BANK_PER_LESSON = 14, 20


def table_after(lines, heading_re):
    for i, l in enumerate(lines):
        if l.startswith("#") and re.search(heading_re, l, re.I):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("|"):
                j += 1
            k = j
            while k < len(lines) and lines[k].startswith("|"):
                k += 1
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in lines[j:k]]
            return rows[2:]  # drop header + separator
    raise SystemExit("table not found for " + heading_re)


def num(s):
    m = re.search(r"\d[\d,]*", s or "")
    return int(m.group(0).replace(",", "")) if m else 0


def clean(s):
    return re.sub(r"\*\*", "", s or "").strip()


def row(strand, section, band, lessons, ex, bank, test, cert):
    return dict(strand=strand, section=section, band=band, lessons=clean(lessons), lessons_n=num(lessons),
                ex_n=num(ex), bank=clean(bank), bank_n=num(bank), test=clean(test), cert=clean(cert), added=0)


rows = []

# grammar 1-7: | Section | Band | Lessons | Exercises | Bank | Test | Certificate |
lines = (D / "grammar-sections-1-7.md").read_text(encoding="utf-8").splitlines()
name = None
for r in table_after(lines, r"summary table"):
    if len(r) < 7 or "total" in r[0].lower():
        continue
    sec = clean(r[0])
    if not re.fullmatch(r"\d+", sec):
        name = sec
    rows.append(row("Grammar", name, clean(r[1]), r[2], r[3], r[4], r[5], r[6]))

# verbs & tenses strand replaces section 4 (same summary-table format; every row carries its own label)
rows = [r for r in rows if not re.match(r"4\b", r["section"] or "")]
lines = (D / "verbs-and-tenses.md").read_text(encoding="utf-8").splitlines()
for r in table_after(lines, r"summary table"):
    if len(r) < 7 or "total" in r[0].lower():
        continue
    rows.append(row("Grammar", clean(r[0]), clean(r[1]), r[2], r[3], r[4], r[5], r[6]))

# grammar 8-12: | Section × band | Lessons | Exercises (total) | Bank size | Test size | Certificate name |
lines = (D / "grammar-sections-8-12.md").read_text(encoding="utf-8").splitlines()
name = None
for r in table_after(lines, r"summary table"):
    if len(r) < 6 or "total" in r[0].lower():
        continue
    left, _, band = clean(r[0]).partition("·")
    left = left.strip()
    band = band.strip()
    if not re.fullmatch(r"\d+", left):
        name = left
    rows.append(row("Grammar", name, band, r[1], r[2], r[3], r[4], r[5]))

# coverage-map additions: | Section | Band | New lessons | Topics |
lines = (D / "grammar-coverage-map.md").read_text(encoding="utf-8").splitlines()
added_total = 0
for r in table_after(lines, r"additions to existing sections"):
    if len(r) < 4:
        continue
    sec, band, n = clean(r[0]), clean(r[1]), num(r[2])
    hit = [x for x in rows if x["strand"] == "Grammar" and re.match(rf"{sec}\b", x["section"] or "") and x["band"] == band]
    if not hit:
        raise SystemExit(f"addition target not found: section {sec} {band}")
    x = hit[0]
    x["lessons_n"] += n
    x["ex_n"] += n * EX_PER_LESSON
    x["bank_n"] += n * BANK_PER_LESSON
    x["added"] += n
    x["lessons"] = str(x["lessons_n"])
    x["bank"] = str(x["bank_n"])
    added_total += n

# writing (later phase): | Level × band | Lessons | Exercises total | Bank size | Test size | Certificate name |
lines = (D / "writing-strand.md").read_text(encoding="utf-8").splitlines()
wrows = []
for r in table_after(lines, r"summary table"):
    if len(r) < 6 or "total" in r[0].lower():
        continue
    level, _, band = clean(r[0]).partition("×")
    bank = clean(r[3])
    bank_n = max([num(x) for x in bank.split("/")] or [0])
    wr = row("Writing", level.strip(), band.strip(), r[1], r[2], bank, r[4], r[5])
    wr["bank_n"] = bank_n
    wrows.append(wr)

# proofreading checkpoints (plan section 2.3 of listening-speaking-and-proofreading.md)
cp_spec = {"Foundations": ("60-90", 5, "2", "10", "8/10"), "Building": ("100-140", 6, "2", "12", "10/12"),
           "Connecting": ("160-220", 8, "2-3", "16-24", "13/16 or 20/24"), "Expanding": ("240-320", 10, "3", "30", "24/30"),
           "Mastery": ("330-420", 12, "3", "36", "29/36")}
cps = [("CP1", "after sections 1-4"), ("CP2", "after sections 5-8"), ("CP3", "after sections 9-12")]

# ---------- totals ----------
g = [r for r in rows if r["strand"] == "Grammar"]


def tot(rs, k):
    return sum(r[k] for r in rs)


T = dict(g_lessons=tot(g, "lessons_n"), g_ex=tot(g, "ex_n"), g_bank=tot(g, "bank_n"), g_tests=len(g),
         w_lessons=tot(wrows, "lessons_n"), w_ex=tot(wrows, "ex_n"), w_bank=tot(wrows, "bank_n"),
         w_tests=len([r for r in wrows if r["bank_n"] > 0]))
T["cps"] = len(cps) * len(BANDS)
by_band = {b: [r for r in g if r["band"] == b] for b in BANDS}
vt = [r for r in g if re.match(r"4[A-Z]", r["section"] or "")]


def code_name(section):
    m = re.match(r"(\d+[A-Z]?(?:\+\d?[A-Z])*)\s*(.*)", section)
    return (m.group(1), m.group(2)) if m else ("", section)


# ---------- write master ----------
out = []
A = out.append
A("# ATTP English Platform — Master Curriculum Table (grammar-based)")
A("")
A("Built from the strand plans in this folder on the rules in `00-platform-frame.md`. Scope decision 2026-09-05: the platform is grammar-based for now; the Verbs and Tenses strand replaces the old Section 4; the coverage map adds the lessons that the section plans were missing; the Listening & Speaking strand is deferred; the Writing strand is a later phase (listed at the end). Every grammar row is one certificate-bearing unit: explain → exercises → test (15 questions drawn from the bank, pass 12/15) → certificate, with remediation back to the exact lesson. Students see band names, never grades.")
A("")
A("## 1. Totals (in scope now)")
A("")
A("| Strand | Units (tests) | Lessons | Exercises in lessons | Bank items (planned) | Certificates |")
A("|---|---|---|---|---|---|")
A(f"| Grammar sections 1-3, 5-12 (11 sections × 5 bands, plus the coverage-map additions) | {len(g) - len(vt)} | {T['g_lessons'] - tot(vt, 'lessons_n')} | {T['g_ex'] - tot(vt, 'ex_n'):,} | {T['g_bank'] - tot(vt, 'bank_n'):,} | {len(g) - len(vt)} |")
A(f"| Verbs and Tenses strand (units 4A-4O, replaces Section 4) | {len(vt)} | {tot(vt, 'lessons_n')} | {tot(vt, 'ex_n'):,} | {tot(vt, 'bank_n'):,} | {len(vt)} |")
A(f"| Proofreading checkpoints (CP1-CP3 × 5 bands) | {T['cps']} | — | 2-3 passages each | 127 topics → 300+ passages | pass/continue |")
A(f"| **Total grammar** | **{T['g_tests']} tests + {T['cps']} checkpoints** | **{T['g_lessons']}** (+37 existing Sentence Builder) | **{T['g_ex']:,}** | **{T['g_bank']:,}** | **{T['g_tests']}** |")
A("")
A(f"Of the {T['g_lessons']} lessons, {added_total} come from the coverage-map additions (quantifiers, adverb types, prepositions of time and place, noun and adverb clauses, question tags and the rest listed in `grammar-coverage-map.md`) and {tot(vt, 'lessons_n')} from the Verbs and Tenses strand, which replaced the 28 lessons of the old Section 4.")
A("")
A("### Lessons and tests per band")
A("")
A("| Band | Units (tests) | Lessons | Exercises | Bank items |")
A("|---|---|---|---|---|")
for b in BANDS:
    rs = by_band[b]
    A(f"| {b} | {len(rs)} | {tot(rs, 'lessons_n')} | {tot(rs, 'ex_n'):,} | {tot(rs, 'bank_n'):,} |")
A("")
A("## 2. Grammar — every section × band")
A("")
A("Rows marked with a plus sign in the Lessons column include lessons added by the coverage map (for example 5+3 = 5 planned in the section plan plus 3 added).")
A("")
A("| # | Section / unit | Band | Lessons | Exercises | Bank | Test | Certificate |")
A("|---|---|---|---|---|---|---|---|")
order = {b: i for i, b in enumerate(BANDS)}


def sort_key(r):
    code, _ = code_name(r["section"])
    m = re.match(r"(\d+)", code)
    return (int(m.group(1)) if m else 99, order.get(r["band"], 9), code)


for r in sorted(g, key=sort_key):
    code, nm = code_name(r["section"])
    lessons = f"{r['lessons_n'] - r['added']}+{r['added']}" if r["added"] else str(r["lessons_n"])
    A(f"| {code} | {nm} | {r['band']} | {lessons} | {r['ex_n']} | {r['bank_n']} | {r['test']} | {r['cert']} |")
A("")
A("## 3. Verbs and Tenses strand — the units at a glance")
A("")
A("| Unit | Covers | Bands |")
A("|---|---|---|")
units = [("4A", "be, have, do; helping verbs", "Foundations"),
         ("4B", "present simple: form, spelling, habits, facts, schedules, stative verbs, time clauses, narrative present", "Foundations-Connecting"),
         ("4C", "present continuous: now, temporary, arrangements, trends, always + -ing, stative shifts, softening", "Foundations-Connecting"),
         ("4D", "past simple: regular and irregular, did, time words, sequencing, narrative", "Foundations-Connecting"),
         ("4E", "past continuous: interrupted actions, background, parallel actions, tentative use", "Building-Connecting"),
         ("4F", "present perfect: experience, just/already/yet, for/since, gone/been, vs past simple, unfinished time, news, superlatives, reports, US/UK", "Building-Expanding"),
         ("4G", "present perfect continuous: duration, recent activity, vs simple", "Connecting-Expanding"),
         ("4H", "past perfect and past perfect continuous; by the time; narrative; reported speech and third conditional links", "Connecting-Expanding"),
         ("4I", "future forms: will, going to, present forms, future continuous, future perfect (continuous), be about to / due to / be to, future in the past, formal futures", "Building-Mastery"),
         ("4J", "used to, would, be used to, get used to", "Building-Connecting"),
         ("4K", "passive: all tenses, agent, modals, two objects, impersonal, get-passive, infinitives/gerunds, academic use, style", "Building-Mastery"),
         ("4L", "verb patterns: -ing vs to, meaning changes, object + to, bare infinitive, transitive/intransitive, preposition + -ing, purpose, perception verbs, causatives, perfect/passive forms", "Connecting-Mastery"),
         ("4M", "phrasal verbs: separable/inseparable, three-part, register, themes, passive, formal equivalents", "Building-Mastery"),
         ("4N", "irregular verbs: 200 in three sets by pattern; past form vs past participle", "Foundations-Connecting"),
         ("4O", "tense consistency, future time clauses, sequencing, narrative tense mix, tense in reports and research", "Connecting-Mastery")]
for u, c, b in units:
    A(f"| {u} | {c} | {b} |")
A("")
A("## 4. Proofreading checkpoints — every checkpoint × band")
A("")
A("| Checkpoint | Position | Band | Words per passage | Errors per passage | Passages | Errors per checkpoint | Pass (80%) |")
A("|---|---|---|---|---|---|---|---|")
for cp, pos in cps:
    for b in BANDS:
        wpp, epp, pcs, epc, ps = cp_spec[b]
        A(f"| {cp} | {pos} | {b} | {wpp} | {epp} | {pcs} | {epc} | {ps} |")
A("")
A("Errors planted are cumulative over the sections passed so far at that band; a miss sends the student to the lesson for that rule and then to a new passage. Passages are about well-known general-knowledge subjects (127 topics in 8 groups: inventions, discoveries, historical events, famous places, notable people, science and nature, health and daily life, work and money), fact-checked against two references and credited.")
A("")
A("## 5. Later phase — Writing strand (not in the totals above)")
A("")
A(f"{T['w_tests']} tests, {T['w_lessons']} new lessons (+37 existing Sentence Builder), {T['w_ex']:,} exercises, {T['w_bank']:,} bank items target. Plan complete in `writing-strand.md`; built after the grammar sections.")
A("")
A("| Level | Band | Lessons | Exercises | Bank | Test | Certificate |")
A("|---|---|---|---|---|---|---|")
for r in wrows:
    A(f"| {r['section']} | {r['band']} | {r['lessons']} | {r['ex_n']} | {r['bank']} | {r['test']} | {r['cert']} |")
A("")
A("## 6. Deferred — Listening & Speaking strand")
A("")
A("Not in scope for now (decision 2026-09-05). The plan in `listening-speaking-and-proofreading.md` (80 lessons, listening tests, speaking badges, audio pipeline) stays ready for a later phase; only its proofreading checkpoints are used now.")
A("")
A("## 7. Where the detail lives")
A("")
A("| File | Contents |")
A("|---|---|")
A("| `00-platform-frame.md` | bands, lesson loop, exercise catalogue, bank quality bar, checkpoints, engines, phone rules, teacher side, build phases |")
A("| `grammar-coverage-map.md` | the full inventory of English grammar and usage topics with their section, band and status; the additions table read by this builder |")
A("| `verbs-and-tenses.md` | units 4A-4O: every lesson with rule, examples and errors to watch; exercise mix; banks; certificates; sources |")
A("| `grammar-sections-1-7.md` | sections 1-3 and 5-7: every lesson (rule, variants, examples, ESL errors by first language), exercise counts, tests, remediation maps, sources, disagreements decided (Section 4 there is superseded) |")
A("| `grammar-sections-8-12.md` | sections 8-12, with the punctuation/usage conventions decided (serial comma, quotation marks, data is/are, possessives, dashes, numbers, titles) |")
A("| `writing-strand.md` | later phase: sentence, paragraph, essay-type and research lessons; MLA 9, APA 7, Chicago 18; 100 adult prompts; rubrics |")
A("| `listening-speaking-and-proofreading.md` | deferred strand plus the checkpoint error types per band, passage spec, 127 topics, 3 worked passages with keys |")
A("| `../standards-mapping.md` | calibration to California ELD, Texas ELPS, Virginia SOL, WIDA and CEFR (internal only) |")
A("")
A("## 8. Verification standard for everything above")
A("")
A("Every rule: confirmed by 6-10 well-known sources listed in the plan; disagreements recorded with the convention taught (standard American classroom usage) and variants accepted in answer keys where correct. Every passage fact: two references of different types, credit line, 12-month re-check. Every bank item: automatic checks, two independent review passes, teacher spot-check, in-app problem reports. Items not yet verified are listed at the end of each plan under 'Verification notes' and are cleared before those items are authored; the Verbs and Tenses strand and the coverage-map additions are drafted and await their source check.")
(D.parent / "curriculum-master.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("wrote curriculum-master.md;", len(rows), "grammar rows incl.", len(vt), "tenses units;", "totals:", T, "added:", added_total)
for b in BANDS:
    rs = by_band[b]
    print(b, len(rs), tot(rs, "lessons_n"), tot(rs, "ex_n"), tot(rs, "bank_n"))
