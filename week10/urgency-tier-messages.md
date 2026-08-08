# Draft Urgency-Tier Messages

The four messages are written for a triage nurse looking at the patient queue.
They describe the required **review action**, not a diagnosis or treatment.
The response-time wording is part of the prototype and requires clinical
validation before any real deployment.

| Tier | Primary alert | Words | Intended reading |
| --- | --- | ---: | --- |
| **Critical** | **Start immediate clinical assessment now.** | 5 | Stop the normal queue sequence and assess immediately. |
| **High** | **Assess this patient within ten minutes.** | 6 | Prioritise the patient for prompt assessment below the critical tier. |
| **Medium** | **Recheck this patient within thirty minutes.** | 6 | Keep the patient visible and complete a planned reassessment. |
| **Low** | **Review this patient during the next queue check.** | 8 | Continue standard monitoring without an interruptive alarm. |

## Wording check

- Each alert is twelve words or fewer; the longest is eight words.
- Each uses an active verb: **start, assess, recheck, review**.
- The linguistic register changes with urgency instead of relying on an
  adverb or colour alone.
- The primary alert contains no abbreviations such as ESI, SpO2, BP, or GCS.
- The action is first. Supporting details such as suggested ESI, wait time,
  vital signs, data source, and model status appear below the message.

## Redundant cues in the prototype

| Tier | Text label | Symbol | Colour role | Sound behaviour |
| --- | --- | --- | --- | --- |
| Critical | CRITICAL | Double exclamation | Dark red border and banner | Repeating alert in a validated deployment; mute must be auditable. |
| High | HIGH | Up arrow | Burnt orange border and banner | Single attention tone after local validation. |
| Medium | MEDIUM | Clock | Ochre border and banner | Visual cue only by default. |
| Low | LOW | Queue dot | Green border and label | Silent; remains in the normal queue. |

Sound is a proposed secondary cue, not part of the static prototype. It cannot
become the only way to detect an alert.

## Words-only safety test

The peer test begins with the four primary messages as plain black text. There
are no labels, icons, colours, patient details, or fixed order. A tester ranks
them from highest to lowest urgency and explains the ranking aloud. If the
language does not produce the intended order, the wording is revised before
visual styling is treated as successful.

