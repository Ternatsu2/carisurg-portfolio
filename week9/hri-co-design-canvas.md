# Completed HRI Co-Design Canvas

## Design question

How might a stationary embodied assistant help patients communicate their
reason for visiting the emergency department while protecting dignity,
preventing contamination, and making nurse handoff immediate?

## Problem space

| Canvas area | Completed design decision |
| --- | --- |
| Setting | A marked intake position inside the emergency department, visible to the triage desk but far enough from the waiting area to limit overhearing. |
| Primary users | Walk-in patients who choose to use the assistant and the triage nurse who reviews the captured draft. |
| Secondary users | Caregiver or interpreter, charge nurse, infection prevention, biomedical engineering, Clinical IT, accessibility/patient experience, and governance. |
| User need | Communicate a chief complaint and access needs through speech, touch, or a nurse-assisted path without believing the robot has diagnosed or triaged them. |
| System task | Obtain consent, capture a structured complaint and access preferences, validate the draft with the patient, and hand it to the triage queue. |
| Clinical boundary | The assistant does not assign or display ESI, diagnose, give treatment advice, navigate autonomously, or replace direct nurse assessment. |

## Environment and physical form

- Stationary 120 cm floor unit with a locked, high-visibility base. There is no
  autonomous navigation during the pilot, removing collision and route-planning
  risks from the interaction.
- Wipeable non-porous shell with few seams, a replaceable screen protector, and
  a visible cleaning-status indicator.
- Adjustable 15-inch high-contrast touch display, microphone array, directional
  speaker, camera shuttered off by default, and a large physical "Call nurse"
  button. No human face, simulated breathing, arms, or emotional claims.
- Volume and screen angle support seated and standing users. Meaning is repeated
  in speech, text, icons, and tactile controls rather than relying on one mode.
- A physical emergency stop and power-isolation switch are reachable by staff.

## Interaction and behaviour

1. The assistant states its purpose: collect a draft for a nurse, not diagnose
   or decide urgency.
2. The patient chooses to continue, decline, or call a nurse. Declining causes
   no delay or loss of queue position.
3. The patient chooses language and input mode: touch, push-to-talk speech, or
   nurse-assisted entry. Captions remain visible during speech interaction.
4. The assistant asks one short question at a time and shows a progress marker.
5. A captured answer is read back and displayed for correction. Low-quality
   speech or conflicting answers trigger clarification, not silent guessing.
6. Before handoff, the patient reviews a plain-language summary and can change
   or erase it.
7. The assistant sends the consent state, complaint draft, access preferences,
   input mode, timestamps, and device-health state to the triage queue.
8. A nurse receives the draft, assesses the patient, and decides whether to use
   any information. The model and final ESI workflow remain nurse-facing.

## Social behaviour

The assistant is calm, concise, and transparent. It uses neutral acknowledgments
such as "I have recorded that" rather than "I understand how you feel." It does
not use jokes, emojis, or simulated empathy in an urgent setting. It tells the
patient when it cannot hear or connect and offers a nurse immediately.

## Ethical and safety decisions

| Risk | Design control | Residual risk and owner |
| --- | --- | --- |
| Patient mistakes the robot for a clinician | Repeated role statement, no ESI or diagnosis display, visible "Assistant - nurse decides" label. | Embodiment may still create excess trust. Patient-experience and governance teams review comprehension. |
| Infection transmission | Voice-first option, cleaning status, wipeable surfaces, cleaning log, blocked use when cleaning is overdue. | Cleaning may be recorded without being completed. Infection prevention audits the process. |
| Speech recognition error in ED noise | Push-to-talk, captions, answer read-back, explicit correction, confidence used only to request clarification. | A patient may confirm an incorrect draft. The nurse treats it as unverified information. |
| Privacy or overhearing | Directional speaker, headset option, privacy position, camera off, minimum necessary data, erase-before-send. | Speech can still be overheard. Clinical operations owns placement and privacy checks. |
| Physical collision, tip, or obstruction | Stationary locked base, marked clearance zone, rounded edges, no moving arms, staff emergency stop. | The unit can still obstruct evacuation or be struck. Facilities and biomedical engineering inspect placement. |
| Power, network, or sensor degradation | Health check, low-battery warning, fail-closed handoff, no stale response, immediate nurse route. | Failure can add frustration or delay. Triage lead monitors abandonment and downtime. |
| Accessibility or language mismatch | Multimodal input, captions, adjustable display, plain language, interpreter and nurse path. | Supported modes may remain incomplete. Accessibility review continues before pilot expansion. |

## Completed MVP boundary

The final Week 9 HRI artefact is a three-state visual prototype: consent and
access choice, multimodal complaint capture, and nurse handoff/degraded mode.
It represents physical form and behaviour but does not claim a working speech
model, robot, device connection, or clinical integration.

## Co-design test plan

- Patients and caregivers complete the flow with touch, speech, refusal, noisy
  audio, and nurse-call scenarios.
- Triage nurses inspect the handoff draft and identify that it is unverified.
- Infection prevention tests cleaning steps and overdue-cleaning lockout.
- Biomedical engineering tests stability, emergency stop, power loss, speaker,
  microphone, and device-health reporting.
- Accessibility and language reviewers test captions, screen height, contrast,
  plain language, and interpreter handoff.

Success means users can explain that a nurse still decides urgency, decline or
call a nurse without assistance, correct the captured draft, and complete the
interaction without exposing more information than necessary.
