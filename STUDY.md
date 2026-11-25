# STUDY.md — "Have You Tried Turning It Off?"

Entry title: **Escalated to Tier 2**
Competition: `u-motasimfuad-have-you-tried-turning-it-off-154a938b` ($10 pool, free entry)

## The brief

One funny line, under 200 characters, spoken by a hopeless tech support
agent to a desperate customer. An AI judge compares lines pairwise over
three private blind rounds. The leaderboard and scores are withheld until
after the results are published, so no top-10 study was possible — this
entry was chosen by reasoning from the brief alone, not by copying
winners.

## What wins a pairwise blind comparison

1. **Instantly funny on first read.** The judge sees two bare lines with
   no setup and no context, so the joke must land in one sentence.
2. **Fresh, not the cliche itself.** "Have you tried turning it off and
   on again?" will appear in a large share of the ~900 entries. A line
   that merely repeats the trope loses to one that subverts it.
3. **The hopelessness must be the agent's own.** The brief's subject is
   the hopeless agent, not the customer — shared misery and giving up
   beat a competent-sounding agent.
4. **A concrete, vivid, quotable image** beats an abstract complaint,
   and a punchline that lands in the second half (setup, then reveal)
   beats a flat statement.
5. **Spoken directly to the customer** ("Your ticket…") — it must sound
   like dialogue, not a caption.

## Candidates considered

Twenty-two candidate lines were scored 1–5 against those rules. The
strongest alternatives were:

- *"The system says your issue was resolved three days ago. The system
  has never met you, but I admire its confidence."* (4.5/5) — absurdist
  and memorable, kept as runner-up.
- *"Sir, I've been on hold with our own support line for forty minutes.
  We're in this together now."* (4/5) — strong solidarity, specific
  detail.
- *"I'm going to put you on a brief hold while I Google your exact
  problem and pretend I knew the answer."* (4/5) — honest and relatable.
- *"I understand your frustration — I wrote the same complaint about
  this system last year, and it's still open."* (4/5) — the hopeless
  agent embodied.

Weaker lines mostly repeated the "turn it off and on again" cliche,
meandered without a punchline, or drifted off-topic (e.g. a security
joke about hackers, which is not a support joke).

## The chosen line (101 characters)

> Your ticket has been escalated to Tier 2, which is me, in a different chair, with the same manual.

## Why this line wins

- **It IS the support experience**, not a joke about it: every desperate
  customer has lived an escalation, so it lands instantly in a blind pair.
- **Setup, then reveal:** "escalated to Tier 2" promises help; "me, in a
  different chair, with the same manual" demolishes that promise with a
  concrete, quotable image.
- **The hopelessness belongs to the agent:** he IS the escalation, and he
  knows it is useless.
- **It never repeats the cliche**, so it stands out against the many
  entries that will lean on "turn it off and on again".
- **101 characters, one sentence, spoken directly to the customer**
  ("Your ticket…"), clean dialogue voice.

## Verification

`python3 main.py` writes exactly this line plus a newline to
`/output/entry.txt`; re-running produces byte-identical output
(sha256 `96d9b97f0c618b80d54ff05af4c6ea6477f220edde5e97dc1b5191c9a492405b`).
The program is deterministic — no network, no randomness, no clock, no
environment input — and asserts the line is a single line under 200
characters before writing it.
