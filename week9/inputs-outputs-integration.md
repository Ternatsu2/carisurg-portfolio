# Inputs and Outputs Integration Notes

## Selected setting

I selected an HCI screen for the Mercer General ED triage desk. The triage
nurse is the primary user. The current model remains a shadow-mode comparator,
and the nurse owns the final ESI decision.

## Input route

The normal route is an EHR pull. Each imported field shows its source and
collection time. The nurse can correct a value or use manual entry when the EHR
interface or a connected device is unavailable.

I did not choose a continuous device stream for the first prototype. It would
create extra timing, reconciliation, and outage questions before the basic
nurse-review flow has been tested. The interface still records whether a value
came from the EHR, a device, or manual entry so that a device stream can be
tested later without changing the audit structure.

### Values presented for review

- encounter identifier, with no patient name in the prototype
- age
- chief complaint
- arrival mode
- pulse
- systolic and diastolic blood pressure
- respiratory rate
- oxygen saturation
- temperature
- glucose
- oxygen device or room-air status
- source, collection time, and validation state for each value

The source pipeline may use additional encoded features. The screen shows the
clinical values a nurse can recognise and check instead of exposing the model's
encoded columns.

## Validation before the model request

- Required empty fields appear in a single missing-input list.
- A stale value is shown with its recorded time and needs nurse confirmation.
- The nurse can correct a value without replacing the original source in the
  audit record.
- The interface does not guess or impute a value for display.
- If the required review is incomplete, the model action stays disabled and
  the nurse can continue the normal manual workflow.

## Model output

The model returns one suggested ESI level from 1 to 5. The interface shows:

- the numeric ESI level
- a plain-language urgency label
- a colour cue that repeats, rather than replaces, the number and label
- the reviewed vital signs and complaint beside the suggestion
- a clear "decision support only" status

The current model does not provide a calibrated patient-level confidence
score, so the mock-up does not invent one. It also avoids causal language. The
display can say which values were supplied to the model, but it should not say
that a single vital sign caused the prediction.

## Human action

The nurse must choose one of two paths:

1. **Confirm:** record the suggested ESI as the nurse's final decision.
2. **Override:** select the nurse's ESI level and give a reason. Draft reasons
   are clinical judgement, new information, data quality issue, and other.

Both paths record the nurse, time, model suggestion, final ESI, data version,
and any override reason. The nurse can revise the decision before closing the
encounter; the audit keeps the earlier entry.

## No-action path

A model suggestion remains pending until a nurse responds. For a suggested ESI
1 or 2, the screen gives one additional visual and audible reminder after 60
seconds and adds the case to a charge-nurse review queue. It does not write a
final ESI or start a treatment action automatically.

The reminder timing and escalation route are draft choices for nurse review.

## Degraded mode

| Failure | Screen response | Clinical path |
| --- | --- | --- |
| EHR pull unavailable | Keep entered values, show "EHR unavailable," and unlock manual entry. | Nurse continues the standard intake. |
| Required value missing | Name the missing field and keep the model action disabled. | Nurse measures or records the value, or continues without model support. |
| Model endpoint unavailable | Show "Model unavailable" without a stale suggestion. | Nurse completes normal triage and documents the final ESI. |
| Audit write fails | Keep the decision visible as unsaved and retry locally; do not present it as recorded. | Nurse follows the existing downtime documentation process. |

## Integration boundary

The first implementation needs four interfaces:

1. **EHR read:** fetch the current encounter and reviewed intake values.
2. **Model request:** send the approved feature set with model and schema
   versions.
3. **Decision write:** write the nurse's final ESI through the authorised EHR
   workflow, not directly from the model response.
4. **Audit write:** store the model suggestion, final human decision, override
   reason, user, times, data source, and version identifiers.

The prototype in this interim is visual only. These notes define what would
have to connect before a later implementation or shadow-mode pilot.
