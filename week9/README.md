# Week 9: Interim Deliverable

**Student:** Terry Benjamin Jr.  
**Programme:** CariSurg MedTech Pathways  
**Date:** 1 August 2026

## Design direction

I chose a screen-based HCI design for the emergency triage desk. The primary
user is the triage nurse. The model remains in shadow mode and offers a
suggested ESI level for review; it does not write the final triage decision.

For the prototype, the normal data route is an EHR pull with source and time
shown beside each field. The nurse can correct a value or enter it manually
when an interface or device feed is unavailable. Required missing values stop
the model request and leave the normal clinical workflow available.

## Rubric map

| Rubric area | Evidence |
| --- | --- |
| Draft Co-Design Canvas | [Rendered canvas](co-design-canvas.png) gives the one-page design view. [Detailed canvas notes](co-design-canvas.md) record the setting, users, task, system mode, interaction, safety concerns, open questions, and people needed for review. The [HTML source](co-design-canvas.html) is also committed. |
| Initial Mock-Up Sketches | [Three-screen mock-up](mockups/triage-review.png) covers input review, the model suggestion, and nurse confirmation or override. The [HTML source](mockups/triage-review.html) keeps the layout inspectable. |
| Inputs/Outputs Integration Notes | [Integration notes](inputs-outputs-integration.md) commit to the input route, required fields, output format, human action, no-action path, and degraded mode. |
| Repo Discipline & Committed Artefacts | Week 9 work is contained in this folder. The mock-up source and rendered image are both committed, and the existing model pipeline remains unchanged. |

## Prototype boundary

The mock-up uses a fictional patient record. It does not connect to an EHR,
monitoring device, or live model endpoint. Its purpose is to make the proposed
workflow concrete enough for nurses and technical reviewers to challenge
before implementation.

## Decisions carried into the mock-up

- The nurse sees the ESI suggestion as a number, text label, and colour cue.
- The screen keeps the patient's vital signs and data provenance beside the
  suggestion so the nurse can review the evidence in one place.
- The nurse must confirm or override before any final ESI value is recorded.
- An override requires a reason and is logged, visible, and reversible.
- Missing required inputs block the model request instead of silently filling
  a value.
- If the model service is unavailable, the nurse continues manual triage.

These are draft choices for co-design review, not a claim that the interface
has been clinically validated.
