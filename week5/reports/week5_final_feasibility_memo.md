# Week 5 Final Feasibility Memo: AI-Assisted Emergency Triage

Student: Terry Benjamin Jr.  
Programme: CariSurg MedTech Pathways  
Dataset: yaleemmlc_admissionprediction_triage.csv  
Date: 4 July 2026

## One-Sentence Verdict

The Week 5 triage dataset is strong enough to support a first baseline triage-support model, but I would not treat it as deployment-ready until the team checks class imbalance, range flags, and subgroup performance.

## Dataset Summary

I used the TenX Week 5 CSV file and treated "esi" as the triage level target. The file contains 55,121 ED visits and 225 usable columns after removing the exported index column. The features cover demographics, arrival details, triage vital signs, glucose, and 200 chief complaint flags.

The target is complete in this reduced file. The ESI distribution is uneven: ESI 1 accounts for 0.14% of visits, ESI 2 for 32.52%, ESI 3 for 49.00%, ESI 4 for 16.14%, and ESI 5 for 2.20%. Most records sit in the middle-acuity groups, which matches ED triage work but creates a modelling risk for the rare extremes.

The data also includes race and ethnicity fields, so a later model can be checked for subgroup performance. Those fields should support fairness review, not automatic triage decisions.

## Top Three Data Quality Concerns

1. Class imbalance needs attention. The dataset has only 77 ESI 1 visits and 1214 ESI 5 visits. A model could perform well on average while doing poorly for the most urgent or least urgent classes.

2. Some vital and glucose values need clinical review before modelling. I flagged 530 rows across the range checks. Most flags are rare, but glucose has 403 values outside 40 to 500 mg/dL. Some may represent true clinical extremes, while others may be data-entry or unit issues.

3. Chief complaint data is useful but uneven. "cc_abdominalpain" appears in 6,717 visits, while many complaint flags are rare. The broad "cc_other" field also appears often, so the team should avoid letting vague complaint buckets carry too much weight.

## Top Three Reasons to Proceed

1. The file has enough scale for baseline modelling. With 55,121 visits and a complete target, Week 6 can build a train/test split without fighting missing labels.

2. The features are available at or near triage. Age, arrival mode, vital signs, glucose, and chief complaints fit the information a triage workflow can reasonably use.

3. The first signal checks make clinical sense. Age, oxygen saturation, chest pain, shortness of breath, suicidal ideation, altered mental status, respiratory rate, and heart rate all show measurable association with ESI. None of these signals should decide triage alone, but they are reasonable inputs for decision support.

## Top-10 Feature Shortlist

| Rank | Feature | ESI Correlation | Direction | Reason |
|---:|---|---:|---|---|
| 1 | age | -0.2366 | Lower ESI, more urgent | Older adults often receive higher-acuity review because frailty, comorbidity, and atypical symptoms can change risk. |
| 2 | triage_vital_o2 | 0.1779 | Higher ESI, less urgent | Low oxygen saturation can point to respiratory compromise and can move a patient toward faster assessment. |
| 3 | cc_chestpain | -0.1643 | Lower ESI, more urgent | Chest pain needs rapid triage because myocardial infarction and other time-sensitive diagnoses must stay on the table. |
| 4 | cc_shortnessofbreath | -0.1503 | Lower ESI, more urgent | Shortness of breath can reflect asthma, heart failure, pulmonary embolism, infection, or other urgent problems. |
| 5 | cc_suicidal | -0.1426 | Lower ESI, more urgent | Suicidal ideation changes safety planning and disposition even when vital signs look stable. |
| 6 | cc_alcoholintoxication | -0.1421 | Lower ESI, more urgent | Intoxication can mask trauma, hypoglycaemia, overdose, or reduced consciousness. |
| 7 | cc_alteredmentalstatus | -0.1320 | Lower ESI, more urgent | Altered mental status is a high-risk complaint because the patient may not give a reliable history. |
| 8 | triage_vital_rr | -0.0953 | Lower ESI, more urgent | Respiratory rate is a simple bedside marker for respiratory distress, sepsis, pain, and compensation. |
| 9 | triage_vital_hr | -0.0952 | Lower ESI, more urgent | Heart rate helps flag shock, pain, fever, arrhythmia, dehydration, and anxiety, but it needs clinical context. |
| 10 | triage_glucose | -0.0778 | Lower ESI, more urgent | Very low or very high glucose can change triage priority and may explain confusion or weakness. |


## Supporting Plots and Tables

The repository includes the following Week 5 outputs:

- "docs/week5_data_quality_dashboard.svg"
- "docs/week5_missingness_summary.svg"
- "docs/week5_feature_signal_summary.svg"
- "docs/week5_chief_complaint_distribution.svg"
- "docs/week5_demographics_review.svg"
- "docs/week5_top10_feature_shortlist.csv"
- "docs/week5_data_quality_checks.csv"

## Caveats for the ED Board

This dataset supports a feasibility decision, not a clinical launch decision. Before anyone uses a model from it, the team should define the exact triage task, remove leakage fields, confirm the ESI direction with clinicians, and test performance by ESI class, race, ethnicity, age group, and arrival mode.

I would build the Week 6 baseline as a transparent classifier first. Logistic regression or a shallow decision tree would make sense before trying a larger model. The first pass should report confusion matrix results by ESI class, not only one overall accuracy score.

## References

Hong, W. S., Haimovich, A. D., & Taylor, R. A. (2018). Predicting hospital admission at emergency department triage using machine learning. PLOS ONE, 13(7), e0201016. https://doi.org/10.1371/journal.pone.0201016

CariSurg MedTech Pathways. (2026). Week 5: AI-Assisted Triage: Data Exploration. TenX Week 5 module and dataset.
