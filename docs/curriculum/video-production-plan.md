# Story videos for every lesson — production plan

Decision (2026-09-06): every lesson gets two explanations that say the same thing in the same
order: a short animated story (60-90 seconds) and a written page. The story is made with
Remotion from a small data file; the written page is generated from the same data. Sample:
`samples/lesson-4F-B3-just-already-yet.md` and the rendered video `la7zy-just-already-yet.mp4`
(scene stills in the storyboard sheet).

## 1. The shape of a lesson story (the same seven beats every time)

| Beat | Seconds | What the student sees | What the narration says |
|---|---|---|---|
| 1 Title | 0-10 | lesson name, the target words as coloured chips | the lesson in one sentence |
| 2 Story 1 | 10-25 | a real-life moment (bus stop, kitchen, clinic, office) with a clock; the sentence builds word by word in the colour code | the moment, then the sentence, then the meaning in five words |
| 3 Story 2 | 25-40 | second moment, second target word or use | same pattern |
| 4 Story 3 | 40-55 | third moment | same pattern |
| 5 The rule | 55-65 | the pattern in slots (have / has + just + verb) | where the word goes |
| 6 Watch out | 65-80 | two wrong sentences struck through, the right ones with a tick | the two mistakes students actually make |
| 7 Recap and try | 80-90 | the three meanings; the "now try 8 questions" stamp | recap, then the invitation |

A lesson with one target rule (for example "third-person -s") uses beats 2-4 for three examples of
the same rule. Drill lessons (irregular verb sets, spelling) use a different, shorter template
(list + rhythm), not the story template.

## 2. Everything is data; the template does the drawing

Each lesson has one JSON file:

```
{
  "tag": "4F-B3",
  "title": "Just, already and yet",
  "unit": "Present Perfect", "band": "Building", "lesson": 3, "of": 5,
  "character": "Ana",
  "scenes": [
    {"time": "8:06", "place": "bus-stop", "line": "The bus has just left.",
     "words": [["The bus","subj"],["has","verb"],["just","time"],["left","verb"],["."]],
     "meaning": ["just", "a short time ago"], "narration": "..."},
    ...
  ],
  "rule": [[["have / has","verb"],["just","time"],["verb","verb"]], ...],
  "mistakes": [["I just have eaten.", "I have just eaten."], ...],
  "recap": [["just","a short time ago"], ...],
  "next": "for and since"
}
```

Places are a small library of scenes drawn in code (bus stop, office desk, kitchen table,
clinic, shop, phone call, park, station). Characters are the same simple figures with different
colours. New lessons need new text, not new drawings. The written page is generated from the same
file, so the two can never disagree.

## 3. Voice

- Now: the Windows voice, as a placeholder to set timing (each scene's length comes from the
  narration length plus a pause).
- Shipped: the natural voice from the pre-generated audio pipeline (Sesame CSM on the PC),
  one file per scene, re-generated when a line changes. No text-to-speech runs on the phone.
- Narration text is written at the band's level and never says a grammar term before the
  example has been shown.

## 4. How it reaches the phone (and stays free)

Two ways to deliver the same story. Both are supported by the same code.

| Way | What is stored | Size for 461 lessons | Offline | Use |
|---|---|---|---|---|
| Live story in the app (Remotion Player) | JSON + narration audio only | about 230 MB total (0.5 MB per lesson at 48 kbps mono) | yes, cached per section | default inside the platform |
| MP4 file | rendered video, 720p | 3-4 GB (7-9 MB per lesson) | yes, once saved | sharing on WhatsApp, teacher demos, YouTube |

The live story is the default because it fits GitHub Pages and works offline with the rest of the
section. The MP4s are rendered on the PC as needed; the whole set would need Cloudflare R2 (free
tier 10 GB) or one repo per band, so they are not hosted by default.

## 5. Production numbers

| Item | Value |
|---|---|
| Lessons in scope | 461 (grammar sections plus the Verbs and Tenses strand) |
| Story template lessons | about 400; drill template about 60 |
| Writing per lesson | 7 narration lines, 3 sentences, 2 mistakes, 3 meanings (about 120 words) |
| Render time per MP4 | 3-6 minutes on this PC at 1080x1920; 1-2 minutes at 720p |
| Review | every story checked against the lesson's rule and its 6-10 sources before it ships |

## 6. Order of work

1. Finish the story template (done for the sample) and the drill template.
2. Build the place library (8 places) and 6 character colours.
3. Write the JSON for Foundations sections 1-2 and tenses units 4A-4B (the phase-1 lessons).
4. Generate written pages from the same JSON; teacher spot-check.
5. Wire the Player into the lesson screen; MP4 export on demand.
6. Swap the placeholder voice for the natural voice when the audio pipeline is ready.
