# Week 9 Final Walkthrough Transcript

## Opening

This Week 9 design asks a practical question: how can the emergency-triage
model support a real encounter without hiding uncertainty or taking the final
decision away from the nurse? I developed two interaction concepts around the
same clinical boundary. The first is a nurse-facing computer interface. The
second is a stationary embodied assistant for optional patient intake. Both are
prototypes, and neither diagnoses, assigns a final ESI, or starts treatment.

## HCI co-design canvas

The HCI design sits on the workstation already used at the triage desk. It
pulls the complaint and vital signs, but the nurse sees the source and time for
every value before the model runs. Missing required data block the request,
and manual triage stays within two actions. The model returns one ESI
suggestion with a number, urgency label, and colour. I do not show a confidence
score because the current model does not provide a calibrated one. The nurse
must confirm or override, and the audit keeps the model value, human value,
reason, user, and time.

## HRI co-design canvas

The HRI design solves a different interaction problem. It is an optional,
stationary intake assistant that helps a walk-in patient give a complaint and
access preferences before nurse assessment. It has a locked base, wipeable
surfaces, an adjustable screen, push-to-talk audio, captions, a physical nurse
call, and an emergency stop. It does not move, show ESI, or claim empathy. A
patient can decline it, erase a draft, or summon a nurse at any point. The
output is clearly marked as an unverified draft for the nurse, not model-ready
clinical truth.

## HCI mock-up

The HCI mock-up shows the complete nurse workflow. The first state is input
review. Imported and manual values are visibly different, and oxygen context
stays beside saturation. The second state places the model suggestion next to
the reviewed data and says that nurse review is required. The third state
shows an override from ESI 2 to ESI 1 after the patient's condition changes.
The nurse records a reason and note before writing the decision. This makes the
disagreement useful for audit and later model review without turning the model
into the decision maker.

## HRI mock-up

The HRI mock-up starts with role clarity and consent. The patient sees that the
device is an assistant and that a nurse decides. The next state uses one short
question, push-to-talk, a visible caption, and explicit confirmation rather
than silently trusting speech recognition in a noisy emergency department.
The final state shows the patient-reviewed complaint, access needs, cleaning
status, and device health before handoff. The draft is not sent to the model.
If the network or device fails, the system avoids a stale handoff and directs
the patient to the normal desk.

## Deployment requirements

The deployment document turns the mock-ups into testable requirements. The
system needs authorised EHR read, a versioned model request, nurse-controlled
decision write, audit storage, identity, and a charge-nurse queue. Functional
requirements cover provenance, validation, confirm and override, no-action,
correction, consent, and HRI health checks. Non-functional requirements cover
latency, accessibility, security, privacy, auditability, physical safety, and
infection control. The model endpoint has no permission to write a final ESI.
The first deployment remains shadow mode, with fault injection and usability
testing before any pilot expansion.

## Safety and close

The safety one-pager scores likelihood and severity before and after controls.
The highest concerns are under-triage, bad source data, alert fatigue,
infection, speech or privacy errors, and physical or technical HRI failure. I
used five layers: the clinical boundary, input protection, human confirmation,
technical fallback, and monitoring with named owners and pause triggers. Some
risk remains even after those controls. That residual risk must be accepted by
clinical governance, Clinical IT, infection prevention, biomedical
engineering, and patient experience before a limited pilot. The complete
canvases, mock-ups, requirements, safety page, and this walkthrough are all in
the Week 9 folder so the design can be reviewed as one traceable package.
