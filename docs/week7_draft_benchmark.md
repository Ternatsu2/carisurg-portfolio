# Week 7 draft benchmark comparison

**Student:** Terry Benjamin Jr.

**Programme:** CariSurg MedTech Pathways

**Date:** 18 July 2026

## Scope

This draft compares the reproduced Week 6 tuned logistic model with three Week 7
Random Forest runs. All rows use the same stratified holdout created with
`test_size=0.20`, `stratify=y` and `random_state=42`: 44,096 training visits and
11,025 test visits. The test set contains 16 ESI 1 visits. Hyperparameters were
selected by three-fold cross-validation on the training set; the holdout was not
used for selection.

## Initial benchmark

| Model | Features | Accuracy | Macro precision | Macro recall | Macro F1 | ESI 1 caught | Train (s) | Inference (ms/patient) | Interpretability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Week 6 tuned logistic | Week 6 numeric set | 0.681 | 0.553 | 0.511 | 0.501 | 7/16 (43.8%) | 1.70 | 0.0008 | High |
| Initial Random Forest | Week 6 numeric set | 0.623 | 0.475 | 0.548 | 0.493 | 5/16 (31.2%) | 9.59 | 0.0184 | Medium |
| Macro-F1 Random Forest + red flags | Week 6 numeric set + 2 red flags | 0.642 | 0.498 | 0.509 | 0.502 | 5/16 (31.2%) | 31.17 | 0.0108 | Medium |
| ESI 1-sensitive Random Forest + red flags | Week 6 numeric set + 2 red flags | 0.522 | 0.392 | 0.545 | 0.396 | 7/16 (43.8%) | 3.43 | 0.0060 | Medium |

The hyperparameter search took 305.1 seconds. This is reported
separately from final-model training time.

## Early read

`Macro-F1 Random Forest + red flags` has the strongest macro F1 in this first benchmark.
The highest observed ESI 1 recall is 43.8%, shared by the Week 6 tuned logistic
and the ESI 1-sensitive Random Forest. The macro-F1 forest caught
5 of 16 ESI 1 visits and missed
11. The ESI 1-sensitive forest caught
7 but gave up substantial macro-F1 performance.
Because that class has only 16 test examples, one
case moves recall by 6.25 percentage points; the count and the rate should stay
together in later reporting.

The Random Forest remains more expensive and less directly interpretable than
logistic regression, although feature importance provides a useful first check.
This interim table is evidence for the Tuesday analysis, not a deployment
recommendation.

## Artefacts

- [Executed Week 7 notebook](../notebooks/week7_interim_complex_model.ipynb)
- [Model comparison plot](week7_model_comparison.png)
- [Random Forest confusion matrix](week7_confusion_random_forest.png)
- [Feature importance plot](week7_feature_importance.png)
- [Machine-readable metrics](week7_benchmark_metrics.csv)
- [Cross-validation results](week7_random_forest_cv_results.csv)
