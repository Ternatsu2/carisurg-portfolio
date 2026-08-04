# Completed HCI Co-Design Canvas

## Design question

How might a screen-based decision-support tool show an emergency triage nurse
a model's suggested ESI level without slowing the encounter, hiding data
quality problems, or replacing the nurse's judgement?

## Problem space

| Canvas area | Completed design decision |
| --- | --- |
| Setting | Mercer General emergency department triage workstation. The interaction begins after complaint and vital signs are recorded and ends when the nurse records a final ESI level. |
| Primary user | ED triage nurse. The nurse reviews the patient and data and owns the final ESI decision. |
| Secondary users | Charge nurse, ED clinician, Clinical IT, accessibility/patient-experience reviewer, and clinical governance. |
| User need | See whether the source data are complete, review a model suggestion in context, and record a defensible decision without duplicating intake work. |
| Clinical context | Noise, interruptions, queue pressure, glare, fatigue, night shifts, and unstable network or power. |
| System task | Pull reviewed intake values, request one shadow-mode ESI suggestion, present it beside the source values, and capture confirm or override. |
| Human task | Assess the patient, correct data, decide the final ESI, and escalate care through the existing clinical workflow. |

## Environment and form

- Existing desktop workstation inside the triage bay; no separate device is
  required for the first pilot.
- One active nurse per case. A charge nurse can review escalated or audited
  cases but cannot silently replace the original decision.
- Main type is at least 16 px, contrast meets WCAG 2.2 AA, and controls remain
  usable at 100% browser zoom under clinical lighting.
- Number and urgency text repeat every colour cue. Audio is limited to one
  high-acuity reminder because the emergency department is already noisy.
- The case summary, suggestion, and decision controls stay in one reading path.

## Inputs and interaction

1. Pull age, chief complaint, arrival mode, vital signs, glucose, and oxygen
   context from the EHR and connected monitors.
2. Show the source, collection time, and validation state for every value.
3. Let the nurse correct an imported value or switch to manual entry without
   erasing the original value from the audit record.
4. Block the model request when a required value is missing or invalid. A
   manual-triage path remains reachable within two actions.
5. Send only the nurse-reviewed feature set to the versioned model endpoint.
6. Return an ESI suggestion from 1 to 5 with a number, urgency label, and
   redundant colour cue.
7. Keep the complaint and reviewed values beside the suggestion. Do not invent
   a confidence score or causal explanation.
8. Require the nurse to confirm or override before a final ESI can be recorded.

## Behaviour and feedback loop

**Confirm:** The nurse accepts the suggestion as the nurse's final decision.

**Override:** The nurse selects a different ESI and records clinical judgement,
new information, a data-quality issue, or another reason. Both values remain
in the audit record.

**No action:** The suggestion remains pending. For ESI 1 or 2, the screen gives
one visual and audible reminder after 60 seconds and adds the case to a charge
nurse queue. It does not assign an ESI or trigger treatment.

**Correction:** The nurse can revise a decision until the encounter is closed.
The audit trail retains the earlier value, user, reason, and time.

## Ethical and safety decisions

| Risk | Design control | Residual risk and owner |
| --- | --- | --- |
| Under-triage or automation bias | Nurse ownership, source data visible, no auto-submit, immediate override, shadow-mode monitoring. | A suggestion can still anchor judgement. Clinical governance reviews disagreement and ESI 1 misses weekly during pilot. |
| Missing, stale, or incorrect data | Show source and time, block invalid requests, require review, retain original and corrected values. | A rushed user may confirm an incorrect value. Triage lead reviews data-quality overrides. |
| Alert fatigue | One high-acuity reminder; no repeated pop-ups or colour-only alerts. | A reminder can still be missed in a crowded bay. Charge nurse owns escalation review. |
| Clutter and input error | One reading path, grouped controls, spacing between destructive and primary actions, confirmation before record write. | Usability problems may appear on different displays. Clinical IT tests approved hardware. |
| Accessibility and language | Text plus colour, AA contrast, keyboard access, plain clinical labels, language review. | The first prototype does not cover every access need. Patient experience owns further testing. |
| Service outage | Clear unavailable state, no stale suggestion, entered data retained, manual workflow within two actions. | Wider EHR downtime can still limit documentation. Existing downtime policy applies. |

## Completed MVP boundary

The final Week 9 HCI artefact is a three-state visual prototype: review inputs,
review suggestion, and record a nurse decision. It is complete enough for
scenario testing but is not connected to an EHR, monitor, model endpoint, or
clinical record.

## Co-design test plan

- Two triage nurses from different shifts complete four scenarios: complete
  data, stale data, under-triage suggestion, and model outage.
- A charge nurse tests the pending high-acuity queue and audit record.
- Clinical IT tests display size, browser, EHR outage, retry, and authentication
  assumptions.
- An accessibility reviewer tests keyboard use, contrast, glare, and non-colour
  meaning.
- Governance reviews whether the suggestion should appear before or after the
  nurse records an unaided provisional ESI.

Success means every nurse can identify data provenance, reach manual triage
within two actions, override without assistance, and explain which value is
the model suggestion versus the final human decision.
