# CariSurg Portfolio

Portfolio work for the CariSurg MedTech Pathways Healthcare AI programme.

## What This Is

This repository collects my CariSurg technical work, starting with emergency triage data cleaning, visualisation, and research writing. The project direction is clinician-facing support for emergency triage, with the final decision kept with the nurse or clinician.

## Who It Is For

The main audience is CariSurg tutors and clinical or technical reviewers who want to see the work behind my submissions without digging through separate files. It should also be readable for someone reviewing my healthcare AI portfolio later.

## Current Week 6 Submission

The Week 6 interim submission builds reproducible baseline models for the emergency triage dataset:

- `notebooks/week6_interim_baseline_models.ipynb`: dummy, logistic-regression, and depth-5 decision-tree baselines.
- `docs/w6_initial_metrics.csv`: accuracy, macro F1, weighted F1, and ESI 1 recall.
- `docs/w6_confusion_logreg.png`: the main interim confusion-matrix artefact.
- `docs/w6_confusion_tree.png`: an additional comparison for the second baseline.

The notebook uses an 80/20 split stratified on `esi` and a fixed random seed of 42. I treat recall for ESI 1 as the primary safety measure because a false negative in that class could delay immediate intervention.

## Repository Layout

- `notebooks/`: Jupyter notebooks for the technical work.
- `docs/`: memos, reports, plots, and supporting tables.
- `data/`: placeholder folder for small programme data files. Real patient data should not be committed here.
- `week0/`: original Week 0 submission folders and report outputs.
- `week1/`: original Week 1 submission folders.
- `week5/`: Week 5 triage data exploration and feasibility package.

## Setup

The notebooks use Python 3 with pandas, numpy, matplotlib, seaborn, and scikit-learn.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The full programme CSV is not stored in GitHub. Set its local path before running the Week 6 notebook:

```bash
export CARISURG_TRIAGE_CSV=/path/to/yaleemmlc_admissionprediction_triage.csv
jupyter notebook notebooks/week6_interim_baseline_models.ipynb
```

In Google Colab, upload or mount the same CSV, then set `CARISURG_TRIAGE_CSV` to that path.

## Data Note

The Week 5 and Week 6 analyses use the TenX file `yaleemmlc_admissionprediction_triage.csv`. I did not commit the full CSV because it is a large clinical dataset. The repo includes a sample and schema under `week5/data/` so reviewers can inspect the structure without storing the full file here.

## Contact

Terry Benjamin Jr.  
St. John's, Antigua and Barbuda  
LinkedIn: <https://www.linkedin.com/in/terry-benjamin-jr-274434116/>
