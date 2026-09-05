# ATTP English Platform — the frame everything hangs on

This file fixes the rules that every strand, section, lesson, test and bank must follow.
The strand plans (grammar sections 1-7, 8-12, writing, listening-speaking + proofreading)
fill in the content; this file is the contract they fill it into.

## 1. Who it is for

Adult ESL learners from many countries and first languages, from complete beginners
(including elders who have never studied English) to C1. No school grades are ever shown.
Topics are adult and real: work, family, health, money, community, travel, and general
knowledge (history, inventions, discoveries, famous places and people).

## 2. The five bands (student-facing names)

| Band | Name | CEFR | A learner here can... |
|---|---|---|---|
| 1 | Foundations | A1 | write short present-tense sentences about familiar things |
| 2 | Building | A2 | link simple sentences with and/but/because into a short paragraph |
| 3 | Connecting | B1 | write connected multi-paragraph texts with complex sentences |
| 4 | Expanding | B2 | write clear essays that argue and use sources (MLA/APA) |
| 5 | Mastery | C1 | write polished, complex texts and a full research paper to a style manual |

The mapping to California ELD, Texas ELPS, Virginia SOL and WIDA is internal calibration
only (docs/standards-mapping.md). Students see band names, never grades.

## 3. The four strands

| Strand | What it teaches | Certified by |
|---|---|---|
| Grammar | 13 sections, each revisited across bands (spiral) | section test per band |
| Listening & Speaking | sounds, stress, rhythm, listening skills; speaking practice | listening test per band; speaking = practice badge (+ optional teacher grade) |
| Writing | sentence → paragraph → essay types → research paper | level test per band (auto part + writing part) |
| Proofreading checkpoints | cumulative mastery checks between grammar units | checkpoint pass |

## 4. The lesson loop (identical everywhere)

1. **Explain** — one rule per screen, in plain words a slow beginner can follow; examples
   before terminology; every screen has a play button that reads it aloud.
2. **Exercises** — 8-20 items per lesson from the exercise catalogue below, with instant
   feedback that says *why*, and hints before answers (never leave a student stuck).
3. **Section test** — 15 questions drawn at random from that section's bank at that band,
   different every attempt. Pass mark **80%** (12/15).
4. **Certificate** — on passing: a certificate naming the section and band, the student's
   name and date, with a verification code.
5. **Remediation** — every bank item is tagged with the lesson that teaches it. A failed
   test lists the missed lessons, sends the student back to them (explain + a fresh set of
   exercises), then offers a new test with new questions.

## 5. Exercise catalogue (exact type names used by every plan)

| Type | The student... | Auto-checked by |
|---|---|---|
| mc | picks the right option | answer key |
| click | taps the word with a given role | answer key |
| next | picks which word comes next | answer key |
| gap | types the missing word | key + accepted variants (whole-sentence answers accepted) |
| order | puts words in order | key (+ accepted alternative orders) |
| error-spot | taps the wrong word | key |
| transform | rewrites a sentence (tense, number, join, report) | key + variants, rules engine assist |
| match | pairs items | key |
| classify | sorts words into groups | key |
| sequence-paragraphs | orders sentences/paragraphs | key |
| listen-choose | hears audio, picks the answer | key |
| listen-order | hears audio, orders items | key |
| dictation | hears audio, types it | key + tolerant matching |
| minimal-pair-choose | hears one of two similar words, picks it | key |
| say-it / repeat-after / shadowing | reads or repeats aloud | phone speech recognizer, word-level |
| record-for-teacher | records a clip and sends it | teacher |
| write | writes freely to a prompt | rules engine + structure rubric (+ teacher) |
| proofread-passage | finds each planted error and types the fix | key + variants |

## 6. Banks and their quality bar

- Section bank: 100-120 items per section per band; a test draws 15. Whole-platform
  target: 1,000+ grammar items in phase 1, growing to several thousand.
- Passage bank: 300+ proofreading passages over time; each checkpoint draws 2-3.
- Every rule in a lesson is confirmed by **6-10 well-known sources** (Khan Academy, Purdue
  OWL, British Council, Cambridge, Oxford, Merriam-Webster, Chicago Manual, MLA Style
  Center, APA Style, university writing centres), recorded in a source registry the teacher
  can audit. Where sources disagree, teach the standard American classroom convention, name
  the variant, and accept both in answer keys where both are correct.
- Every fact in a passage is confirmed by at least two reliable references and credited.
- Every bank item passes: (a) automatic checks (exactly one correct answer; distractors
  provably wrong; accepted variants listed; no duplicates; reading level within band),
  (b) at least two independent review passes that try to find a second valid answer,
  (c) teacher spot-check before release, (d) an in-app "report a problem" button that
  flags the item in the teacher dashboard.

## 7. Proofreading checkpoints

| Checkpoint | After grammar sections | Cumulative error types allowed |
|---|---|---|
| CP1 | 1-4 (sentence anatomy, nouns/articles, pronouns, verb tense) | everything taught in 1-4 at this band |
| CP2 | 5-8 (agreement, modals/conditionals, adjectives/adverbs, prepositions) | 1-8 |
| CP3 | 9-12 (conjunctions, questions/reported speech, punctuation, cohesion) | 1-12 |

Each checkpoint: 2-3 passages about well-known general-knowledge subjects; find every error
and type the correction; pass = 80% of errors found *and* correctly fixed; a miss sends the
student to the lesson for that rule, then to a **new** passage. Passage length and planted
errors per passage rise with the band (specified in the listening-speaking-and-proofreading
plan).

## 8. Engines (all free, all on the phone)

| Job | Engine | Needs internet? |
|---|---|---|
| Grammar checking of free writing | Harper rules engine (15 MB, once) | no, after first load |
| Structure checks of writing | rubric rules in the app | no |
| Coaching tips on writing and speech | small on-device language model (opt-in, ~1 GB, capable phones only) | no, after download |
| Read-aloud voice | pre-generated natural speech (Sesame CSM) shipped as audio files; phone voice as fallback | no, after the section is saved |
| Speech recognition for say-it | phone's built-in recognizer | usually yes |
| Progress sync, teacher dashboard | Cloudflare relay (free tier), GitHub repo as permanent record | yes, when available; queues offline |

Nothing is graded by the language model; answer keys, the rules engine and the teacher grade.

## 9. Phone-first rules

Works on a low-end Android (2-3 GB) and older iPhones; Safari and Chrome tested every release;
sections are small packages saved offline on first open; downloads shown before they happen,
large ones opt-in with a Wi-Fi reminder; one task per screen, large text, no timers, read-aloud
everywhere; progress saved on the phone first, synced when possible; nothing appears in the
student's Files app; no store install (home-screen shortcut only).

## 10. Teacher side

Login on the relay; dashboard: classes and class codes, per-student progress per section,
test and checkpoint attempts, writing and speaking submissions to grade, certificates issued
(with verification), problem reports, controls (open/close sections, pass mark, reset a
student), export. Data lives on the relay with daily snapshots committed to the GitHub repo.

## 11. Build phases

1. Engine + hub + relay + dashboard skeleton + Foundations sections 1-2 with verified banks.
2. Proofreading checkpoint engine + first passage bank.
3. Remaining grammar sections, band by band, Foundations first.
4. Listening & Speaking strand (audio generation pipeline, say-it).
5. Writing strand: paragraph, essay types, research paper (MLA/APA/Chicago).
6. Continuous: bank growth, teacher-reported fixes, standards re-check.
