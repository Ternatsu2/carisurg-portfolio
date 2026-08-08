# Week 10: Interim Deliverable

**Student:** Terry Benjamin Jr.  
**Programme:** CariSurg MedTech Pathways  
**Date:** 8 August 2026

## Submission scope

This interim package extends the Week 9 nurse-facing emergency-triage
workstation. It tests how four levels of urgency can be communicated without
letting colour, the model, or the interface replace clinical judgement.

The model remains in shadow mode. A triage nurse reviews the source data,
owns the final ESI decision, and can confirm or override the suggestion. The
prototype uses fictional records and is not a clinical tool.

## Rubric evidence

| Rubric area | Evidence |
| --- | --- |
| Draft Urgency-Tier Messages (4 Tiers) | [Four primary messages and rationale](urgency-tier-messages.md). Every message is active, plain English, and eight words or fewer. |
| Initial Prototype Sketches | [Queue and alert workflow](prototype/queue-and-alert.png) and [four urgency states](prototype/urgency-tier-states.png). The inspectable HTML sources sit beside both images. |
| Accessibility Considerations One-Pager | [Rendered one-pager](accessibility-one-pager.png) and [text version](accessibility-one-pager.md). |
| Peer-Testing Plan | [Structured peer-testing plan](peer-testing-plan.md) with recruitment, facilitator script, two-stage urgency test, tasks, measures, accessibility checks, and data handling. |

## Design decisions carried forward

- The primary alert states the action first and keeps the wording under twelve
  words. Supporting clinical context is secondary.
- Urgency is repeated through words, tier label, symbol, placement, and colour.
  The interface still has to work in greyscale.
- The queue stays neutral until a status needs attention. Colour is reserved
  for urgency and does not decorate the base interface.
- The prototype never presents model confidence because the current model does
  not provide a calibrated patient-level confidence score.
- The nurse can inspect inputs, work manually during an outage, and record a
  reason when overriding a model suggestion.

## Interim boundary

This submission contains a **testing plan**, not invented testing results. The
Week 10 final will report testing with at least three cohort peers, compare the
words-only and full-interface stages, preserve verbatim feedback, and connect
every finding to an accepted, modified, or rejected design change.

