# Week 6 Final Report: Emergency Triage Classification

**Student:** Terry Benjamin Jr.<br>
**Programme:** CariSurg MedTech Pathways<br>
**Date:** 14 July 2026

## Decision supported

I tested whether simple classifiers could support a triage nurse by estimating the recorded Emergency Severity Index (ESI) level from information available at triage. The models do not assign care independently. After tuning on a validation split, logistic regression identified 7 of the 16 ESI 1 visits in the held-out test set, compared with 4 before tuning.

## Dataset and split

The supplied dataset contains 55,121 emergency department visits and 225 usable columns after removal of the exported index. Only 77 visits are ESI 1, compared with 27,010 ESI 3 visits. I used 209 numeric inputs, including age, front-door vital signs and chief-complaint flags. I excluded "disposition" and "previousdispo" because both are known after triage and would leak future information.

I held out 20% of the data for the final test and stratified on ESI with random seed 42. I then split the remaining training data again for tuning. The test set was not used to select settings. It contains 11,025 visits, including 16 ESI 1 cases.

## Models and tuning

The comparison floor is a stratified dummy classifier. The required logistic baseline uses standardised inputs. The required decision-tree baseline uses unscaled inputs and a maximum depth of five.

David's interim feedback called for stronger rare-class performance and closer inspection of ESI 1 presentations. I therefore tested ESI 1 class weights of 2, 4, 8 and 12 for logistic regression. For the tree, I tested depths of 5, 8 and 12, minimum leaf sizes of 1, 5, 10 and 25, with and without balanced class weights. I required validation ESI 1 recall of at least 0.25, then selected the eligible setting with the highest validation macro F1. This selected an ESI 1 weight of eight for logistic regression and a balanced depth-12 tree with a minimum leaf size of ten.

## Held-out results

| Model | Accuracy | Macro F1 | Weighted F1 | ESI 1 recall | ESI 1 precision | ESI 1 caught | False ESI 1 alerts |
|---|---:|---:|---:|---:|---:|---:|---:|
| Stratified dummy | 0.375 | 0.204 | 0.375 | 0.000 | 0.000 | 0/16 | 10 |
| Logistic baseline | **0.683** | **0.508** | **0.677** | 0.250 | 0.500 | 4/16 | 4 |
| Tree baseline | 0.547 | 0.207 | 0.448 | 0.000 | 0.000 | 0/16 | 0 |
| Logistic tuned | 0.681 | 0.501 | 0.675 | **0.438** | 0.233 | **7/16** | 23 |
| Tree tuned | 0.497 | 0.356 | 0.510 | 0.375 | 0.024 | 6/16 | 244 |

Tuning improves the chosen safety measure. The logistic model catches three additional ESI 1 visits while its accuracy changes by only 0.002. The price is 19 additional false ESI 1 alerts. The tuned tree also finds more ESI 1 visits, but its 244 false alerts and lower accuracy make it a poor candidate.

## Class-level results after tuning

| Model | ESI | Precision | Recall | F1 | Test visits |
|---|---:|---:|---:|---:|---:|
| Logistic tuned | 1 | 0.233 | 0.438 | 0.304 | 16 |
|  | 2 | 0.735 | 0.621 | 0.673 | 3,585 |
|  | 3 | 0.675 | 0.769 | 0.719 | 5,402 |
|  | 4 | 0.621 | 0.610 | 0.615 | 1,779 |
|  | 5 | 0.500 | 0.119 | 0.193 | 243 |
| Tree tuned | 1 | 0.024 | 0.375 | 0.045 | 16 |
|  | 2 | 0.715 | 0.368 | 0.486 | 3,585 |
|  | 3 | 0.600 | 0.548 | 0.572 | 5,402 |
|  | 4 | 0.297 | 0.643 | 0.406 | 1,779 |
|  | 5 | 0.361 | 0.214 | 0.269 | 243 |

## ESI 1 error review

I reviewed the 16 held-out ESI 1 cases after evaluation, using aggregate values rather than individual records. Five of the seven caught cases had a stroke-alert flag. The nine misses were less consistent: four were grouped as "other", two had shortness-of-breath flags, and single cases carried flags for hypotension, altered mental status, dizziness, a neurologic problem, poisoning or a mass. Multiple flags can appear for one visit.

| Median triage measure | Caught, n=7 | Missed, n=9 |
|---|---:|---:|
| Age | 73 | 81 |
| Heart rate | 81 | 81 |
| Systolic blood pressure | 195.5 | 148 |
| Diastolic blood pressure | 101 | 64 |
| Respiratory rate | 18.5 | 18 |
| Oxygen saturation | 98 | 96 |
| Temperature | 97.8 | 97.8 |
| Glucose | 118 | 113 |

The caught group is dominated by a clear stroke-alert signal. The missed group is older at the median and has lower median oxygen saturation, but 16 cases are too few for a stable clinical conclusion. A clinician should review these errors before complaint interactions, vital thresholds or new features are added.

## Metric choice and decision

I use ESI 1 recall as the primary safety measure because it asks how many patients needing immediate intervention are recognised at that level. Accuracy and weighted F1 remain useful, but both are dominated by common ESI levels. The tuned logistic model improves ESI 1 recall by 0.188 without a material accuracy loss, yet it still misses 9 of 16 cases and more than triples the number of ESI 1 predictions.

The result supports further testing, not deployment. I would carry the tuned logistic model forward for probability calibration, clinician review and repeated stratified validation. Any threshold change should report critical cases caught alongside false alerts. The dataset also needs external validation and subgroup checks before it can support a real workflow.

## Reproducibility and artefacts

- Random seed: 42
- Split: 80/20 held-out test, with a second stratified split inside training for tuning
- Notebook: `notebooks/week6_final_baseline_models.ipynb`
- Aggregate metrics: `docs/w6_final_metrics.csv`
- Class metrics: `docs/w6_per_class_metrics.csv`
- Tuning record: `docs/w6_tuning_results.csv`
- ESI 1 profiles: `docs/w6_esi1_vital_profile.csv` and `docs/w6_esi1_complaint_profile.csv`
- Confusion matrices: baseline and tuned versions in `docs/`
- Clinical explainer: `docs/week6_clinical_explainer.mp4`

The full clinical CSV remains outside GitHub.
