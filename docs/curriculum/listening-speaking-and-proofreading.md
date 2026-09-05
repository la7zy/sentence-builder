# Listening & Speaking strand + Proofreading checkpoints

Prepared 2026-09-05 for the ATTP English Platform. Fills in two parts of the contract in
`00-platform-frame.md`: the Listening & Speaking strand (Part 1) and the three proofreading
checkpoints per band (Part 2). Bands are always named, never graded: **Foundations (A1),
Building (A2), Connecting (B1), Expanding (B2), Mastery (C1)**. Grammar section numbers
(S1-S13) are the 13 sections of `standards-mapping.md` Section C. Exercise type names are
exactly those in the frame's catalogue. Where a statement is my design judgement rather than
a sourced fact it is marked *(inference)*.

Variety taught: General American (the model voice). Where British and American pronunciation
or spelling both exist, the lesson names the variant and answer keys accept both when both
are correct (frame §6).

---

## PART 1 — Listening & Speaking strand

### 1.0 Design facts and what they force

| Fact | Consequence for the plan |
|---|---|
| Audio is pre-generated natural speech, one consistent model voice, played on the phone | Every listening/pronunciation item ships with an audio file made once from a script. One voice means dialogues are read by one voice with spoken speaker labels ("Ana:", "Sam:") and a half-second pause between turns; if the voice model supports stable speaking styles, use two fixed styles for A/B. Accent variety cannot come from the bank; it is offered as optional external listening (BBC, British Council, GMU Speech Accent Archive) and is never tested. Phone-call and noisy-room practice is made by post-processing the same audio (band-pass filter, low background noise) and is flagged as a pipeline feature *(inference)*. |
| The phone's built-in recognizer turns speech into text; the app marks words not recognised (word-level only, no accent scoring) | say-it / repeat-after / shadowing are scored as "words matched / words in target" after normalisation (case, punctuation, numerals vs number words, standard contractions both ways). A word is *marked*, never "wrong": the screen says "The word **three** wasn't recognised — listen and try again." Three attempts, then "move on"; nothing blocks progress. If the recognizer is unavailable, the item degrades to repeat-after with self-check and still counts for the practice badge. This matches the intelligibility principle (Levis 2005; Derwing & Munro 2005): the goal is being understood, not sounding native. |
| A small on-device language model can phrase tips (opt-in) | Tips are authored per lesson as a tip table keyed by (lesson, sound, word); the model only rephrases a chosen tip in plain words. It never scores, never invents advice (frame §8). |
| Adult learners, many first languages, elders and pre-literate beginners | Foundations lessons run listening-first: listen-choose and minimal-pair-choose before any dictation; say-it before typing; every screen read aloud; large play buttons; no timers. The L1 matrix (1.2) drives which minimal pairs a student sees first *(inference)*. |

Exercise-count legend used in all lesson tables: **MP** minimal-pair-choose · **LC** listen-choose · **LO** listen-order · **DI** dictation · **RA** repeat-after · **SI** say-it · **SH** shadowing · **RT** record-for-teacher. Every lesson has 16-20 items (frame §4: 8-20).

Audio speed targets (script wpm, model voice): Foundations 110-120 with pauses at phrase ends;
Building 125-135; Connecting 140-150; Expanding 150-165 natural; Mastery 160-180 with full
reductions. Fast/connected-speech lessons at each band run 10-15 wpm above the band target.

### 1.1 Strand map

| Band | Pronunciation lessons | Listening lessons | Auto-checked test (15 of 100, pass 80%) | Badge | Optional teacher task |
|---|---|---|---|---|---|
| Foundations | F-P1 … F-P8 (8) | F-L1 … F-L8 (8) | Certificate **Listening — Foundations** | **Speaking Practice — Foundations** | Speaking Task — Foundations (rubric 1.6) |
| Building | B-P1 … B-P8 (8) | B-L1 … B-L8 (8) | **Listening — Building** | **Speaking Practice — Building** | Speaking Task — Building |
| Connecting | C-P1 … C-P8 (8) | C-L1 … C-L8 (8) | **Listening — Connecting** | **Speaking Practice — Connecting** | Speaking Task — Connecting |
| Expanding | E-P1 … E-P8 (8) | E-L1 … E-L8 (8) | **Listening — Expanding** | **Speaking Practice — Expanding** | Speaking Task — Expanding |
| Mastery | M-P1 … M-P8 (8) | M-L1 … M-L8 (8) | **Listening — Mastery** | **Speaking Practice — Mastery** | Speaking Task — Mastery |

80 lessons in all (40 pronunciation, 40 listening), roughly 1,500 practice items plus five
100-item test banks (1.7). The strand runs in parallel with grammar: a student may open
Listening & Speaking at the band of their placement regardless of grammar progress.

### 1.2 First-language interference matrix

Columns: **Ar** Arabic · **Sp** Spanish · **Zh** Chinese (Mandarin/Cantonese) · **Ur/Hi** Urdu/Hindi ·
**Fa** Farsi · **Tr** Turkish · **Vi** Vietnamese · **So** Somali · **Uk/Ru** Ukrainian/Russian · **Fr** French.
**●** = typical, persistent difficulty; **○** = some speakers / milder; blank = rarely a problem.
Built from the language chapters of Swan & Smith, *Learner English* (CUP 2001), cross-checked
against recordings in the GMU Speech Accent Archive; a starting point for sequencing, not a
diagnosis of any individual *(inference where the two disagree)*.

| Feature (lesson) | Ar | Sp | Zh | Ur/Hi | Fa | Tr | Vi | So | Uk/Ru | Fr |
|---|---|---|---|---|---|---|---|---|---|---|
| /ɪ/ vs /iː/ ship–sheep (F-P1) | ○ | ● | ● | ○ | ● | ● | ● | ○ | ● | ● |
| /æ/ /e/ /ʌ/ bat–bet–but (F-P2) | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| /p/ vs /b/ pen–Ben (F-P3) | ● | | | ○ | | | ○ | ● | | |
| /f/–/v/–/w/ fan–van–wan (F-P3) | ● | ● (b/v) | ● (v/w) | ● (v/w) | ● (v/w) | ● (v/w) | ○ | ● (f/v) | ● (v/w) | |
| /θ/ /ð/ think–sink, they–day (F-P4) | ○ | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| /l/ vs /r/ vs /n/ light–right–night (F-P5) | | | ● | | | | ● | | | |
| /r/ quality (trill, tap, uvular) (F-P5) | ● | ● | ○ | ● | ● | ● | ○ | ● | ● | ● |
| Final consonants dropped/unreleased (F-P6) | ○ | ● | ● | ○ | ○ | ○ | ● | ● | | |
| -s and -ed endings, three sounds (F-P6, B-P2) | ● | ● | ● | ● | ● | ● | ● | ● | ○ | ● |
| Initial clusters sp-/st-/str- (B-P3) | ● | ● | ● | ● | ● | ● | ● | ● | | |
| Final clusters -sts/-nths/-ld (B-P4, E-P4) | ● | ● | ● | ○ | ○ | ● | ● | ● | | ○ |
| /ʃ/–/tʃ/–/dʒ/–/j/ ship–chip–jeep–yes (B-P5) | ● | ● | ○ | ○ | | | ● | ● | ● | ● |
| /h/ dropped or too strong (B-P6) | | ● | ○ | | | | | | ● | ● |
| /ŋ/ sing–sin, -ing (B-P6) | ● | ● | | ○ | ● | ● | | ● | ● | |
| Extra vowel inside/after words (B-P3/4) | ● | ● | ● | ● | ● | ● | ● | ● | | |
| Final voicing bag–back (C-P2) | | ○ | ● | | ○ | ● | ● | ○ | ● | |
| Word stress placement (F-P7, B-P7, C-P6) | ● | ● | ● | ● | ● | ● | ● | ● | ○ | ● |
| Sentence stress, weak forms, rhythm (F-P8, B-P8, C-P3) | ○ | ● | ● | ● | ● | ● | ● | ○ | ○ | ● |
| Intonation (flat, or tone carried over) (C-P5, E-P2) | ● | ○ | ● | ○ | ○ | ○ | ● | ○ | ● | ○ |
| Aspiration of p/t/k (pin heard as bin) (F-P3) | ○ | ● | | ● | ○ | ○ | ● | | ● | ● |

Also note: many Somali- and Arabic-speaking elders and some Vietnamese and Urdu speakers may
have limited literacy in any script; for them the listening-first path (1.0) is the default.

### 1.3 Pronunciation lessons

Each pronunciation lesson = explain (one sound or feature per screen, mouth diagram, audio) →
exercises → the lesson's say-it set feeds the band's practice badge. "Pairs" lists are the
minimum minimal-pair bank per lesson (each pair recorded as two audio files). L1 tags name the
groups that get the lesson's items first; every student still sees every lesson.

#### Foundations (A1)

| Lesson | Focus | Minimal pairs / examples (minimum bank) | L1 tags | Items |
|---|---|---|---|---|
| F-P1 | Long and short i: /ɪ/ vs /iː/ | ship/sheep, sit/seat, live/leave, fill/feel, chip/cheap, bin/bean, hit/heat, slip/sleep, list/least, his/he's | Sp Zh Fa Tr Vi Uk/Ru Fr | MP 8 · LC 2 · RA 5 · SI 3 · SH 1 = 19 |
| F-P2 | Three short vowels: /æ/ /e/ /ʌ/ | bat/bet/but, man/men, bad/bed, cat/cut, sad/said, pan/pen/pun, hat/hut, bag/beg/bug, ran/run, cap/cup | all | MP 8 · LC 2 · RA 5 · SI 3 · SH 1 = 19 |
| F-P3 | Lip sounds: /p/ /b/, /f/ /v/, /v/ /w/ | pen/Ben, pig/big, park/bark, pear/bear; fan/van, fine/vine, safe/save, leaf/leave; very/wary, vest/west, vine/wine, veal/wheel | Ar So Ur/Hi Fa Tr Uk/Ru Sp Zh | MP 8 · LC 2 · RA 5 · SI 3 · RT 1 = 19 |
| F-P4 | th sounds /θ/ /ð/ | think/sink, thin/tin, thank/tank, three/tree/free, bath/bass, mouth/mouse; then/den, they/day, breathe/breeze, there/dare, with/wit | all | MP 8 · LC 2 · RA 5 · SI 3 · SH 1 = 19 |
| F-P5 | /l/ /r/ /n/ and the American /r/ | light/right, lice/rice, collect/correct, glass/grass, lead/read, low/row, lock/rock; night/light, no/low; red/wed, road/load; car, work, first (r after vowels) | Zh Vi (l/r/n); Sp Ar Tr Fa Ur/Hi Uk/Ru Fr So (r quality) | MP 8 · LC 2 · RA 5 · SI 3 · SH 1 = 19 |
| F-P6 | Say the end of the word: final consonants and the three -s sounds | cat/cats, dog/dogs, bus/buses; /s/ books, cups, hats · /z/ days, cars, pens, goes · /ɪz/ watches, boxes, classes; plural, he/she/it verbs, possessive 's | Vi Zh Sp Ar So Tr | MP 6 · LC 4 · RA 5 · SI 3 · SH 1 = 19 |
| F-P7 | Syllables and word stress; -teen vs -ty | TAble, COFfee, hoTEL, comPUter, baNAna, toMORrow, PHOto, OFfice, aPARTment; thirTEEN/THIRty, fourTEEN/FORty … nineTEEN/NINEty; stress-shift pairs for MP: DEsert/desSERT, THIRty/thirTEEN | Fr Fa Tr Ur/Hi Sp Ar Zh Vi So | MP 6 (stress pairs) · LC 4 · RA 5 · SI 3 · SH 1 = 19 |
| F-P8 | Rhythm basics, contractions, can/can't; falling vs rising tune | I'm, it's, he's, don't, isn't, can't; I CAN go /kən/ vs I CAN'T go /kænt/; "Where do you live?" (falls) vs "Do you live here?" (rises) | all; esp. Zh Vi Uk/Ru Ar | MP 4 · LC 4 · RA 5 · SI 3 · SH 2 · RT 1 = 19 |

(In F-P7 the pairs are recorded as stressed forms only; the table shows the teaching point.)

#### Building (A2)

| Lesson | Focus | Minimal pairs / examples | L1 tags | Items |
|---|---|---|---|---|
| B-P1 | More vowels: /ʊ/ /uː/, /ɑ/ /ʌ/, /ɜr/, /eɪ/ /e/ | full/fool, pull/pool, look/Luke; cop/cup, not/nut, shot/shut; bird, work, first, learn, nurse; paper/pepper, late/let, wait/wet, taste/test | Sp Ar Vi Zh Tr So Fa Ur/Hi | MP 8 · LC 3 · RA 4 · SI 3 · SH 1 = 19 |
| B-P2 | The three -ed sounds /t/ /d/ /ɪd/ | walked, washed, stopped, laughed /t/ · played, lived, cleaned, called /d/ · wanted, needed, started, visited /ɪd/; no extra syllable in "worked"; contrasts: wait/waited, play/played | Sp Vi Zh Ar So Tr Fr Ur/Hi Fa | MP 6 · LC 3 · RA 4 · SI 4 · SH 1 · RT 1 = 19 |
| B-P3 | Clusters at the start: sp- st- sk- sl- str- spr- | school, street, Spain, sport, spring, small, snow, sleep, stop, study; no "e-" before s: "school" not "eschool"; "street" not "istreet" | Sp Ar Fa Tr Ur/Hi Vi So Zh | MP 6 · LC 3 · RA 4 · SI 4 · SH 1 · RT 1 = 19 |
| B-P4 | Clusters at the end: -st -sk -nd -ld -lp -ts -ks | first, last, ask, desk, hand, friend, cold, world, help, cats, books, tests, months, asked, helped | Vi Zh Ar So Sp Tr Fa | MP 6 · LC 3 · RA 4 · SI 4 · SH 1 · RT 1 = 19 |
| B-P5 | /ʃ/ /tʃ/ /dʒ/ /j/ | ship/chip, wash/watch, share/chair, shoes/choose; cheap/jeep, choke/joke, chin/gin; yes/Jess, year/jeer, yellow/Jell-O, yet/jet; sheep/cheap/jeep | Sp Fr Vi Ar So Uk/Ru Zh | MP 8 · LC 3 · RA 4 · SI 3 · SH 1 = 19 |
| B-P6 | /h/, /ŋ/ and silent letters | hair/air, hat/at, hill/ill, heart/art, high/eye; sing/sin, thing/thin, rang/ran, wing/win; -ing without a /g/; silent: knife, know, walk, half, comb, island, Wednesday, listen | Fr Sp Uk/Ru (h); Fa Tr Sp Ar So Uk/Ru (ŋ); all (silent letters) | MP 6 · LC 4 · RA 4 · SI 3 · SH 1 · RT 1 = 19 |
| B-P7 | Word-stress patterns | REcord/reCORD, PREsent/preSENT, OBject/obJECT; compounds: BUS stop, CREDit card, POST office; suffix rules: naTION, deCIsion, ecoNOMic, aBILity, PHOtograph; -teen/-ty review | Fr Fa Tr Ur/Hi Sp Ar Zh Vi So | MP 6 · LC 4 · RA 4 · SI 3 · SH 1 · RT 1 = 19 |
| B-P8 | Linking and weak forms 1 | an‿apple, turn‿off, pick‿it‿up, come‿in; weak a, the, to, and, of, for, can, was, were, at, from ("a cup‿of tea", "bread‿and butter"); I'll, I'd, I've, she's, we're, they'll | Sp Fr Zh Vi Ur/Hi Tr Fa (syllable-timed L1s); all | MP 4 · LC 4 · DI 2 · RA 4 · SI 3 · SH 2 = 19 |

#### Connecting (B1)

| Lesson | Focus | Minimal pairs / examples | L1 tags | Items |
|---|---|---|---|---|
| C-P1 | Diphthongs and back vowels | boat/bought/bot, coal/call, low/law, coat/cot; buy/boy, tie/toy, pies/poise; how/hoe, town/tone; note the American cot–caught merger (many speakers say both the same: accept both) | Sp Ar Vi Zh Tr So Uk/Ru Fa | MP 6 · LC 4 · DI 2 · RA 3 · SI 3 · SH 1 · RT 1 = 20 |
| C-P2 | Voicing at the end + vowel length | bag/back, cab/cap, had/hat, ride/write, eyes/ice, price/prize, leaf/leave, safe/save, bus/buzz; long vowel before a voiced end (bead > beat) | Uk/Ru Tr Zh Vi So Fa Sp | MP 8 · LC 3 · DI 2 · RA 3 · SI 3 · SH 1 = 20 |
| C-P3 | Sentence stress and rhythm; schwa | content vs function words: "I WANT to GO to the BANK"; /ə/ in about, banana, sofa, support; thought groups with pauses | all; esp. Sp Fr Zh Vi Ur/Hi Tr Fa | MP 4 (stress) · LC 4 · DI 2 · RA 3 · SI 4 · SH 2 · RT 1 = 20 |
| C-P4 | Connected speech 1: linking with /j/ /w/, assimilation, elision | go‿(w)on, I‿(j)agree, do‿(w)it, the‿(j)end; "ten boys" → tem boys, "in Paris" → im Paris; nex(t) day, mus(t) be; recognise gonna/wanna/gotta (do not require them in speech) | all | MP 4 · LC 5 · DI 3 · RA 3 · SI 3 · SH 2 = 20 |
| C-P5 | Intonation for meaning | statements and wh-questions fall; yes/no questions rise; lists (rise, rise, fall); tag questions (fall = checking, rise = asking); polite vs abrupt requests | Zh Vi Uk/Ru Ar; all | MP 4 (tune pairs) · LC 5 · DI 1 · RA 3 · SI 4 · SH 2 · RT 1 = 20 |
| C-P6 | Word stress in longer words; stress shift | PHOtograph / phoTOgraphy / photoGRAphic; ECOnomy / ecoNOMic; -ic, -tion/-sion, -ity, -ical, -ate, -ize, -ee (emploYEE), prefixes unstressed (unHAPpy, reWRITE) | Fr Fa Tr Ur/Hi Sp Ar Zh Vi So | MP 6 · LC 4 · DI 2 · RA 3 · SI 3 · SH 1 · RT 1 = 20 |
| C-P7 | Consonants mid-word: flap /t/, /s/ /z/, /ʒ/ | water, better, city, little (flap); ice/eyes, use (noun)/use (verb), close (adj)/close (verb), advice/advise; usual, measure, decision, garage | Sp Zh Vi Ar Ur/Hi So | MP 8 · LC 3 · DI 2 · RA 3 · SI 3 · SH 1 = 20 |
| C-P8 | Contractions and negatives at speed | isn't/aren't/wasn't/weren't, won't/wouldn't, couldn't/shouldn't, 'd/'ll/'ve, "didn't you" /dɪdn̩tʃu/, "don't you", "would you"; can vs can't at speed (review) | all | MP 6 · LC 4 · DI 3 · RA 2 · SI 3 · SH 2 = 20 |

#### Expanding (B2)

| Lesson | Focus | Examples | L1 tags | Items |
|---|---|---|---|---|
| E-P1 | Contrastive stress and focus | "I said FIFteen, not FIFty." "It's not MY problem, it's YOURS." "I didn't say he STOLE it." (move the stress, change the meaning) | all | MP 4 · LC 4 · DI 2 · RA 2 · SI 5 · SH 2 = 19 |
| E-P2 | Intonation for attitude and discourse | interest vs boredom, doubt, politeness; non-final rise before a comma; indirect questions ("Could you tell me where the office is?" falls); "Really?" as question vs comment | Zh Vi Uk/Ru Ar; all | MP 4 · LC 5 · DI 1 · RA 2 · SI 4 · SH 2 · RT 1 = 19 |
| E-P3 | Thought groups, pausing, pacing for longer speech | chunking sentences with relative clauses and appositives (links to S9 at this band); pause = comma/period; reading a paragraph aloud at a steady pace | all | MP 2 · LC 4 · DI 2 · RA 2 · SI 5 · SH 3 · RT 1 = 19 |
| E-P4 | Hard clusters and endings in real words | months, clothes, sixths, asked, texts, strengths, worlds, crisps, scripts; -s and -ed on cluster-final words (helps, risked, lasts) | Vi Zh Ar Sp So Tr Fa Ur/Hi | MP 6 · LC 3 · DI 2 · RA 2 · SI 4 · SH 2 = 19 |
| E-P5 | Vowel reduction and secondary stress in work/academic words | analysis/analyze, economy/economic, politics/political, photograph/photographer; ˌinforˈmation, ˌuniˈversity; keeping schwa in unstressed syllables | all | MP 4 · LC 4 · DI 2 · RA 2 · SI 4 · SH 2 · RT 1 = 19 |
| E-P6 | Fast speech reductions (recognise; use in casual speech only) | "What do you" → whaddaya; "going to/want to/have to" → gonna/wanna/hafta; him/her/them → 'im/'er/'em; "Did you" → didja; dropped /h/ in weak he/his/her | all | MP 2 · LC 5 · DI 4 · RA 2 · SI 3 · SH 3 = 19 |
| E-P7 | Spelling to sound: homophones, homographs, -ough | through/threw, weather/whether, right/write; live/live, read/read, lead/lead, tear/tear; though, through, tough, cough, thought, bough | all | MP 6 · LC 4 · DI 2 · RA 2 · SI 3 · SH 2 = 19 |
| E-P8 | Stress in phrasal verbs, compounds and long noun phrases | pick UP the phone / PICK it up; LOOK it up; a GREENhouse vs a green HOUSE; well-KNOWN; "the FIRST-floor OFfice"; stress in numbers with units (two HUNdred DOLlars) | Ur/Hi Ar Sp Zh Vi; all | MP 6 · LC 4 · DI 2 · RA 2 · SI 3 · SH 2 = 19 |

#### Mastery (C1)

| Lesson | Focus | Examples | L1 tags | Items |
|---|---|---|---|---|
| M-P1 | Clarity and register: full forms vs reductions by audience | presenting to a group (slower, fuller forms, more pauses) vs chatting; when to spell a name or restate; recording and reviewing your own speech | all | LC 4 · DI 3 · RA 2 · SI 5 · SH 3 · RT 1 = 18 |
| M-P2 | Intonation for nuance: irony, hedging, challenge | "Oh, GREAT." (sincere vs sarcastic); hedged falls-rises ("I suppose"); tags that challenge; emphasis to correct politely | Zh Vi Uk/Ru Ar; all | MP 4 · LC 5 · DI 2 · RA 2 · SI 4 · SH 2 · RT 1 = 20 |
| M-P3 | Advanced connected speech | assimilation of /t d n/ before /p b m/ (that man → thap man), "don't you/would you" → /tʃ dʒ/, glottal /t/ (button), syllabic consonants (bottle, cotton, sudden), catenation across phrases | all | MP 4 · LC 4 · DI 4 · RA 2 · SI 3 · SH 3 = 20 |
| M-P4 | Rhythm in long, complex sentences | parenthetical tune for appositives and non-defining relatives; enumeration; reading a 120-word script aloud with marked thought groups | all | MP 2 · LC 4 · DI 3 · RA 2 · SI 4 · SH 3 · RT 1 = 19 |
| M-P5 | Stress in technical and academic vocabulary | hyPOthesis/hypoTHEtical, aNALysis/aNALyses (plural), SEParate (adj)/SEpaRATE (verb), ESTimate (n)/EStiMATE (v), Greek/Latin roots; acronyms (NASA vs F.B.I.) | all | MP 6 · LC 4 · DI 2 · RA 2 · SI 3 · SH 2 = 19 |
| M-P6 | Self-monitoring and repair | reading IPA in Oxford/Cambridge dictionaries; asking for and giving clarification; spelling out names, numbers, addresses; restating | all | LC 4 · DI 3 · RA 2 · SI 5 · SH 2 · RT 2 = 18 |
| M-P7 | Varieties of English (recognition only) | American vs British: water, can't, schedule, tomato, r after vowels, flap vs /t/; a note on Indian, Australian and Caribbean features heard at work; optional external listening links | all | LC 8 · DI 3 · RA 2 · SI 3 · SH 2 = 18 |
| M-P8 | Speaking under pressure | interviews, presentations, phone calls with bad lines: keeping pace, chunking, stress on key words, controlled restarts | all | LC 3 · DI 2 · RA 2 · SI 6 · SH 3 · RT 2 = 18 |

### 1.4 Listening lessons

Each listening lesson = one skill, 2-4 short recordings (scripts written for the band's
vocabulary range, one voice, speaker labels for dialogues), explain screen with the listening
strategy (predict → listen for gist → listen for detail), then exercises. Dictation items
mark *focus words* (numbers, endings, weak forms) that must match exactly; other words allow
one letter of difference.

#### Foundations (A1)

| Lesson | Skill | Audio content (one voice) | Items |
|---|---|---|---|
| F-L1 | Numbers 0-100, prices, phone numbers | "It's $4.50." "My number is 555-0142." thirteen vs thirty in prices and ages | LC 8 · LO 2 · DI 4 · RA 3 · SI 1 = 18 |
| F-L2 | Spelling names and addresses | letter names; confusable letters (b/v/p/d, e/i, a/e, g/j, m/n); "double l"; email addresses read aloud | LC 8 · LO 1 · DI 5 · RA 3 · SI 1 = 18 |
| F-L3 | Days, months, dates, times | "Monday the third", "June 21st", "half past two", "3:15", "a.m./p.m."; appointment cards | LC 8 · LO 2 · DI 4 · RA 3 · SI 1 = 18 |
| F-L4 | Following simple instructions | app and classroom instructions ("Tap the blue button"), directions ("Turn left at the bank"), forms ("Write your last name") | LC 8 · LO 3 · DI 3 · RA 3 · SI 1 = 18 |
| F-L5 | Short dialogues: greetings, shopping | introductions; store dialogue (size, colour, price, "Do you have this in medium?") | LC 8 · LO 2 · DI 4 · RA 3 · SI 1 = 18 |
| F-L6 | Short dialogues: health and work | pharmacy ("Take one tablet twice a day, with food"); shift talk ("Can you work on Saturday?") | LC 8 · LO 2 · DI 4 · RA 3 · SI 1 = 18 |
| F-L7 | Transport and simple announcements | bus and train numbers, platform, "next stop", "The store closes in ten minutes" | LC 8 · LO 2 · DI 4 · RA 3 · SI 1 = 18 |
| F-L8 | A short talk: listen for key facts | 6-8 sentence description of a person, a family or a place; note name, job, number, place | LC 8 · LO 2 · DI 4 · RA 2 · SI 1 · RT 1 = 18 |

#### Building (A2)

| Lesson | Skill | Audio content | Items |
|---|---|---|---|
| B-L1 | Numbers in context | large numbers, decimals, fractions, percentages, years, money, measurements ("two and a half kilos", "1,250 dollars", "in 1998") | LC 8 · LO 2 · DI 5 · RA 2 · SI 2 = 19 |
| B-L2 | Instructions and processes | recipes, machine and app steps, safety instructions with first/then/after that/finally | LC 8 · LO 3 · DI 4 · RA 2 · SI 2 = 19 |
| B-L3 | Work dialogues and voicemail | schedules, requests, reporting a problem, a call to a workplace, leaving a voicemail with a callback number | LC 8 · LO 2 · DI 4 · RA 2 · SI 2 · SH 1 = 19 |
| B-L4 | Health dialogues | making an appointment, describing symptoms, medicine labels, calling 911 (what the operator asks) | LC 8 · LO 2 · DI 4 · RA 2 · SI 2 · SH 1 = 19 |
| B-L5 | Shopping and services | returns and receipts, comparing prices, a utility bill explained, phone menus ("Press 1 for…") | LC 8 · LO 2 · DI 4 · RA 2 · SI 2 · SH 1 = 19 |
| B-L6 | Transport and travel | directions with landmarks, delays, airport and train announcements, a ride-share pickup | LC 8 · LO 2 · DI 4 · RA 2 · SI 2 · SH 1 = 19 |
| B-L7 | Fast/connected speech 1 | can/can't, wanna/gonna, weak "to/for/and" in dialogue; gist first, then detail | LC 8 · LO 2 · DI 5 · RA 2 · SI 1 · SH 1 = 19 |
| B-L8 | Short talks and stories (1-2 min) | a past event told in order; weather and traffic reports; note who/what/when/where | LC 8 · LO 2 · DI 4 · RA 1 · SI 2 · SH 1 · RT 1 = 19 |

#### Connecting (B1)

| Lesson | Skill | Audio content | Items |
|---|---|---|---|
| C-L1 | Longer conversations (2-3 min) | job interview, team meeting, appointment with follow-up; who agrees with whom; attitude | LC 8 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 19 |
| C-L2 | Announcements and recorded messages | airport/train changes, public-service messages, voicemail with dates, times and reference numbers | LC 8 · LO 2 · DI 5 · SI 2 · SH 2 = 19 |
| C-L3 | Explanations and procedures | how a device works; workplace procedure or safety briefing; steps with conditions ("If the light is red, …") | LC 8 · LO 3 · DI 4 · SI 2 · SH 2 = 19 |
| C-L4 | Short talks (2-3 min) with note-taking | general-knowledge talks (history, science, health) sharing topics with the proofreading bank; main idea + details; abbreviations and symbols in notes | LC 8 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 19 |
| C-L5 | News-style reports | 3-4 short items, weather, traffic, community notice; fact vs opinion | LC 8 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 19 |
| C-L6 | Fast/connected speech 2 | assimilation, elision, gonna/wanna/gotta in dialogue; reconstruct the full form | LC 8 · LO 2 · DI 5 · SI 2 · SH 2 = 19 |
| C-L7 | Telephone listening | automated menus, call-centre dialogue, poor-line audio (post-processed), confirming details back | LC 8 · LO 2 · DI 4 · SI 3 · SH 1 · RT 1 = 19 |
| C-L8 | Listen and retell | 2-min talk → spoken 3-sentence summary (record-for-teacher) and dictation of the key sentences | LC 7 · LO 2 · DI 4 · SI 2 · SH 2 · RT 2 = 19 |

#### Expanding (B2)

| Lesson | Skill | Audio content | Items |
|---|---|---|---|
| E-L1 | Talks and lectures (4-5 min) | signposting ("first", "moving on", "to sum up"); Cornell-style notes; main idea, details, examples | LC 9 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 20 |
| E-L2 | Discussion and debate | two speakers disagree; positions, reasons, concessions; tone | LC 9 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 20 |
| E-L3 | Workplace briefings and meetings | agenda, decisions, actions with owners and deadlines, feedback with conditions | LC 9 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 20 |
| E-L4 | Health and public information | a clinic talk, medication warnings, an insurance explanation; numbers with conditions | LC 9 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 20 |
| E-L5 | Interviews and podcast-style talk | implied meaning, hedging, a speaker's stance | LC 9 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 20 |
| E-L6 | Fast/connected speech 3 | full-speed monologue; 'im/'er/'em, dropped auxiliaries, emphasis and sarcasm cues | LC 9 · LO 2 · DI 5 · SI 2 · SH 2 = 20 |
| E-L7 | Numbers, data and trends | statistics in talks, ranges, comparisons ("rose by a third to just under 40%") | LC 9 · LO 2 · DI 5 · SI 2 · SH 2 = 20 |
| E-L8 | Extended dictation and shadowing | 40-60-word dictations, 60-90-second shadowing, recorded retelling | LC 8 · LO 2 · DI 5 · SI 1 · SH 3 · RT 1 = 20 |

#### Mastery (C1)

| Lesson | Skill | Audio content | Items |
|---|---|---|---|
| M-L1 | Long talks (6-8 min) on complex subjects | structure, argument, evidence; detailed notes; the talk topics mirror Mastery proofreading topics | LC 9 · LO 2 · DI 4 · SI 1 · SH 2 · RT 2 = 20 |
| M-L2 | Nuance and implication | idiom, understatement, irony, hedging; what the speaker avoids saying | LC 9 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 20 |
| M-L3 | Complex procedures and plain-language regulation | workplace training, tenancy and consumer rules, financial disclosures | LC 9 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 20 |
| M-L4 | Multi-speaker discussion (one voice, labelled) | a three-person panel; tracking who said what; agreement shifts | LC 9 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 20 |
| M-L5 | News analysis with statistics | fact, opinion, speculation; evaluating the source | LC 9 · LO 2 · DI 4 · SI 2 · SH 2 · RT 1 = 20 |
| M-L6 | Fast/connected speech 4 | natural-speed monologue with every reduction; transcription accuracy | LC 8 · LO 2 · DI 6 · SI 1 · SH 3 = 20 |
| M-L7 | Academic and professional listening | summarise a lecture, evaluate its argument (record-for-teacher) | LC 8 · LO 2 · DI 4 · SI 2 · SH 2 · RT 2 = 20 |
| M-L8 | Integrated tasks | listen → notes → 2-3-minute spoken response; simulated interview; phone negotiation | LC 7 · LO 2 · DI 4 · SI 3 · SH 2 · RT 2 = 20 |

### 1.5 Speaking items: the word-level protocol

1. The target text is shown and played (model voice). The student records. The phone's
   recognizer returns text; the app normalises both strings (case, punctuation, numerals ↔
   number words, standard contractions accepted both ways, American/British spellings) and
   aligns them word by word.
2. Words not matched are highlighted; the screen never says "wrong pronunciation". The tip
   shown comes from the lesson's tip table (e.g. "three — put the tip of your tongue between
   your teeth and blow"); the on-device model may rephrase it, opt-in only.
3. Up to three attempts; the best attempt is kept. Item counts as *done* after any attempt.
   shadowing items are scored on the last 60% of the passage only (the first part is the
   student catching the rhythm) *(inference)*.
4. No timer, no accent score, no comparison with other students. Recognizer confidence values
   are never shown. If the recognizer fails twice in a row, the app offers the self-check
   path (listen, record, compare by ear) and marks the item "self-checked".
5. record-for-teacher clips are capped at 3 minutes, stored on the relay, and appear in the
   teacher dashboard with the band rubric (1.6) pre-loaded.

### 1.6 Tests, badge and teacher task per band

**Listening test (auto-checked).** 15 items drawn at random from the band's 100-item bank,
different every attempt; pass 80% (12/15); certificate as named in 1.1 (verification code as
in frame §4). Only auto-checkable types appear in tests.

| Band | LC | LO | DI | MP | Max audio per item | Dictation length (focus words exact) | Remediation tag |
|---|---|---|---|---|---|---|---|
| Foundations | 6 | 2 | 2 | 5 | 20 s | 4-6 words | every item → one F-P/F-L lesson |
| Building | 7 | 2 | 3 | 3 | 40 s | 6-9 words | one B-P/B-L lesson |
| Connecting | 8 | 2 | 3 | 2 | 75 s | 8-12 words | one C-P/C-L lesson |
| Expanding | 9 | 2 | 3 | 1 | 2.5 min | 12-16 words | one E-P/E-L lesson |
| Mastery | 10 | 2 | 3 | 0 | 4 min | 16-20 words | one M-P/M-L lesson |

Bank rules: 100 items per band (≥10 per listening lesson, remainder from pronunciation lessons
as MP/LC items); each item tagged with its lesson; audio generated once and stored with the
item; the frame's quality bar (§6: single correct answer, distractors provably wrong, two
review passes, teacher spot-check, report button) applies. Failed test → the missed lessons →
fresh exercises → a new draw of 15.

**Speaking practice badge (not a certificate).** Awarded automatically when (a) every say-it,
repeat-after and shadowing item in the band's 16 lessons has been attempted and (b) the
student's best attempts match at least 70% of target words across the band's say-it items.
Unlimited retries; the badge can never be lost. Shown on the profile as
"Speaking Practice — <Band>"; if a teacher has graded the optional task, the badge carries the
line "Teacher-graded: N/16" (no separate certificate; frame §3).

**Optional teacher-graded speaking task.** One recorded task per band (record-for-teacher),
graded on four criteria, 0-4 each (16 max). "At band" = 12/16 with no criterion below 2.
Criteria and score anchors are the same at every band; the descriptors below define score 3
("at band"). 4 = clearly beyond the band descriptor; 2 = approaching (frequent lapses but the
task is completed); 1 = well below (listener effort high, task partly done); 0 = no usable
response. Criteria paraphrase the CEFR Companion Volume 2020 phonological-control scales
(overall control, sound articulation, prosody) and the Cambridge English speaking scales
(pronunciation, discourse management, grammatical and lexical resource).

| Band · task (time) | 1 Intelligibility: sounds and word stress | 2 Rhythm and intonation | 3 Fluency and task completion | 4 Language for the band |
|---|---|---|---|---|
| Foundations · introduce yourself and describe your usual day (45-60 s, notes allowed) | Learnt words and short phrases are understood by a listener used to learners; the band's target sounds (F-P1-P6) are attempted; word stress right on familiar words | Some phrases run together; questions and statements have a recognisable tune | Task done with pauses and restarts; short memorised chunks | Present-tense sentences with subject and verb; basic vocabulary of the topic |
| Building · tell what happened last weekend or on a trip; then one short opinion (60-90 s) | Generally intelligible; systematic L1-influenced substitutions do not block meaning; -s/-ed endings mostly present | Word stress mostly right on common words; some weak forms; occasional list/yes-no tunes | Keeps going with simple linkers (and/but/because); task complete | Past simple mostly correct; some compound sentences; everyday vocabulary |
| Connecting · explain how something works or give your view on a familiar issue with reasons (90-120 s) | Clearly intelligible despite accent; occasional mispronunciations do not need repair | Sentence stress carries meaning most of the time; thought groups audible; falls/rises mostly appropriate | Sustained speech with some hesitation; clear beginning-middle-end; asks for clarification if needed | Complex sentences; tenses generally consistent; connectors (however, for example) |
| Expanding · present two sides of an issue and recommend one (2-3 min, may use notes) | Sounds articulated clearly; accent has little effect on intelligibility | Uses contrastive stress and intonation to organise and emphasise; natural chunking | Fluent, only occasional searching for words; argument develops systematically | Range of structures incl. passives, conditionals, relative clauses; precise vocabulary; hedging |
| Mastery · summarise a 6-8-min talk you listened to, evaluate it, and answer two follow-up prompts (3-4 min) | Full control; any residual accent never affects meaning | Varies stress and intonation to convey finer shades of meaning; parenthetical tune for asides | Smooth, well-structured, adjusts register for the audience; handles the follow-ups without preparation | Wide, accurate range: nominalisation, inversion, past modals; idiom and collocation used appropriately |

Teacher time per task: 5-8 minutes. The dashboard shows the rubric, the transcript from the
recognizer (marked "machine transcript, not for grading"), and the student's word-match history.

### 1.7 Bank sizes (Part 1)

| Item pool | Foundations | Building | Connecting | Expanding | Mastery | Total |
|---|---|---|---|---|---|---|
| Pronunciation lesson items (8 lessons) | 152 | 152 | 160 | 152 | 150 | 766 |
| Listening lesson items (8 lessons) | 144 | 152 | 152 | 160 | 160 | 768 |
| of which say-it / repeat-after / shadowing | ~88 | ~90 | ~96 | ~96 | ~104 | ~474 |
| Listening test bank | 100 | 100 | 100 | 100 | 100 | 500 |
| Minimal-pair audio pairs (distinct) | ~80 | ~70 | ~55 | ~40 | ~25 | ~270 |

Phase-4 build order (frame §11): Foundations pronunciation + listening + test bank first
(the largest audience and the elders' path), then band by band.

### 1.8 Sources for Part 1

1. BBC Learning English, *Pronunciation* (The Sounds of English videos; Tim's Pronunciation
   Workshop on linking, assimilation, weak forms):
   https://www.bbc.co.uk/learningenglish/english/features/pronunciation — the site blocks
   automated fetch; the page and its contents were confirmed from BBC Learning English's
   published description (https://en.wikipedia.org/wiki/BBC_Learning_English).
2. Rachel's English, *ED endings* (three sounds) https://rachelsenglish.com/ed-endings-2020-1-3/
   and https://rachelsenglish.com/get-it-right-how-to-nail-ed-endingsspeaking-english/ ;
   site index https://rachelsenglish.com/ (American reductions, linking, stress).
3. British Council LearnEnglish, *Listening* A1-C1 (situations per level used to calibrate
   1.4): https://learnenglish.britishcouncil.org/skills/listening ; TeachingEnglish,
   *Minimal pair*: https://www.teachingenglish.org.uk/professional-development/teachers/teaching-knowledge-database/d-h/minimal-pair ;
   phonemic chart: https://www.teachingenglish.org.uk/teaching-resources/teaching-secondary/teaching-tools/phonemic-chart-english-teachers
4. Cambridge University Press: Baker, *Ship or Sheep?* (minimal-pair course, 3rd ed. 2006)
   https://assets.cambridge.org/97805216/06714/frontmatter/9780521606714_frontmatter.pdf ;
   Swan & Smith (eds.), *Learner English: A Teacher's Guide to Interference and Other
   Problems* (2nd ed. 2001) https://assets.cambridge.org/97805217/79395/frontmatter/9780521779395_frontmatter.pdf
   (the L1 matrix in 1.2 rests on its language chapters).
5. Cambridge English, *Assessing Speaking Performance*: B1 https://www.cambridgeenglish.org/Images/563276-b1-preliminary-assessing-speaking.pdf ;
   B2 https://www.cambridgeenglish.org/images/168619-assessing-speaking-performance-at-level-b2.pdf ;
   C1 https://www.cambridgeenglish.org/images/168620-assessing-speaking-performance-at-level-c1.pdf
   (C1 URL taken from search index, not re-fetched); teacher guide C1
   https://www.cambridgeenglish.org/Images/735851-teacher-guide-for-speaking-c1-advanced.pdf
6. Council of Europe, *CEFR Companion Volume* (2020), phonological control scales:
   https://rm.coe.int/common-european-framework-of-reference-for-languages-learning-teaching/16809ea0d4
   (PDF returns 403 to automated fetch; URL confirmed via the CoE index
   https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-companion-volume-and-its-language-versions);
   background to the new scale: https://rm.coe.int/the-new-scale-for-phonological-control-piccardo-/1680788b29
7. Oxford Learner's Dictionaries, pronunciation guide (IPA symbols; American English guide
   used for the model voice): https://www.oxfordlearnersdictionaries.com/about/english/pronunciation_english ;
   https://www.oxfordlearnersdictionaries.com/about/american_english/pronunciation_american_english
8. Purdue OWL, *English as a Second Language* (multilingual students and instructors):
   https://owl.purdue.edu/owl/multilingual/index.html ;
   https://owl.purdue.edu/owl/multilingual/multilingual_instructors_tutors/esl_teacher_resources/index.html
9. University of Iowa, *Sounds of Speech* (animated articulation of every American English
   sound): https://soundsofspeech.uiowa.edu/english/english.html ; Iowa Speaking Center
   pronunciation resources: https://speakingcenter.uiowa.edu/pronunciation-resources
10. George Mason University, *Speech Accent Archive* (same paragraph read by ~3,000 speakers;
    used to check the L1 matrix and for optional accent listening): https://accent.gmu.edu/
11. Research on intelligibility and L1 influence: Derwing & Munro (2005), "Second language
    accent and pronunciation teaching: a research-based approach", *TESOL Quarterly* 39(3)
    https://doi.org/10.2307/3588486 ; Levis (2005), "Changing contexts and shifting paradigms
    in pronunciation teaching", *TESOL Quarterly* 39(3) https://doi.org/10.2307/3588485
    (ERIC: https://eric.ed.gov/?id=EJ752932) ; Levis (2020), "Revisiting the intelligibility
    and nativeness principles" https://www.jbe-platform.com/content/journals/10.1075/jslp.20050.lev ;
    Jenkins (2000) Lingua Franca Core, summarised with critique at
    https://www.redalyc.org/journal/4994/499462160006/html/ (core = consonants except th,
    clusters, vowel length, nuclear stress; used to rank which lessons come first).

---

## PART 2 — Proofreading checkpoints

### 2.1 How a checkpoint runs

- **When.** CP1 after grammar sections 1-4, CP2 after 5-8, CP3 after 9-12, at every band
  (frame §7). A checkpoint opens when the section tests before it are passed.
- **What.** 2-3 passages (2.3) drawn at random from the band's checkpoint pool; each passage
  is a `proofread-passage` item: the student taps a word (or a space between words for a
  missing item, or a punctuation mark) and types the correction. Whole-sentence answers are
  accepted and matched by the rules engine plus the item's variant list.
- **Scoring.** An error counts only when it is *found and correctly fixed*. Pass = 80% of the
  checkpoint's planted errors, rounded up (ceil). False alarms: the app replies "This is
  correct — <one-line why>" and does not deduct; more than 3 false alarms in one passage
  count as one miss (stops carpet-tapping) *(inference)*. No timer.
- **Feedback.** After submitting a passage the student sees every planted error, the fix, the
  rule name and the lesson link. The clean passage is then read aloud by the model voice
  (doubles as listening practice).
- **Miss → lesson → new passage.** Each missed error sends the student to the lesson that
  teaches the rule (explain + fresh exercises). The retry uses a **different clean text** from
  the same pool, with at least one planted error of each missed type. Seed variants (same
  clean text, different error set; 2.7) are never used for a retry within 30 days.
- **Record.** Checkpoint pass is recorded on the dashboard ("CP2 — Connecting: 21/24, passed
  2nd attempt"). No certificate; the pass unlocks the next grammar sections.
- **Cumulative rule.** Allowed error types = those taught in the listed sections at this band
  *plus* the lower-band visits of the same sections (the spiral makes them prerequisites);
  at least 60% of planted errors come from the current band's visit *(inference)*.
- **Never planted.** Facts, names, dates; contested usages where authorities disagree
  (singular *they*, *less/fewer*, *feel bad/badly*, *comprised of*, *different than/from*,
  optional Oxford comma, *I wish I was*); anything with two defensible fixes unless every
  defensible fix is in the variant list.

### 2.2 Allowed error types per checkpoint per band

Each line: rule (section) — planted → fix. CP2 = CP1 list + its additions; CP3 = CP2 + its
additions. Rules named here map one-to-one to lessons in the grammar strand plans.

**Foundations (A1)**
- CP1 · S1 missing subject or verb ("Paris the capital." → *is*); wrong or missing end mark; basic word order (*I like very much coffee* → *I like coffee very much*). S2 plural -s missing/extra; irregular plurals (*childs*); *a/an*; missing article before a singular count noun; *a* + plural. S3 subject/object/possessive confusion (*me go*, *he book* → *his*); *my/mine*. S4 *am/is/are*, *was/were*; present-simple 3rd-person -s; present continuous form (*is work* → *is working*); negative *don't/doesn't*; imperative form.
- CP2 adds · S5 agreement in simple sentences (*they is*, *she have*). S6 *can/can't* + base (*can to go*, *can goes*); *I'd like* + noun/*to*. S7 adjective before noun (*a car red*); no plural on adjectives (*reds cars*); *very* + adjective; frequency adverb position (*I go always*); *this/these*. S8 *in/on/at* for place and time (*in Monday*, *at the morning*).
- CP3 adds · S9 *and/but/or/so* choice. S10 question word order (*Where you live?*, *Do you can?*); negatives (*I no have*, *he don't*). S11 capital for sentence start, *I*, names, days/months; apostrophes in contractions (*dont*); end marks. S12 sequence words out of order or missing (*Then … First …*).

**Building (A2)**
- CP1 · S1 fragments and run-ons (two sentences with no mark or joiner). S2 count/uncount (*an information*, *furnitures*, *much books*); irregular plurals; possessive *'s/s'*. S3 reflexives (*hisself*, *I hurt me*); indefinite pronouns; noun-pronoun agreement (*The students … he*). S4 past simple regular/irregular (*goed*, *buyed*); *will/going to* forms (*will to go*, *going to went*); past continuous form; present perfect form (*have go* → *have gone*) with *ever/never/just*.
- CP2 adds · S5 compound subjects (*Tom and Ana is*); *there is/are* with plurals. S6 *have to/should/could* + base (*should to go*); zero and first conditional (*If it will rain, …*). S7 comparatives/superlatives (*more bigger*, *the most tall*, *gooder*, *than/then*); *-ly* adverbs of manner (*drive careful*); double negatives (*don't have nothing*). S8 movement and phrase prepositions (*go to home*, *arrive to*, *in the night*); *on the weekend/at the weekend* both accepted.
- CP3 adds · S9 *because/when/if* clauses (word order; *because of* + clause). S10 past wh-questions (*Where did you went?*, *Where you went?*); question tags (*You like tea, isn't it?*). S11 commas in series, dates, addresses, letters; quotation marks in dialogue; possessive apostrophes (*the dogs bowl*, *it's* for *its*); capitals in titles, holidays, place names. S12 *first/next/then/finally*; pronoun reference (*it/they* number); *this/that/these/those*.

**Connecting (B1)**
- CP1 · S1 subordinate-clause fragments (*Because it was late.*); comma splices; run-ons. S2 relative pronoun choice (*the man which*); missing relative pronoun when required (*the woman lives next door is …*); collective nouns (*the team*: singular verb taught, plural named and accepted where context allows). S3 pronouns in compound objects (*between you and I*, *gave it to John and I*); reflexive misuse (*Myself and John went*); antecedent agreement with clear number. S4 tense consistency across a paragraph; present perfect with a finished time (*have seen him yesterday*); past perfect after *by the time*; reported speech shifts (*She said she is tired yesterday*).
- CP2 adds · S5 agreement with intervening phrases (*The box of apples are*); *a lot of / most of* subjects. S6 modal + base (*might goes*); *should have/could have* + past participle (*should have went*; *should of*); second and third conditionals (*If I would have money*; *If I had known, I would come*). S7 adverb modifying an adjective/adverb (*real good*, *very careful*); *too/enough* order (*enough big*, *too much big*); degrees of adverbs (*more faster*). S8 double connectors (*Although it rained, but …*); verb + preposition (*depend of*, *married with*, *listen music*, *arrive to*); *since/for*.
- CP3 adds · S9 correlatives (*either … or*, *not only … but also*, *neither … nor*); conjunctive adverbs punctuation (*It rained, however we went*); *despite of*, *in spite of* + clause. S10 reported questions (*asked me where did I live*); *say/tell* (*He said me*); complex tags. S11 comma before *and/but/so* joining two independent clauses; comma after an introductory clause; paired commas for clearly non-restrictive elements (*My mother, who is 70, …*); semicolons between independent clauses; colons before lists; punctuation inside quotation marks; commonly confused words (*their/there/they're, its/it's, affect/effect, then/than, lose/loose, to/too, accept/except*). S12 *for example/however* placement and logic; synonym vs repetition; tense consistency as cohesion; unclear pronoun reference.

**Expanding (B2)**
- CP1 · S1 compound-complex punctuation and coordination; fragments used unintentionally. S2 abstract uncountables (*advices*, *researches*, *informations*); articles with generic/abstract nouns (*the happiness is important*); complex noun-phrase embedding. S3 defining vs non-defining relatives (*who/whom/whose/which/that*; *whom* as subject; preposition + *which*); substitution and ellipsis (*I hope so/not*; *so do I*; *the one/ones*). S4 narrative tenses (past perfect continuous, past continuous vs simple); future perfect (*By 2030 the city will build* → *will have built*); mixed conditionals; passive formation (*was build*, *is consist of*); *wish* + past (*I wish I have*); *used to/would* (*used to going*).
- CP2 adds · S5 inverted and long subjects (*There is many reasons*; *Neither of the answers are*; *The number of … are*; *Here comes the buses*); subjects joined by *or/nor*. S6 speculation modals (*must have went*, *can't have been* vs *couldn't have*); double modals (*might could*); hedging forms (*It is possible that it may can*). S7 *good/well* after action verbs (*played good*); *as … as*; *the more … the more*; register-appropriate adjectives (*kids* in a formal report → *children*, variants listed). S8 paired commas or dashes around interrupters (*The bridge, built in 1932 was …*); misplaced and dangling modifiers (*Walking down the street, the building was beautiful* — planted only where one subject is logical); prepositional idioms (*in regard of*, *according with*).
- CP3 adds · S9 parallel structure (*reading, to swim, and hiking*); appositive punctuation; semicolon misuse with subordinate clauses (*Although it rained; we went*); correlative parallelism. S10 reporting verb patterns (*suggested me to go*; *said me*); embedded questions (*I wonder what time is it*; *Do you know where does he live?*). S11 semicolons, colons, dashes, parentheses to set off clauses (*three problems; traffic, housing and noise* → colon); spelling of reference-checked academic words (*accommodate, separate, definitely, occurred, recommend, receive, necessary, government, environment*). S12 given/new ordering; paragraph openers; substitution/ellipsis errors; *this/these* number agreement; transition logic (*Moreover* where contrast is needed; *In conclusion* mid-paragraph).

**Mastery (C1)**
- CP1 · S1 negative-adverbial inversion (*Never I have seen* → *Never have I seen*; *Not only he came*); participle and reduced-relative forms (*a strip of land knowing as*); dangling reduced clauses where one subject is logical. S2 nominalisation choice (*The transferring of authority* → *transfer*); articles with nominalised subjects. S3 reference chains with sentential/collective antecedents where number is clear (*The committee published its findings; they were …*). S4 modals in the past (*would have liked to have gone*); narrative passives (*is believed to be built in 1300* → *to have been built*); *wish/if only* (*If only I would have known*).
- CP2 adds · S5 agreement with nominalised/abstract subjects (*The rise in prices and the fall in wages has*); *statistics/politics/news* by context. S6 inverted conditionals (*Had I knew*; *Should you needed*); past modals of regret/criticism. S7 collocation and shades of meaning (*make a research*; *strong rain*; *do a mistake*), register mismatch with variant list. S8 compounded prepositional phrases and connectors (*due to* + clause → *because* / *due to the* + noun, variants listed; *in favor to*).
- CP3 adds · S9 faulty parallelism in complex series; deliberate clause variation gone wrong (stranded subordinate clause after a semicolon). S10 rhetorical inversion (*Seldom we see*; *Only then he realised*); embedded questions in formal prose. S11 style-manual punctuation of quotations (period/comma inside closing quotation marks in American style; colon before a block quotation; parenthetical citation before the period: *… (Smith, 2019).*); ellipsis and brackets in quotations; semicolons in a complex series; confusables (*principle/principal, elicit/illicit, complement/compliment, discreet/discrete, affect/effect* as verb and noun). S12 *consequently/specifically/moreover* logic; nominalised cohesion (*This delay …* for a vague *This*); audience-adapted organisation (topic sentence buried mid-paragraph → moved, variants listed).

### 2.3 Passage length, planted errors, reading level

| Band | Words per passage | Errors per passage | Passages per checkpoint | Errors per checkpoint | Pass (ceil 80%) | Sentence length (avg) | Vocabulary ceiling (English Vocabulary Profile level; frequency band) |
|---|---|---|---|---|---|---|---|
| Foundations | 60-90 | 5 | 2 | 10 | 8/10 | 6-9 words | A1-A2 words; top 1,000 |
| Building | 100-140 | 6 | 2 | 12 | 10/12 | 9-12 | A2-B1; top 2,000 |
| Connecting | 160-220 | 8 | 2-3 | 16-24 | 13/16 · 20/24 | 12-16 | B1-B2; top 3,000 |
| Expanding | 240-320 | 10 | 3 | 30 | 24/30 | 15-20 | B2-C1; top 5,000 |
| Mastery | 330-420 | 12 | 3 | 36 | 29/36 | 18-25 | no ceiling; technical terms glossed in context |

Authoring rules (checked automatically where possible, frame §6):
1. The first sentence of every passage is clean (orientation). At most one planted error per
   sentence. Errors spread over the whole passage; no two consecutive sentences of the same
   error type.
2. Each passage covers ≥3 different sections; each checkpoint draw covers ≥6 sections
   (Foundations: ≥4).
3. Exactly one correct fix, or every accepted fix listed as a variant; the reviewer's job in the
   two independent passes is to find a second valid reading. Position-independent fixes
   (e.g. a missing comma that could go in two places) are rewritten until only one place works.
4. The clean passage passes the Harper rules engine with zero flags; a planted error must be
   flagged by the engine *or* by the item key — never rely on the engine alone.
5. Numbers in passages are written in words below Connecting except years and prices.
   Proper nouns are never the site of an error (a student cannot be expected to "fix" a name).
6. Reading level checked with the band's vocabulary ceiling (English Vocabulary Profile,
   https://www.englishprofile.org/wordlists/evp — not re-fetched) and sentence-length target;
   words above the ceiling are allowed only if glossed by the sentence itself.
7. American spelling and punctuation in the clean text; British variants listed as accepted
   fixes where the student's correction is otherwise right.

### 2.4 Fact-checking rule and source-credit line

**Rule.** Every checkable statement in a passage (date, number, name, place, sequence, cause)
is confirmed by **at least two reliable references of different types** before the passage
enters review; contested or fast-changing facts are hedged ("about", "more than", "as of
2026") or removed. Wikipedia may be used to find sources but does not count as one of the two.
Reference types accepted:
- general encyclopaedias (Encyclopaedia Britannica);
- official bodies and institutions (NASA, NIH, CDC, WHO, USDA, FDIC, IRS, OSHA, Smithsonian,
  Library of Congress, National Archives, US Department of State Office of the Historian,
  UNESCO, national statistics offices, NobelPrize.org);
- museums, monuments and heritage sites (British Museum, Science Museum, toureiffel.paris,
  National Park Service);
- university sites (.edu) and university presses; peer-reviewed articles (PubMed, journals);
- professional/scientific societies (American Chemical Society Landmarks, AHA, ADA);
- major reference dictionaries (Merriam-Webster, Oxford) for word facts.

Two references of the *same* type (two encyclopaedias) are accepted only when no other type
covers the fact. The checker records the reference, the exact figure found, and the date.
Time-sensitive numbers (visitor counts, populations, prices, wages) carry a re-check date
12 months out.

**Source-credit line format** (stored with the passage; shown on the feedback screen under
"Where these facts come from"):

```
Sources: (1) <Organisation>, "<Page or article title>", <URL>, accessed <YYYY-MM-DD>.
         (2) <Organisation>, "<Title>", <URL>, accessed <YYYY-MM-DD>.
Passage text is original ATTP writing; facts paraphrased, no quotation. Checked by <initials>
on <YYYY-MM-DD>; re-check due <YYYY-MM-DD>.
```

### 2.5 Passage topic bank (127 topics, 8 groups)

Bands: F Foundations · B Building · C Connecting · E Expanding · M Mastery. A topic listed
"F-C" yields separate passages at each of those bands (different clean texts). Content lines
state the facts a passage may use; each still needs the two-reference check before writing.

**A. Inventions (16)**

| # | Topic | Content (1-2 lines) | Bands |
|---|---|---|---|
| 1 | The bicycle | Drais's 1817 "running machine" had no pedals; pedals came in the 1860s and the chain-driven "safety bicycle" in 1885; bicycles outnumber cars worldwide. | F-C |
| 2 | The telephone | Bell's 1876 patent and first call to Watson; exchanges and operators; from party lines to mobiles. | F-E |
| 3 | The printing press | Gutenberg's movable metal type in Mainz, 1450s; the 42-line Bible c.1455; cheaper books, wider literacy. | B-M |
| 4 | The electric light bulb | Edison's long-lasting carbon-filament bulb (1879) built on earlier work by Swan and others; Menlo Park; power stations. | F-C |
| 5 | The airplane | Wright brothers, Kitty Hawk, 17 December 1903; first flight 12 seconds; passenger flight within two decades. | F-E |
| 6 | The automobile | Benz's 1886 motor car; Ford's Model T (1908) and moving assembly line (1913) cut the price. | B-E |
| 7 | The refrigerator | Household electric refrigerators spread in the 1920s-30s; safer food, less daily shopping. | F-B |
| 8 | The internet and the World Wide Web | ARPANET's first link 1969; Berners-Lee proposed the Web at CERN in 1989, public in 1991. | C-M |
| 9 | The smartphone | Early smartphones in the 1990s-2000s; the 2007 iPhone popularised touchscreens; billions of users today. | B-E |
| 10 | Photography | Niépce's earliest surviving photograph (1826-27); Daguerre's process announced 1839; Kodak's 1888 camera; digital photography. | B-E |
| 11 | Paper | Papermaking recorded in China in 105 CE (Cai Lun); spread through the Islamic world to Europe by the 12th century. | B-M |
| 12 | The magnetic compass | Lodestone compasses in China by the 11th century; used for navigation soon after; magnetic vs true north. | B-C |
| 13 | The steam engine | Newcomen's 1712 pumping engine; Watt's separate condenser (patented 1769); power for factories and railways. | C-M |
| 14 | Vaccination | Jenner's 1796 cowpox experiment; WHO declared smallpox eradicated in 1980, the only human disease wiped out. | C-M |
| 15 | The washing machine | Hand-cranked machines in the 1800s; electric machines from about 1908; hours of housework saved. | F-B |
| 16 | Radio and television | Marconi's wireless signals in the 1890s; regular TV broadcasting in the 1930s; colour TV after 1950. | C-E |

**B. Discoveries (15)**

| # | Topic | Content | Bands |
|---|---|---|---|
| 17 | Penicillin | Fleming's 1928 observation at St. Mary's Hospital; Florey and Chain's Oxford team (1940s); Nobel Prize 1945. | B-E |
| 18 | Newton and gravity | *Principia* (1687): laws of motion and universal gravitation; the apple story is a later anecdote. | C-M |
| 19 | The structure of DNA | Watson and Crick's 1953 double helix, using Franklin's X-ray data; Nobel Prize 1962. | C-M |
| 20 | The circulation of the blood | Harvey (1628) showed the heart pumps blood in a circuit. | C-M |
| 21 | Germ theory and handwashing | Semmelweis (1847) cut deaths by handwashing; Pasteur and Koch (1860s-80s) linked microbes to disease. | C-M |
| 22 | X-rays | Röntgen, 1895; first Nobel Prize in Physics (1901); medical imaging within months. | B-E |
| 23 | Radioactivity | Becquerel (1896) and the Curies; Marie Curie's two Nobel Prizes (1903 Physics, 1911 Chemistry). | B-E |
| 24 | Insulin | Banting and Best in Toronto, 1921-22; first patients 1922; Nobel Prize 1923. | C-E |
| 25 | The Sun at the centre | Copernicus (1543); Galileo's telescope observations (1609-10). | C-M |
| 26 | Electricity | Franklin's lightning experiment (1752); Volta's battery (1800); Faraday's motor (1821) and generator (1831). | C-M |
| 27 | Continental drift and plate tectonics | Wegener's 1912 idea, accepted only in the 1960s with sea-floor evidence. | E-M |
| 28 | The atom | Rutherford's nucleus (1911); Bohr's model (1913). | E-M |
| 29 | Vitamins and scurvy | Lind's 1747 trial with citrus fruit; vitamin C identified in the 1930s. | C-E |
| 30 | Tutankhamun's tomb | Found by Howard Carter in the Valley of the Kings, November 1922; nearly intact. | B-E |
| 31 | The Rosetta Stone | Found 1799; Champollion read the hieroglyphs in 1822; in the British Museum. | C-M |

**C. Historical events (16)**

| # | Topic | Content | Bands |
|---|---|---|---|
| 32 | The first Moon landing | Apollo 11, 20 July 1969; Armstrong and Aldrin walked, Collins orbited. | F-E |
| 33 | The Great Wall of China | Walls built over many centuries; most of what stands is Ming dynasty (1368-1644); thousands of kilometres. | F-C |
| 34 | The Titanic | Struck an iceberg and sank 15 April 1912; about 1,500 of some 2,200 people died. | B-E |
| 35 | The fall of the Berlin Wall | Border opened 9 November 1989; Germany reunified 3 October 1990. | C-M |
| 36 | The Black Death | Reached Europe in 1347; killed a large share of the population (estimates vary, often around a third). | E-M |
| 37 | The Great Fire of London | September 1666; most of the medieval city burned; Wren's St. Paul's rebuilt. | B-E |
| 38 | The first writing | Cuneiform in Mesopotamia c.3200 BCE, first for accounts and trade. | C-M |
| 39 | The Olympic Games | Ancient games at Olympia from 776 BCE; modern games revived in Athens, 1896; every four years. | F-E |
| 40 | Crossing the Atlantic by air | Alcock and Brown non-stop 1919; Lindbergh solo 1927; Earhart solo 1932. | C-E |
| 41 | Women's right to vote | New Zealand 1893; US 19th Amendment 1920; UK 1918 (some women) and 1928 (equal). | C-M |
| 42 | The Panama Canal | French failure 1881-89; US construction 1904-14; opened 15 August 1914; handed to Panama 31 December 1999; expansion 2016. | E-M |
| 43 | The Silk Road | Overland and sea routes linking China, Central Asia, the Middle East and Europe; silk, paper, spices, ideas. | C-M |
| 44 | The 1918 influenza pandemic | Infected about a third of the world's people; tens of millions died. | E-M |
| 45 | The Industrial Revolution | Britain, late 1700s-1800s: steam power, factories, railways, fast-growing cities. | E-M |
| 46 | The Suez Canal | Built 1859-69, connecting the Mediterranean and Red Sea; about 193 km today. | C-M |
| 47 | Ellis Island | US immigration station 1892-1954; about 12 million people entered through it. | B-E |
| 48 | The California Gold Rush | Gold found at Sutter's Mill, January 1848; some 300,000 people came; San Francisco boomed. | B-E |

**D. Famous places (16)**

| # | Topic | Content | Bands |
|---|---|---|---|
| 49 | The Eiffel Tower | Paris; wrought iron; finished 1889 for the world's fair; about 330 m with antennas; about 7 million visitors a year. | F-C |
| 50 | The Statue of Liberty | Gift from France, dedicated 1886; copper; designed by Bartholdi; Liberty Island, New York. | F-C |
| 51 | The Taj Mahal | Agra, India; built 1632-c.1653 by Shah Jahan for Mumtaz Mahal; white marble. | B-E |
| 52 | The Grand Canyon | Arizona; carved by the Colorado River; about 446 km long and up to 1.8 km deep; national park since 1919. | F-C |
| 53 | Machu Picchu | Inca site in the Peruvian Andes (15th century), about 2,430 m up; brought to world attention by Bingham in 1911. | C-E |
| 54 | The Pyramids of Giza | The Great Pyramid (c.2560 BCE, Khufu) was about 146 m tall; the last surviving ancient wonder. | B-E |
| 55 | The Colosseum | Rome; completed 80 CE; held about 50,000 spectators. | B-E |
| 56 | Niagara Falls | On the US-Canada border; three falls; hydroelectric power; a honeymoon and tourist destination. | F-C |
| 57 | The Great Barrier Reef | Off Australia, about 2,300 km long; the largest coral reef system; bleaching from warming seas. | C-M |
| 58 | Mount Everest | 8,849 m (2020 survey); Hillary and Tenzing reached the top in 1953. | B-E |
| 59 | The Amazon | The largest river by volume; rainforest across nine countries; huge biodiversity. | C-E |
| 60 | Petra | Nabataean city in Jordan carved into rock; Burckhardt described it to Europe in 1812. | C-M |
| 61 | The Sahara | The largest hot desert, about 9 million km²; oases, camels, ancient trade routes. | F-C |
| 62 | Venice | Built on more than 100 small islands; canals instead of streets; flood barriers (MOSE) operating since 2020. | C-E |
| 63 | The Golden Gate Bridge | San Francisco; opened 1937; 1,280 m main span; painted "International Orange". | B-E |
| 64 | Antarctica | The coldest continent; no permanent population; Antarctic Treaty (1959) reserves it for peace and science. | C-M |

**E. Notable people (16)**

| # | Topic | Content | Bands |
|---|---|---|---|
| 65 | Marie Curie | Polish-born physicist and chemist; first person to win two Nobel Prizes; died 1934. | B-E |
| 66 | Nelson Mandela | 27 years in prison; President of South Africa 1994-99; Nobel Peace Prize 1993. | B-E |
| 67 | Leonardo da Vinci | 1452-1519; *Mona Lisa*, *The Last Supper*; notebooks of inventions and anatomy. | C-M |
| 68 | Florence Nightingale | Crimean War nursing 1854-56; founded a nursing school in 1860; used statistics to argue for reform. | C-E |
| 69 | Mahatma Gandhi | Nonviolent resistance; Salt March 1930; India's independence 1947. | C-M |
| 70 | Helen Keller | Deaf and blind from infancy; taught by Anne Sullivan; graduated from Radcliffe College 1904; author and activist. | B-E |
| 71 | Albert Einstein | Special relativity 1905, general relativity 1915; Nobel Prize 1921 for the photoelectric effect. | C-M |
| 72 | Rosa Parks | Refused to give up her bus seat in Montgomery, 1955; the year-long bus boycott. | B-E |
| 73 | Wangari Maathai | Founded Kenya's Green Belt Movement (1977); Nobel Peace Prize 2004. | C-M |
| 74 | Ibn Battuta | 14th-century traveller from Tangier; about 30 years and tens of thousands of kilometres; the *Rihla*. | C-M |
| 75 | Ada Lovelace | 1843 notes on Babbage's Analytical Engine, often called the first computer program. | C-M |
| 76 | Jonas Salk | Polio vaccine declared safe and effective in 1955; did not patent it. | C-E |
| 77 | Malala Yousafzai | Campaigner for girls' education; Nobel Peace Prize 2014, the youngest laureate. | B-E |
| 78 | Louis Pasteur | Pasteurisation; rabies vaccine first used on a person in 1885. | C-E |
| 79 | Katherine Johnson | NASA mathematician who calculated flight paths for early US space missions; Presidential Medal of Freedom 2015. | C-E |
| 80 | Frida Kahlo | Mexican painter (1907-54) known for self-portraits made after a serious accident. | B-E |

**F. Science and nature (16)**

| # | Topic | Content | Bands |
|---|---|---|---|
| 81 | Honey bees | One queen, thousands of workers; the waggle dance; pollination of many crops. | F-C |
| 82 | The water cycle | Evaporation, condensation, precipitation; the same water used again and again. | F-B |
| 83 | Volcanoes | Magma, eruptions, the Pacific "Ring of Fire"; Vesuvius buried Pompeii in 79 CE. | B-E |
| 84 | Earthquakes | Moving plates; magnitude scales; drop, cover, hold on. | B-E |
| 85 | The human heart | Four chambers; about 100,000 beats a day; how exercise helps it. | B-E |
| 86 | The Sun | A star about 4.6 billion years old; its light takes about 8 minutes to reach Earth. | F-C |
| 87 | The Moon and tides | About 384,000 km away; its gravity causes two high tides a day. | F-C |
| 88 | Whales | Mammals that breathe air; the blue whale is the largest animal known; whale songs. | F-C |
| 89 | Bird migration | The Arctic tern flies between the Arctic and Antarctic each year; navigation by sun, stars and magnetism. | C-E |
| 90 | Rainforests | Warm, wet, extraordinarily rich in species; deforestation and its effects. | C-M |
| 91 | Photosynthesis | Plants use light, water and carbon dioxide to make sugar and release oxygen. | C-E |
| 92 | Weather and climate | Weather is today; climate is the long-term pattern; the greenhouse effect in plain terms. | C-M |
| 93 | Elephants | The largest land animals; herds led by a matriarch; international ivory trade banned in 1989. | B-E |
| 94 | Coral reefs | Corals are animals; reefs shelter about a quarter of marine species; bleaching. | C-M |
| 95 | Sleep | Sleep cycles and REM; adults need about 7-9 hours; effects of too little. | F-C |
| 96 | The octopus | Three hearts, blue blood, eight arms, remarkable camouflage and problem-solving. | B-E |

**G. Health and daily life (15)**

| # | Topic | Content | Bands |
|---|---|---|---|
| 97 | Handwashing | Soap, 20 seconds, before food and after the bathroom; Semmelweis's 1847 finding. | F-B |
| 98 | A balanced plate | Half fruit and vegetables, a quarter grains, a quarter protein (MyPlate). | F-B |
| 99 | Reading a medicine label | Dose, how often, with or without food, warnings; ask the pharmacist. | F-B |
| 100 | Shift work and sleep | The body clock; tips for night workers. | B-C |
| 101 | Walking for health | About 150 minutes of moderate activity a week (WHO/CDC); stairs, errands on foot. | F-C |
| 102 | Sugar and soft drinks | Added-sugar limits (AHA: about 25 g women, 36 g men per day); tooth decay. | B-E |
| 103 | Vaccines for adults | Yearly flu shot; tetanus booster every 10 years (CDC). | B-C |
| 104 | Blood pressure | Normal below 120/80; high blood pressure often has no symptoms. | B-E |
| 105 | Stress and the body | Fight-or-flight, cortisol, sleep and exercise as buffers. | C-E |
| 106 | Dental care | Brush twice a day with fluoride toothpaste, floss daily, limit sugar; check-ups. | F-B |
| 107 | Recycling | Plastic codes, sorting, why aluminium cans are worth recycling. | B-C |
| 108 | Safe food storage | Refrigerator at or below 40 °F (4 °C); the two-hour rule for leftovers (USDA). | F-C |
| 109 | Calling 911 | The US emergency number since 1968; what the operator will ask. | F-B |
| 110 | Public libraries | Free cards, books, internet, classes; Carnegie funded about 1,700 US library buildings. | F-C |
| 111 | Sun safety | UV, broad-spectrum SPF 30+, hats and shade; skin cancer is common and preventable. | F-B |

**H. Work and money (16)**

| # | Topic | Content | Bands |
|---|---|---|---|
| 112 | The minimum wage | US federal minimum $7.25 an hour since 2009; many states and cities set higher rates. | B-E |
| 113 | Reading a pay stub | Gross vs net pay; federal tax, Social Security, Medicare deductions. | B-C |
| 114 | Credit scores | FICO range 300-850; paying on time and low balances matter most. | C-E |
| 115 | Interest and saving | Compound interest; the rule of 72. | C-E |
| 116 | A simple budget | The 50/30/20 idea: needs, wants, savings. | B-C |
| 117 | The history of money | Barter, early coins in Lydia (7th century BCE), paper money in China, cards and phones. | C-M |
| 118 | Bank accounts | Checking vs savings; FDIC insurance up to $250,000 per depositor per bank. | B-C |
| 119 | Job interviews | Preparing examples (the STAR method); common questions; follow-up thanks. | B-E |
| 120 | Workplace safety | OSHA (1970): the right to a safe workplace and to report hazards without punishment. | B-E |
| 121 | The eight-hour day | Haymarket 1886; the Fair Labor Standards Act (1938) set a federal minimum wage and the 40-hour week. | C-M |
| 122 | Taxes | Filing by mid-April; the W-2 form; refunds; sales tax varies by state. | B-E |
| 123 | Small business | Most US firms are small; licences, an LLC, keeping records. | C-M |
| 124 | Remote work | Grew sharply after 2020; benefits and costs for workers and employers. | C-E |
| 125 | Renting an apartment | Lease, security deposit, utilities, tenant rights and repairs. | F-C |
| 126 | Tipping in the US | 15-20% at restaurants; customs elsewhere differ. | F-C |
| 127 | The stock market | Shares, the New York Stock Exchange (1792 Buttonwood Agreement), index funds. | E-M |

### 2.6 Three worked passages

Format: passage as the student sees it (errors planted, unmarked), then the answer key
(order of appearance; **section · rule → lesson tag**; accepted variants), then the credit line.

#### Worked passage 1 — Foundations, CP1 (sections 1-4), topic 49 "The Eiffel Tower"

67 words, 5 planted errors, pass = 8/10 across the two passages of the checkpoint.

> The Eiffel Tower is in Paris. Paris the capital of France. The tower are made of iron. It
> is about 330 meters tall. Workers finished it in 1889. It has three floor for visitors.
> People go up in elevators, or them climb the stairs. At night, thousands of lights make it
> shine. Every year, about seven million people visit it. It is very famous place in Paris.

| # | Planted | Fix | Section · rule → lesson |
|---|---|---|---|
| 1 | Paris **the** capital of France. | Paris **is the** capital of France. | S1 · every sentence needs a verb → F-S1-L2 |
| 2 | The tower **are** made of iron. | **is** | S4 · *is/are* with a singular subject → F-S4-L1 |
| 3 | three **floor** | **floors** | S2 · plural -s after a number → F-S2-L2 |
| 4 | or **them** climb the stairs | **they** | S3 · subject pronoun before a verb → F-S3-L1 |
| 5 | It is **very famous place** | It is **a very famous place** | S2 · *a/an* before a singular count noun → F-S2-L3 |

Accepted variants: #1 "Paris is France's capital" (whole-sentence answers allowed);
#5 "a famous place" is not accepted (drops *very*, changes meaning). False-alarm answers the
app explains: "Workers finished it in 1889" (regular past, correct); "thousands of lights"
(plural correct).

```
Sources: (1) Société d'Exploitation de la Tour Eiffel, "The birth of the Eiffel Tower",
         https://www.toureiffel.paris/en/the-monument/history, accessed 2026-09-05.
         (2) Encyclopaedia Britannica, "Eiffel Tower",
         https://www.britannica.com/topic/Eiffel-Tower-Paris-France, accessed 2026-09-05.
Passage text is original ATTP writing; facts paraphrased, no quotation. Checked by CD on
2026-09-05; re-check due 2027-09-05 (visitor number).
```

#### Worked passage 2 — Connecting, CP2 (sections 1-8), topic 17 "Penicillin"

190 words, 8 planted errors; the checkpoint draws two passages (pass 13/16).

> In September 1928, a Scottish scientist named Alexander Fleming returned to his laboratory
> at St. Mary's Hospital in London after a holiday. The dishes of bacteria on his bench was
> uncovered, and a mold was growing on one of them. When he looks at the dish closely, he
> noticed that the bacteria around the mold had died. Fleming realized that the mold, who was
> a type of Penicillium, produced a substance that killed bacteria. He called it penicillin,
> he began to test it. Fleming has published his results in 1929. However, he could not to
> produce large amounts of the substance, so for ten years little happened. In the early
> 1940s, a team at Oxford University led by Howard Florey and Ernst Chain found a way to
> purify penicillin and tested it on patients. During the Second World War, factories in the
> United States made the drug in huge quantities. By 1944 there was penicillin enough to
> treat every wounded Allied soldier. In 1945, Fleming, Florey and Chain shared the Nobel
> Prize in Physiology or Medicine. Today, doctors still depend of antibiotics, although many
> bacteria have become resistant to them.

| # | Planted | Fix | Section · rule → lesson |
|---|---|---|---|
| 1 | The dishes of bacteria on his bench **was** uncovered | **were** | S5 · agreement with an intervening phrase (*dishes … were*) → C-S5-L1 |
| 2 | When he **looks** at the dish closely, he noticed | **looked** | S4 · tense consistency in a past narrative → C-S4-L1 |
| 3 | the mold, **who** was a type of Penicillium | **which** | S2 · relative pronoun for things → C-S2-L2 |
| 4 | He called it penicillin**,** he began to test it. | penicillin**, and** he began / penicillin**;** he began / penicillin**.** He began | S1 · comma splice → C-S1-L2 |
| 5 | Fleming **has published** his results in 1929. | **published** | S4 · past simple with a finished time → C-S4-L2 |
| 6 | he could not **to produce** | could not **produce** | S6 · modal + base verb → C-S6-L1 |
| 7 | there was **penicillin enough** | **enough penicillin** | S7 · *enough* before a noun → C-S7-L3 |
| 8 | doctors still depend **of** antibiotics | depend **on** | S8 · verb + preposition → C-S8-L2 |

Variants: #4 any of the three joins; "penicillin and began" (dropped second *he*) also
accepted. False alarms explained: "the bacteria … had died" (past perfect for the earlier
event, correct); "although many bacteria have become resistant" (present perfect for a
continuing situation, correct).

```
Sources: (1) American Chemical Society, National Historic Chemical Landmarks, "Alexander
         Fleming Discovery and Development of Penicillin",
         https://www.acs.org/education/whatischemistry/landmarks/flemingpenicillin.html,
         accessed 2026-09-05.
         (2) NobelPrize.org, "The Nobel Prize in Physiology or Medicine 1945",
         https://www.nobelprize.org/prizes/medicine/1945/summary/, accessed 2026-09-05.
         (3) Encyclopaedia Britannica, "Today in History, September 3, 1928",
         https://www.britannica.com/today-in-history/September-3-1928-Alexander-Fleming-Finds-Penicillin,
         accessed 2026-09-05.
Passage text is original ATTP writing; facts paraphrased, no quotation. Checked by CD on
2026-09-05; re-check due 2027-09-05.
```

#### Worked passage 3 — Mastery, CP3 (sections 1-12), topic 42 "The Panama Canal"

383 words, 12 planted errors; the checkpoint draws three passages (pass 29/36).

> The idea of a waterway across the Isthmus of Panama is far older than the canal itself;
> Spanish engineers are believed to survey possible routes as early as the sixteenth century.
> Not until 1881, however, construction actually began, when a French company led by
> Ferdinand de Lesseps, the celebrated builder of the Suez Canal, started digging a sea-level
> channel. The attempt was a disaster. The engineering problems of the mountainous terrain
> were serious underestimated. Yellow fever and malaria killed thousands of workers;
> consequently, the company's finances were equally chaotic, and by 1889 it had collapsed.
> Had the French company understand the terrain and the climate, it might have succeeded,
> but it had spent an enormous sum with little to show for it.
>
> The United States took over the project in 1904. Panama, newly independent from Colombia,
> had granted them control of a strip of land along the route. This territory, knowing as
> the Canal Zone, was governed by the United States for decades. Two decisions proved
> decisive; the choice of a lock canal and the defeat of disease. First, the chief engineer
> John Stevens persuaded Washington to abandon the sea-level plan in favor to a system of
> locks that would lift ships to an artificial lake and lower them again on the other side.
> Second, the army doctor William Gorgas, who had already helped to eliminate yellow fever in
> Havana, drained swamps, screened windows and to fumigate buildings until the diseases that
> had defeated the French were brought under control. The elimination of yellow fever and
> malaria were as important as any machine. Under Stevens's successor, George Goethals, the
> work was completed, and on August 15, 1914, the cargo ship SS Ancon made the first official
> transit.
>
> The canal, which is roughly 80 kilometers (50 miles) long, transformed world trade by
> removing the need to sail around South America. It remained under American administration
> for most of the twentieth century. In 1977, President Jimmy Carter and General Omar Torrijos
> signed treaties that provided for a gradual transfer of authority, and at noon on
> December 31, 1999, Panama assumed full control. Since then the Panama Canal Authority has
> run the waterway as a national enterprise. Its most ambitious project, a third set of much
> larger locks, opened in June 2016 and allowed a new generation of ships to pass through.
> Historians still debate whether could the human cost of the canal have been avoided; what
> is not in doubt is that few engineering projects have changed the map of commerce so
> completely.

| # | Planted | Fix | Section · rule → lesson |
|---|---|---|---|
| 1 | are believed **to survey** possible routes as early as the sixteenth century | **to have surveyed** | S4 · passive report + perfect infinitive for an earlier time → M-S4-L2 |
| 2 | Not until 1881, however, **construction actually began** | **did construction actually begin** | S1 · inversion after *Not until* → M-S1-L1 |
| 3 | were **serious** underestimated | **seriously** | S7 · adverb modifying a participle (B1 visit, cumulative) → C-S7-L1 |
| 4 | killed thousands of workers; **consequently**, the company's finances were equally chaotic | **moreover / in addition / furthermore / also** (comma kept) | S12 · connective logic (addition, not result) → M-S12-L1 |
| 5 | Had the French company **understand** | **understood** | S6 · inverted third conditional → M-S6-L1 |
| 6 | had granted **them** control | **it** | S3 · reference chain: *the United States* is singular here → M-S3-L1 |
| 7 | This territory, **knowing** as the Canal Zone | **known** | S1 · past-participle reduced relative → M-S1-L2 |
| 8 | Two decisions proved decisive**;** the choice of a lock canal and the defeat of disease. | decisive**:** | S11 · colon introduces the list that explains → M-S11-L1 |
| 9 | in favor **to** a system of locks | in favor **of** | S8 · fixed prepositional phrase → M-S8-L1 |
| 10 | drained swamps, screened windows and **to fumigate** buildings | **fumigated** | S9 · parallel structure in a series → M-S9-L1 |
| 11 | The elimination of yellow fever and malaria **were** | **was** | S5 · nominalised head noun *elimination* is singular → M-S5-L1 |
| 12 | debate whether **could the human cost** of the canal **have been avoided** | whether **the human cost** of the canal **could have been avoided** | S10 · embedded question keeps statement order → M-S10-L1 |

Variants: #4 any addition connective; #8 a dash also accepted; #12 "whether or not the human
cost … could have been avoided". False alarms explained: "the diseases that had defeated the
French" (past perfect, correct); "few engineering projects have changed" (present perfect,
correct); "Stevens's" (singular possessive, both *Stevens's* and *Stevens'* accepted if
tapped, since style guides differ — but it is not a planted error).

```
Sources: (1) Encyclopaedia Britannica, "Panama Canal",
         https://www.britannica.com/topic/Panama-Canal, accessed 2026-09-05.
         (2) U.S. Department of State, Office of the Historian, "Building the Panama Canal,
         1903-1914", https://history.state.gov/milestones/1899-1913/panama-canal,
         accessed 2026-09-05.
         (3) PBS American Experience, "Creating the Canal",
         https://www.pbs.org/wgbh/americanexperience/features/panama-canal-creating-canal/,
         accessed 2026-09-05.
Passage text is original ATTP writing; facts paraphrased, no quotation. Checked by CD on
2026-09-05; re-check due 2027-09-05.
```

### 2.7 Keeping the passage bank fresh (target 300+)

| Lever | Rule |
|---|---|
| Growth schedule | Phase 2 (frame §11): 60 passages — Foundations and Building, CP1-CP3, 10 per checkpoint. Phase 3: +120 (Connecting, Expanding, then Mastery). Then ≥12 new passages a month → 300+ within about 18 months; 127 topics × up to 3 bands each already gives ~330 clean-text slots. |
| Seed variants | Each clean text carries 2-3 *seeds* (different planted-error sets, same allowed types). Seeds multiply practice without new fact-checking; they count as "new" only across cohorts or after 30 days (2.1), never for an immediate retry. 300 clean texts × 2.5 seeds ≈ 750 distinct checkpoint experiences. |
| Coverage quotas | Per band and checkpoint: every allowed rule appears in at least 4 passages; no single section supplies more than 30% of a checkpoint pool's errors. The dashboard shows the quota table so authors write to the gaps. |
| Retirement | Retire (and rewrite) a passage when: a fact fails its 12-month re-check; ≥3 unresolved problem reports; an error's found-rate is below 35% or above 98% across 100+ attempts (too hard or trivial); or a second valid fix is discovered (frame §6 review). Retired passages are kept as seeds for teacher-led review, never in tests. |
| Topic register | One row per topic with band versions, seeds, sources, re-check dates and retirement history; a new topic is added only if it is absent from the register (no near-duplicates such as "The Eiffel Tower" and "Gustave Eiffel"). Anniversaries and news-independent evergreen subjects are preferred; nothing tied to current politics. |
| Teacher contributions | Teachers submit topics or drafts from the dashboard; a draft becomes a passage only after the two-reference check and two review passes. Credit line records the author's initials. |
| Learner-driven refresh | Once a student has completed a checkpoint, the app schedules one seed from that checkpoint as spaced review (30-60 days later, optional, ungraded). |
| Annual fact sweep | Every August, all time-sensitive numbers (visitor counts, wages, populations, "since 2020" claims) are re-checked in one pass; the credit line's re-check date is updated. |

### 2.8 Sources for Part 2

- Platform contract: `docs/curriculum/00-platform-frame.md` (§6 banks, §7 checkpoints);
  section-by-band content: `docs/standards-mapping.md` Section C.
- Reference types (2.4), with the sites used for the worked passages: Encyclopaedia Britannica
  https://www.britannica.com/ ; Office of the Historian https://history.state.gov/ ;
  NobelPrize.org https://www.nobelprize.org/ ; ACS Landmarks
  https://www.acs.org/education/whatischemistry/landmarks.html ; official Eiffel Tower site
  https://www.toureiffel.paris/en ; PBS American Experience https://www.pbs.org/wgbh/americanexperience/
- Style conventions for planted punctuation (American classroom standard, variants named):
  Purdue OWL punctuation https://owl.purdue.edu/owl/general_writing/punctuation/index.html ;
  MLA Style Center https://style.mla.org/ ; APA Style https://apastyle.apa.org/ ;
  Chicago Manual of Style Online https://www.chicagomanualofstyle.org/ (subscription).
- Vocabulary ceilings: English Vocabulary Profile https://www.englishprofile.org/wordlists/evp
  (not re-fetched during this pass).

---

### Unverified items in this plan

1. The BBC pronunciation page and the CEFR Companion Volume PDF were confirmed by index
   pages, not fetched (both block automated access). 2. The Cambridge C1 speaking-scale URL
   (168620) comes from a search index. 3. The English Vocabulary Profile URL was not
   re-fetched. 4. The L1 matrix is a synthesis (Swan & Smith + accent-archive listening), not a
   study result; treat ● / ○ as sequencing hints. 5. Bank-size totals in 1.7 are sums of the
   planned item counts, not of items that exist yet. 6. Passage facts in the topic bank were
   checked once from memory of standard references; each still needs the two-reference check
   before writing, as 2.4 requires.
