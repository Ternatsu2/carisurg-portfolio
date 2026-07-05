# Week 5 Interim Feasibility Memo Outline: AI-Assisted Emergency Triage

Student: Terry Benjamin Jr.  
Programme: CariSurg MedTech Pathways  
Dataset: yaleemmlc_admissionprediction_triage.csv  
Date: 4 July 2026

## Working Question

Can the Week 5 ED triage dataset support a first baseline triage-support model that helps a triage nurse or clinician review likely acuity without replacing clinical judgement?

## Data Reviewed

I used the TenX Week 5 CSV file and treated "esi" as the triage level target. The file contains 55,121 ED visits and 225 usable columns after removing the exported index column. The features cover demographics, arrival details, triage vital signs, glucose, and 200 chief complaint flags.

The target is complete in this reduced file. The ESI distribution is uneven: ESI 1 accounts for 0.14% of visits, ESI 2 for 32.52%, ESI 3 for 49.00%, ESI 4 for 16.14%, and ESI 5 for 2.20%. Most records sit in the middle-acuity groups, which matches ED triage work but creates a modelling risk for the rare extremes.

## Initial Profiling Checks

I checked row and column counts, duplicate rows, ESI target completeness, ESI class balance, missing values, and basic clinical ranges for triage vital signs. The reduced file has no missing values in the included columns. That makes the data easier to profile, but it does not remove the need for clinical review.

## Missingness and Data Quality Read

Missingness is not the main blocker in the reduced file. The bigger issues are class imbalance, rare ESI 1 cases, and clinically questionable range flags. I would flag those values for review before modelling rather than delete them automatically.

## Early Feasibility Read

The dataset can support a first baseline triage model because it has scale, a complete ESI target, and features that would be available at or near triage. I would not treat the dataset as deployment-ready until the team checks class-wise error, subgroup performance, and whether flagged values reflect real emergencies or entry/unit problems.

## Main Risks To Carry Forward

1. Class imbalance needs attention. The dataset has only 77 ESI 1 visits and 1214 ESI 5 visits. A model could perform well on average while doing poorly for the most urgent or least urgent classes.

2. Some vital and glucose values need clinical review before modelling. I flagged 530 rows across the range checks. Most flags are rare, but glucose has 403 values outside 40 to 500 mg/dL. Some may represent true clinical extremes, while others may be data-entry or unit issues.

3. Fairness review should be planned early. The dataset includes race and ethnicity fields, which means later work should check whether model errors differ across patient groups.

## Next Steps For The Final Submission

For the final deliverable, I would add the full exploration notebook, a data-quality dashboard, a top-10 feature shortlist, and a short feasibility memo for the ED Board.
