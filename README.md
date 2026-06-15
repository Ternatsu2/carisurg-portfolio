# CariSurg Portfolio

Portfolio work for the CariSurg MedTech Pathways Healthcare AI programme.

## What This Is

This repository collects my CariSurg technical work, starting with emergency triage data cleaning, visualisation, and research writing. My project direction is clinician-facing support for emergency triage, with the final decision kept with the nurse or clinician.

## Who It Is For

The main audience is CariSurg tutors and clinical or technical reviewers who want to see the work behind my submissions without digging through separate files. It should also be readable for someone reviewing my healthcare AI portfolio later.

## Repository Layout

- `notebooks/`: cleaned Week 0 notebook copies for the portfolio.
- `docs/`: Week 1 memo, the Week 2-updated proposal, and the reference library.
- `data/`: placeholder for programme datasets. Real patient data should not be committed here.
- `week0/`: original Week 0 submission folders and outputs.
- `week1/`: original Week 1 report folder.

## Week 0

Week 0 covered onboarding, data cleaning, basic visualisation, and rule-based triage logic.

- `week0/notebooks/day1_clean_gender.ipynb`: cleaned the "Gender" column and checked the mapped values.
- `week0/notebooks/day2_clean_pulse.ipynb`: cleaned GCS, SBP, Temp, and Pulse, then checked the final Pulse range.
- `week0/notebooks/day3_visualization.ipynb`: made a Pulse histogram and an Age vs Pulse scatter plot.
- `week0/reports/assignment4_vital_sign_description.pdf`: short write-up on Pulse as a triage vital sign.
- `week0/reports/assignment5_unconsidered_metrics.pdf`: short write-up on SpO2 as an extra triage measure.
- `week0/reports/assignment6_triage_pseudocode.pdf`: pseudocode for a rule-based digital triage screen.

The Day 3 plot images are saved in `week0/outputs/plots`.

## Week 1

Week 1 focuses on research fundamentals and a preliminary proposal direction for AI-assisted emergency triage.

- `week1/reports/week1_interim_ai_triage_memo.pdf`: interim memo with paper summaries and a draft problem statement.
- `docs/week1_interim_ai_triage_memo.md`: Markdown copy of the interim memo.
- `docs/week1_final_ai_triage_proposal.md`: Week 2-updated proposal with eight papers and DOI-checked references.

## Setup

The Week 0 notebooks use Python 3 with pandas, numpy, and matplotlib.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you are using Google Colab, upload or mount the dataset in the path expected by the notebook before running the cells.

## Data Note

The Week 0 dataset is a reduced, de-identified triage dataset provided for the programme. This repo does not include real patient data, credentials, API keys, or private clinical records.

## Contact

Terry Benjamin Jr.  
St. John's, Antigua and Barbuda  
LinkedIn: <https://www.linkedin.com/in/terry-benjamin-jr-274434116/>
