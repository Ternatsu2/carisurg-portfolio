# CariSurg Portfolio

Portfolio work for the CariSurg MedTech Pathways Healthcare AI programme.

## What This Is

This repository collects my CariSurg technical work, starting with emergency triage data cleaning, visualisation, and research writing. The project direction is clinician-facing support for emergency triage, with the final decision kept with the nurse or clinician.

## Who It Is For

The main audience is CariSurg tutors and clinical or technical reviewers who want to see the work behind my submissions without digging through separate files. It should also be readable for someone reviewing my healthcare AI portfolio later.

## Current Week 9 Interim

[Open the Week 9 interim submission](week9/README.md).

The Week 9 interim moves the selected triage model into an initial nurse-facing
HCI design. The submission includes a draft co-design canvas, three linked
mock-up states, and integration notes that define the selected data route,
output format, human action, override path, and degraded mode.

## Current Week 8 Final

[Open the Week 8 final submission](docs/week-8-final.md).

The Week 8 final turns the selected Week 7 model into a reproducible
command-line pipeline while keeping the notebooks as the exploration record:

- `src/data.py`: CSV loading, schema checks, and the fixed stratified split.
- `src/features.py`: the Week 6 feature selection and Week 7 clinical feature functions.
- `src/model.py`: construction and evaluation of the pinned tuned logistic model.
- `config.yaml`: the exact seed, split fingerprint, feature settings, and hyperparameters.
- `scripts/train.py`: one entry point for loading, training, evaluation, and local artefacts.
- `tests/test_pipeline.py`: the data-contract and 50-row training smoke checks.
- `docs/model-selection.md`: the complete Week 6 and Week 7 model audit table.
- `HANDOVER.md`: the one-page project handover.
- `.github/workflows/tests.yml`: the same two checks run on pushes and pull requests.

The refactored command reproduces the recorded holdout result exactly: accuracy
`0.680544`, macro F1 `0.500879`, and ESI 1 recall of 7 out of 16 visits.

## Current Week 7 Submission

[Open the Week 7 final submission wrapper](docs/week-7-submission.md).

The final compares the reproduced Week 6 tuned logistic model with cross-validated
Random Forest and histogram gradient-boosting models on the unchanged holdout:

- `notebooks/week7_final_model_tradeoff.ipynb`: feature engineering, training-only
  tuning, seven-dimension benchmark, interpretability review, and ESI 1 error analysis.
- `docs/week-7-cost-benefit.pdf`: three-page memo for the ED Board and Clinical IT.
- `docs/week-7-cost-benefit.md`: accessible source for the same memo.
- `docs/decisions/2026-week-7-model-choice.md`: dated decision journal.
- `docs/week7_final_benchmark.md`: compact benchmark and recommendation.
- `docs/week7_final_benchmark.csv`: machine-readable scores, timing, and ESI 1 counts.
- `docs/week7_final_model_comparison.png`: macro F1, ESI 1 recall, and inference cost.
- `docs/week7_final_confusion_comparison.png`: held-out confusion matrices.
- `docs/week7_final_esi1_complaints.png`: aggregate complaint patterns in ESI 1 errors.

The tuned logistic model remains the Phase 3 shadow-mode candidate. It caught 7 of
16 held-out ESI 1 visits, compared with 6 for tuned gradient boosting and 5 for the
tuned Random Forest, while retaining the strongest macro F1 and the clearest
patient-level explanation path. None of the models is suitable for autonomous triage.

## Week 6 Baseline

The Week 6 final submission compares the required baselines and a small training-only tuning pass for the emergency triage dataset:

- `notebooks/week6_final_baseline_models.ipynb`: baseline models, validation-only tuning, held-out evaluation, and ESI 1 error review.
- `docs/week-6-baseline.pdf`: the three-page final report with the benchmark, tuning result, metric choice, and failure-mode reflection.
- `docs/w6_final_metrics.csv`: aggregate scores and ESI 1 alert counts for the dummy, baseline, and tuned models.
- `docs/w6_per_class_metrics.csv`: precision, recall, and F1 for each ESI class.
- `docs/w6_tuning_results.csv`: the settings tested on the inner validation split.
- `docs/w6_esi1_vital_profile.csv` and `docs/w6_esi1_complaint_profile.csv`: aggregate review of the held-out ESI 1 cases.
- `docs/w6_confusion_logreg_tuned.png` and `docs/w6_confusion_tree_tuned.png`: tuned-model test-set confusion matrices.
- `docs/week6_clinical_explainer.mp4`: the one-minute clinician-facing explanation.

The notebook uses an 80/20 split stratified on `esi` and a fixed random seed of 42. I treat recall for ESI 1 as the primary safety measure because a false negative in that class could delay immediate intervention.

The original logistic model identified 4 of the 16 ESI 1 visits. After I selected an ESI 1 class weight on an inner validation split, it identified 7 of 16 while test accuracy stayed near 68%. False ESI 1 alerts rose from 4 to 23, so the tuned result is still exploratory rather than clinically usable.

## Repository Layout

- `notebooks/`: Jupyter notebooks for the technical work.
- `docs/`: memos, reports, plots, and supporting tables.
- `src/`: reusable loading, feature, and model modules.
- `scripts/`: command-line entry points.
- `tests/`: fast data-contract and training checks.
- `config.yaml`: the pinned Week 8 training configuration.
- `HANDOVER.md`: the concise project handover.
- `data/`: placeholder folder for small programme data files. Real patient data should not be committed here.
- `week0/`: original Week 0 submission folders and report outputs.
- `week1/`: original Week 1 submission folders.
- `week5/`: Week 5 triage data exploration and feasibility package.

## Setup

The project uses Python 3.9 or newer with exact dependency versions pinned in
`requirements.txt`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The full programme CSV is not stored in GitHub. Set its approved local path,
then run the pinned Week 8 pipeline:

```bash
export CARISURG_TRIAGE_CSV=/path/to/yaleemmlc_admissionprediction_triage.csv
python scripts/train.py --config config.yaml
pytest -q
```

The executed Week 6 and Week 7 notebooks remain under `notebooks/` for audit
and further exploration.

## Data Note

The Week 5, Week 6, and Week 7 analyses use the TenX file
`yaleemmlc_admissionprediction_triage.csv`. I did not commit the full CSV because
it is a large clinical dataset. The repo includes a sample and schema under
`week5/data/` so reviewers can inspect the structure without storing the full file
here.

## Contact

Terry Benjamin Jr.  
St. John's, Antigua and Barbuda  
LinkedIn: <https://www.linkedin.com/in/terry-jr-benjamin-274434116/>
