# Week 6 Baseline Report: Emergency Triage Classification

**Student:** Terry Benjamin Jr.<br>
**Programme:** CariSurg MedTech Pathways<br>
**Date:** 14 July 2026

## Decision supported

I tested whether simple classifiers can support a triage nurse by estimating the recorded Emergency Severity Index (ESI) level from information available at triage. The models do not assign care independently and are not ready for clinical use. The result that matters most is the weakest one: logistic regression correctly identified only 4 of the 16 ESI 1 visits in the held-out test set.

## Dataset recap

The supplied dataset contains 55,121 emergency department visits and 225 usable columns after removal of the exported index. The target has five levels, from ESI 1, which requires immediate intervention, to ESI 5. Only 77 visits are ESI 1, compared with 27,010 ESI 3 visits. That imbalance makes overall accuracy a poor safety measure on its own.

I used 209 numeric inputs, including age, front-door vital signs and chief-complaint flags. I excluded "disposition" and "previousdispo" because they are known after triage and would leak future information. Unencoded string fields were also held out. The data was split 80/20 with stratification on ESI and a fixed random seed of 42. The held-out test set contains 11,025 visits, including 16 ESI 1 cases.

## Models

The comparison floor is a stratified dummy classifier that guesses in the same proportions as the training labels. Logistic regression uses standardised inputs, with the scaler fitted on training data only. The decision tree uses the unscaled values and is limited to a depth of five. This keeps the first tree readable and reduces its tendency to memorise the training set.

## Benchmark results

| Model | Accuracy | Macro F1 | Weighted F1 | ESI 1 recall |
|---|---:|---:|---:|---:|
| Stratified dummy | 0.375 | 0.204 | 0.375 | 0.000 |
| Logistic regression | **0.683** | **0.508** | **0.677** | **0.250** |
| Decision tree, depth 5 | 0.547 | 0.207 | 0.448 | 0.000 |

Logistic regression is the strongest baseline on every reported measure. It improves accuracy by 0.307 and macro F1 by 0.304 over the random comparison. The tree performs above the dummy on accuracy, but it predicts almost everything as ESI 3. It never predicts ESI 1, 4 or 5 in the test set, so its overall score hides severe class failures.

Macro F1 gives each ESI level equal influence. Weighted F1 gives more influence to common levels such as ESI 3. The 0.169 gap between logistic regression's weighted and macro F1 shows how performance on common classes can make the model look safer than its results on rare classes.

## Class-level results

**Logistic regression**

| ESI | Precision | Recall | F1 | Test visits |
|---:|---:|---:|---:|---:|
| 1 | 0.500 | 0.250 | 0.333 | 16 |
| 2 | 0.736 | 0.626 | 0.677 | 3,585 |
| 3 | 0.676 | 0.770 | 0.720 | 5,402 |
| 4 | 0.622 | 0.612 | 0.617 | 1,779 |
| 5 | 0.500 | 0.119 | 0.193 | 243 |

**Decision tree, depth 5**

| ESI | Precision | Recall | F1 | Test visits |
|---:|---:|---:|---:|---:|
| 1 | 0.000 | 0.000 | 0.000 | 16 |
| 2 | 0.790 | 0.233 | 0.360 | 3,585 |
| 3 | 0.522 | 0.962 | 0.677 | 5,402 |
| 4 | 0.000 | 0.000 | 0.000 | 1,779 |
| 5 | 0.000 | 0.000 | 0.000 | 243 |

## Primary metric and failure mode

I chose ESI 1 recall as the primary safety measure because it answers a direct clinical question: of the patients who need immediate intervention, how many does the model identify at that level? Logistic regression finds 4 of 16, for recall of 0.25. It misses 12. Eleven are assigned ESI 2 and one is assigned ESI 4. A false negative could place a patient who needs immediate resuscitation into a slower pathway.

The failure is plausible given the data. ESI 1 has only 77 examples in the full dataset, and the first baseline uses numeric triage fields without the unencoded arrival and demographic fields. The target is also the recorded ESI decision rather than an independently adjudicated clinical outcome. I cannot tell from this run whether each miss reflects scarce examples, an ambiguous presentation, label noise or a missing signal.

The result rules out deployment. Although ESI 2 is still urgent, the model has not shown that it can separate immediate from emergent care with acceptable consistency. Accuracy does not offset that failure.

## Next steps

The next experiment should test class weighting and a one-versus-rest probability threshold for ESI 1 on the training data only. I would compare any gain in ESI 1 detection with the number of false alarms, because an alert that fires too often can lose clinical trust. Cross-validation, probability calibration and subgroup checks should follow before an external dataset or prospective workflow test. A clinician should review the ESI 1 errors before any model change is treated as an improvement.

## Reproducibility and artefacts

- Random seed: 42
- Split: 80/20, stratified on "esi"
- Models: stratified dummy, scaled logistic regression, decision tree with max_depth=5
- Notebook: `notebooks/week6_final_baseline_models.ipynb`
- Aggregate metrics: `docs/w6_final_metrics.csv`
- Class-level metrics: `docs/w6_per_class_metrics.csv`
- Confusion matrices: `docs/w6_confusion_logreg.png` and `docs/w6_confusion_tree.png`
- Clinical explainer: `docs/week6_clinical_explainer.mp4`
- Explainer transcript: `docs/week6_clinical_explainer_script.txt`

The full clinical CSV remains outside GitHub.
