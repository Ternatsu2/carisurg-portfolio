# Week 9: Final Deliverable

**Student:** Terry Benjamin Jr.  
**Programme:** CariSurg MedTech Pathways  
**Date:** 4 August 2026

## Project position

This package turns the emergency-triage model into two deliberately different
human-AI interaction concepts. The HCI concept is a nurse-facing workstation
that presents a shadow-mode ESI suggestion for confirmation or override. The
HRI concept is a stationary, sanitizable intake assistant that helps a patient
give a complaint and accessibility preferences before handing the record to a
nurse. Neither concept assigns a final ESI level or starts treatment.

All patient details are fictional. The mock-ups are design artefacts rather
than clinically validated software or a live robot.

## Rubric evidence

| Rubric area | Evidence |
| --- | --- |
| Completed Co-Design Canvases (HCI + HRI) | [HCI canvas](co-design-canvas.png) and [detailed HCI notes](co-design-canvas.md); [HRI canvas](hri-co-design-canvas.png) and [detailed HRI notes](hri-co-design-canvas.md). Inspectable HTML sources are committed beside both images. |
| Two Mock-Ups (HCI + HRI) | [Nurse-facing HCI workflow](mockups/triage-review.png) covers input review, model suggestion, and confirm/override. [Embodied HRI workflow](mockups/hri-intake-assistant.png) covers consent, multimodal intake, nurse handoff, and degraded mode. |
| Deployment System Requirements Document | [Deployment requirements](deployment-system-requirements.md) define scope, architecture, functional, non-functional, integration, data, security, fallback, verification, and pilot exit criteria. |
| Safety Considerations One-Pager | [Safety one-pager](safety-one-pager.png) applies likelihood and severity scoring, layered controls, HCI and HRI risks, and residual-risk ownership. The [text version](safety-one-pager.md) provides the complete register. |
| Walk-Through Video & Repo Placement | [Week 9 walkthrough video](walkthrough/week9-final-walkthrough.mp4) explains the context, both designs, deployment boundary, and safety controls. The [walkthrough transcript](walkthrough/transcript.md) is committed for accessibility. |

## Key design decisions

- The triage nurse owns the final ESI decision. The model remains decision
  support only and never writes directly to the clinical record.
- The workstation shows source and collection time for each input, blocks a
  model request when required data are missing, and keeps manual triage
  available during outages.
- Output meaning is repeated through number, label, placement, and colour.
- The current model has no calibrated patient-level confidence score, so the
  interface does not invent one or claim a causal explanation.
- The HRI assistant is stationary during use. It has no autonomous navigation,
  diagnosis, ESI display, medication, or treatment capability.
- A patient can decline the robot, change language or input mode, erase the
  draft, or summon a nurse at any point.
- Both designs keep an auditable distinction between imported data, user
  corrections, model suggestion, and final human decision.

## Deployment boundary

The first deployment is a limited shadow-mode pilot. It requires EHR read,
model request, authorised decision write, audit write, identity, and charge
nurse escalation interfaces. The HRI concept adds device health, microphone,
screen, physical emergency stop, cleaning status, and privacy controls.

No deployment proceeds until triage nurses complete scenario-based usability
testing, Clinical IT verifies interface and downtime behaviour, and clinical
governance accepts the residual risk documented in this folder.
