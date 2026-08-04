# Safety Considerations One-Pager

- **Scope:** HCI nurse workstation and optional stationary HRI intake assistant
**Deployment boundary:** Shadow-mode clinical pilot; humans retain all triage decisions

## Risk method

Risk is scored as likelihood (1 rare to 5 almost certain) multiplied by severity
(1 negligible to 5 catastrophic). Controls are layered because each control can
fail. Residual risk remains visible and has a named owner.

| Risk | Initial | Layered controls | Residual | Owner and trigger |
| --- | ---: | --- | ---: | --- |
| HCI under-triage or automation bias | 4 x 5 = **20** | Nurse decision owner; source data beside suggestion; no auto-write; immediate override; shadow monitoring; weekly ESI 1 review | 2 x 5 = **10** | Clinical governance. Pause for harm or threshold breach. |
| HCI stale, missing, or incorrect input | 4 x 4 = **16** | Source and time visible; required-field block; correction retains original; no display imputation; manual path within two actions | 2 x 4 = **8** | Triage lead and Clinical IT. Investigate repeated source failures. |
| HCI alarm fatigue, clutter, or miskey | 4 x 4 = **16** | One high-acuity reminder; grouped reading path; spaced controls; confirm before write; keyboard and glare testing | 2 x 4 = **8** | Clinical operations. Revise after usability failure or ignored alert pattern. |
| HRI infection transmission | 4 x 4 = **16** | Voice-first option; wipeable shell; cleaning status; cleaning log; overdue lockout; infection-control audit | 2 x 4 = **8** | Infection prevention. Quarantine after missed or failed cleaning. |
| HRI speech error, privacy loss, or excess trust | 4 x 4 = **16** | Push-to-talk; captions and read-back; patient correction; directional audio; minimum data; no ESI/diagnosis; "nurse decides" role statement | 2 x 4 = **8** | Patient experience and privacy. Pause for misleading handoff or disclosure. |
| HRI collision, power, network, or sensor failure | 3 x 5 = **15** | Stationary locked base; no arms/navigation; clearance zone; emergency stop; health checks; low-battery warning; nurse route; fail closed | 1 x 5 = **5** | Biomedical engineering. Lock out any failed safety control. |

## Five control layers

1. **Clinical boundary:** no autonomous ESI, diagnosis, treatment, or model-to-EHR write.
2. **Input protection:** provenance, time, validation, read-back, and correction.
3. **Human confirmation:** nurse confirm/override; patient consent, erase, decline, or call nurse.
4. **Technical fallback:** fail closed, no stale suggestion, manual path, device lockout.
5. **Monitoring and governance:** audit events, class and subgroup review, named pause triggers, residual-risk sign-off.

## Accessibility and inclusion

Number and text repeat every colour cue. The HCI supports keyboard use and AA
contrast. The HRI supports captions, touch, push-to-talk, adjustable screen and
volume, language choice, and immediate nurse or interpreter handoff.

## Residual-risk decision

No control removes the possibility of under-triage, a rushed confirmation,
overheard speech, or device failure. The first deployment therefore remains a
limited shadow-mode pilot. Clinical governance, Clinical IT, infection
prevention, biomedical engineering, and patient experience must accept their
assigned residual risks before use and can pause the pilot independently.
