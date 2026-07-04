# CariSurg Portfolio

Portfolio work for the CariSurg MedTech Pathways Healthcare AI programme.

## What This Is

This repository collects my CariSurg technical work, starting with emergency triage data cleaning, visualisation, and research writing. The project direction is clinician-facing support for emergency triage, with the final decision kept with the nurse or clinician.

## Who It Is For

The main audience is CariSurg tutors and clinical or technical reviewers who want to see the work behind my submissions without digging through separate files. It should also be readable for someone reviewing my healthcare AI portfolio later.

## Current Week 5 Submission

The Week 5 final submission is the AI-assisted triage data exploration package:

- `notebooks/week5_final_triage_profile.ipynb`: full exploration notebook.
- `docs/week5_feasibility_memo.md`: feasibility memo for the ED Board.
- `docs/week5_top10_feature_shortlist.csv`: ranked feature shortlist.
- `docs/week5_data_quality_dashboard.svg`: four-plot data quality dashboard.
- `docs/week5_missingness_summary.csv`: missingness table.
- `week5/`: mirrored Week 5 folder with sample data, schema, reports, and plots.

## Repository Layout

- `notebooks/`: Jupyter notebooks for the technical work.
- `docs/`: memos, reports, plots, and supporting tables.
- `data/`: placeholder folder for small programme data files. Real patient data should not be committed here.
- `week0/`: original Week 0 submission folders and report outputs.
- `week1/`: original Week 1 submission folders.
- `week5/`: Week 5 triage data exploration and feasibility package.

## Setup

The notebooks use Python 3 with pandas, numpy, and matplotlib.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you are using Google Colab, upload or mount the dataset in the path expected by the notebook before running the cells.

## Data Note

The Week 5 analysis used the TenX file `yaleemmlc_admissionprediction_triage.csv`. I did not commit the full CSV because it is a large clinical dataset. The repo includes a sample and schema under `week5/data/` so reviewers can inspect the structure without storing the full file here.

## Contact

Terry Benjamin Jr.  
St. John's, Antigua and Barbuda  
LinkedIn: <https://www.linkedin.com/in/terry-benjamin-jr-274434116/>