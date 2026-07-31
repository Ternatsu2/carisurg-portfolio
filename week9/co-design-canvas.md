# Draft Co-Design Canvas

## Design question

How might a screen-based decision-support tool show an emergency triage nurse
a model's suggested ESI level without slowing the encounter or replacing the
nurse's judgement?

## Where and when

| Canvas area | Draft decision |
| --- | --- |
| Where is it used? | At the Mercer General ED triage desk, on the workstation already used for intake. |
| When is it used? | After the initial complaint and vital signs are recorded, before the nurse finalises the ESI level. |
| What changes by context? | Noise, interruptions, queue pressure, night shifts, power or network instability, and missing device data can all affect use. |
| Simultaneous users | One nurse enters or reviews a case at a time. A charge nurse may review an escalation or audit record. |

## Users

**Primary user:** ED triage nurse. The nurse reviews the patient, checks the
record, and owns the final ESI decision.

**Secondary users:** Charge nurse for escalation and audit; Clinical IT for
integration and support; governance staff for monitoring overrides and model
performance. The patient is affected by the result but does not operate this
screen in the first prototype.

## User goal and current task

The nurse needs to identify acuity quickly, see whether the available data are
complete, and record a defensible ESI level. Today the nurse gathers the chief
complaint and vital signs, applies the triage process, and documents the final
decision in the clinical record.

The proposed screen adds one review step. It shows a model suggestion beside
the source data, then asks the nurse to confirm or override it. It never
completes triage on its own.

## System mode and behaviour

| Area | Draft choice |
| --- | --- |
| Form factor | HCI screen at the triage workstation, not a social robot. |
| Mode of operation | Nurse-controlled. The model produces a suggestion only after the nurse has reviewed the inputs. |
| Tone | Short, clinical, and neutral. No conversational personality or reassurance language. |
| Attention | Use a number, text label, and colour together. Avoid colour-only meaning. |
| Human action | Review the inputs and suggestion, then confirm or override. |
| Disagreement | Capture a reason, keep both values in the audit record, and allow correction before the encounter is closed. |
| No action | Leave the suggestion pending. A high-acuity suggestion produces a second reminder and alerts the charge-nurse queue after 60 seconds, but the system does not assign an ESI level. |

## Information flow

1. Pull the latest intake values from the EHR.
2. Show each value's source and collection time.
3. Let the nurse correct a value or switch to manual entry.
4. Block the model request if a required value is missing or invalid.
5. Send the reviewed values to the current shadow-mode model.
6. Return a suggested ESI level with a text and colour cue.
7. Ask the nurse to confirm or override.
8. Record the final human decision, model suggestion, reason, user, and time.
9. Use aggregate override and error patterns as feedback for later review.

## Safety review

| Concern | Context | Mitigation in the draft | Residual risk |
| --- | --- | --- | --- |
| Under-triage | A critical patient may receive a lower-acuity suggestion, especially because the held-out ESI 1 sample is small. | Keep the nurse as decision owner, show the source values, allow immediate override, and never auto-submit. | The suggestion may still anchor the nurse's judgement. Prospective shadow-mode review remains necessary. |
| Alert fatigue | Repeated or poorly targeted warnings during a busy shift may be ignored. | Reserve the strongest visual and audible alert for high-acuity suggestions or missing critical inputs. Use one timed reminder rather than repeated pop-ups. | Even a limited alert can be missed during a crowded shift. |
| Data quality or device failure | An old EHR value, dropped device stream, or transcription error could change the suggestion. | Show source and time, flag stale or missing values, and provide manual correction. Do not infer a missing value. | A nurse may confirm an incorrect value under time pressure. |
| Interface clutter | Too many panels can slow review or hide the action needed. | Keep the case summary, suggestion, and decision controls in one reading path. Move technical detail out of the primary view. | Users may need different information density depending on experience. |
| Accessibility | Colour, small text, glare, or language can make the screen harder to read. | Pair colour with a number and label, use high contrast, keep type at least 16 px, and avoid meaning carried by icons alone. | The draft still needs review with users who have visual or language-access needs. |
| Service outage | The model or network may be unavailable during intake. | Show an unavailable state and return the nurse to the existing manual triage process without losing entered values. | The audit trail may be incomplete if the wider EHR is also unavailable. |

## People to include in the next review

- Two triage nurses from different shifts
- One charge nurse
- One ED clinician
- One Clinical IT or EHR integration representative
- One accessibility or patient-experience representative
- One governance or safety reviewer

## Questions for co-design

1. Which values must stay visible while the nurse reviews the suggestion?
2. Should the model suggestion appear before or after the nurse records an
   initial judgement?
3. Which override reasons match the language nurses already use?
4. Is a 60-second high-acuity reminder useful, too slow, or distracting?
5. What should the screen do when only one vital sign is stale?
6. Which users may reverse a decision, and until what point in the encounter?
7. What information would help a nurse challenge the model without implying a
   causal explanation the model cannot support?

## Assumptions to validate

- The triage workstation can read the required intake fields from the EHR.
- Nurses can correct imported values without duplicating the whole intake.
- A charge-nurse queue exists or can receive an escalation.
- The audit record can store the model suggestion separately from the final
  human decision.
- The final interface should remain useful when the model is unavailable.
