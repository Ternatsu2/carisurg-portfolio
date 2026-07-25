# Emergency triage model handover

## Project summary

This project tests a clinician-facing model that estimates Emergency Severity
Index level from routine arrival information. The intended setting is a
shadow-mode review at Mercer General ED: a triage nurse can compare the model's
output with the recorded assessment, but the clinician retains the decision.
The current work is a technical prototype, not a clinical device.

## Final model decision

Use the tuned multinomial logistic regression with ESI 1 weighted at 8. It
caught 7 of 16 ESI 1 visits on the unchanged holdout, retained a macro F1 of
0.501, and gives Clinical IT a clearer explanation path than the tested tree
ensembles. The full trade-off is recorded in the
[decision journal](docs/decisions/2026-week-7-model-choice.md).

## How to run it

```bash
git clone https://github.com/Ternatsu2/carisurg-portfolio.git
cd carisurg-portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export CARISURG_TRIAGE_CSV=/approved/path/yaleemmlc_admissionprediction_triage.csv
python scripts/train.py --config config.yaml
pytest -q
```

The training command loads and validates the CSV, rebuilds the 209-feature
table, recreates the fixed split, checks its SHA-256 fingerprint, trains the
pinned model, and writes local model and metric files under `artifacts/`.

## Data and governance

The full programme CSV stays in approved private storage and is supplied
locally through `CARISURG_TRIAGE_CSV`. It is not committed or redistributed.
The public repository contains only the programme-provided two-row sample,
column schema, code, and aggregate results. Access to the full file should be
limited to authorised CariSurg reviewers and the designated Clinical IT or
data owner.

## Known limitations

- The data come from one Yale emergency department and have not been validated at Mercer General or another Caribbean ED.
- The holdout contains only 16 ESI 1 visits; 9 were missed, so the model is not suitable for autonomous triage.
- Nonnumeric workflow and demographic fields were excluded from this model, limiting local context and subgroup assessment.

## Who to ask

- **Model and repository:** Terry Benjamin Jr., project maintainer.
- **Clinical interpretation and ESI workflow:** the designated CariSurg clinical mentor or Mercer General ED clinical lead.
- **Data access and governance:** the CariSurg programme data custodian or the approved Clinical IT data owner.
