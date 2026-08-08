# Peer-Testing Plan

## Purpose

The test checks whether urgency is understandable from language alone and
whether the visual interface reinforces that meaning without creating a new
error. It also checks whether a first-time user can move from a queue alert to
source-data review and a nurse-owned confirm or override decision.

This is the interim plan. Results, quotes, design changes, and the final
three-page design and test report are not claimed here.

## Participants

- Recruit at least **three CariSurg cohort peers** who did not help design this
  interface and are not members of the same final-presentation group.
- Invite four people so one cancellation does not leave the study short.
- Record only a tester code and relevant background, for example `P1 - software
  track`. Do not collect patient data or unnecessary personal information.
- Explain that the prototype is fictional, the interface is being tested rather
  than the person, participation is voluntary, and quotes will be de-identified.

Peers can evaluate comprehension and interaction. They cannot validate the
clinical response times or replace later testing with triage nurses.

## Materials

1. Four printed or on-screen words-only alert cards.
2. A different random card order for each tester.
3. The full queue and alert prototype with the same four messages.
4. A stopwatch, observation sheet, and verbatim note or audio-capture method.
5. Greyscale, 200% zoom, and keyboard-only variants.

If audio is recorded, obtain explicit permission first and delete it after the
notes have been checked.

## Neutral facilitator opening

> This is a fictional prototype for an emergency-department triage support
> interface. I am testing the design, not you. Please say aloud what you see,
> what you expect, and what confuses you. There are no right or wrong answers.
> I will take notes and will only help if you are completely stuck.

Do not explain the tiers, colours, icons, or intended button path before the
test. Do not praise, correct, defend, or complete a tester's thought.

## Stage 1: words only

1. Present the four primary alerts as plain black text with no tier label,
   colour, icon, patient detail, or fixed order.
2. Start timing when the messages appear.
3. Ask: **"Rank these messages from highest to lowest urgency."**
4. Ask the tester to think aloud. Record the order, time to identify the first
   priority, hesitations, corrections, and exact words used to explain it.
5. Ask: **"What made one message feel more urgent than another?"**

The critical message should be identified first within five seconds. If the
pilot reveals a language failure, pause the full study, revise the wording, and
restart with new random orders. Visual design must not rescue unclear text.

## Stage 2: full interface

Show the same wording inside the complete queue prototype. Do not change the
messages between stages for a given tester.

1. **Prioritise:** "Which patient would you act on first?"
2. **Inspect:** "Show me what information you would check before acting."
3. **Act:** "Continue as if you agree with the model suggestion."
4. **Recover:** "Now assume the suggestion does not match your judgement. Show
   me what you would do."
5. Repeat the urgency ranking and ask what changed, stood out, or confused them.

Record whether the tester reads the message before opening details, notices the
data source and time, finds the primary action, finds override without help,
and can recover from a wrong click.

## Accessibility checks

- Repeat the priority task in greyscale. Ask what still communicates urgency.
- Use 200% zoom and confirm that the tier, primary message, and action remain in
  the same reading path.
- Complete the queue-to-decision path by keyboard only and note any focus trap,
  missing label, or invisible focus state.
- Lower screen brightness and add glare. Ask the tester to identify each tier.
- Ask what would happen if the attention tone could not be heard.

## Measures and observation sheet

| Measure | Capture |
| --- | --- |
| Words-only ranking | Exact four-tier order and whether Critical was first |
| Recognition time | Seconds to first-priority identification |
| Visual influence | Any change between stage-one and stage-two ranking |
| Task success | Prioritise, inspect, confirm, override: completed / help / failed |
| Errors and recovery | Wrong click, missed cue, pause location, recovery without help |
| Accessibility | Greyscale, zoom, keyboard, glare, and no-audio outcome |
| Verbatim evidence | Exact quote, task, what was read correctly, what was misread, suggestion |

Provisional success criteria are: all testers place Critical first; at least two
of three produce the complete intended words-only order; no visual styling
reverses a correct ranking; and every tester can find confirm and override
without an explanation. These are design gates for the prototype, not clinical
performance claims.

## Post-test questions

- Which message would you act on first if all four appeared together? Why?
- What was the most challenging part of the interface?
- Was there anything on the screen you did not understand?
- What did you expect to happen after selecting the primary action?
- Which cue did you rely on most: wording, label, symbol, position, or colour?
- What one change would make the next version safer or clearer?

Avoid leading questions such as "Did you find it easy?" or "Did the red alert
look critical?"

## Analysis and final-report handoff

1. Transcribe verbatim notes before interpreting them.
2. Summarise each tester separately, then calculate counts and median task time.
3. Compare stage-one and stage-two rankings and flag any case where colour or
   placement changed the meaning.
4. List the three weakest design elements clearly enough that a reviewer can
   understand them without seeing the prototype.
5. Map every finding to an **accepted**, **modified**, or **rejected** change;
   explain the reason for any rejection.
6. Retest revised wording with a fresh order and preserve before/after evidence.

