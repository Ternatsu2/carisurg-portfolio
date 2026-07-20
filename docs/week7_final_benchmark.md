# Week 7 final benchmark

**Student:** Terry Benjamin Jr.  
**Programme:** CariSurg MedTech Pathways  
**Date:** 20 July 2026

## Method

All models use the same 44,096 training visits and 11,025 test visits from the
Week 6 stratified split (`random_state=42`). Random Forest and gradient-boosting
hyperparameters were selected by three-fold cross-validation on the training
set. The unchanged holdout contains 16 ESI 1 visits.

## Seven-dimension comparison

| Model | Features | Accuracy | Macro precision | Macro recall | Macro F1 | ESI 1 caught | Train (s) | Inference (ms/patient) | Interpretability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Week 6 tuned logistic | Week 6 numeric set | 0.681 | 0.553 | 0.511 | 0.501 | 7/16 (43.8%) | 3.36 | 0.0012 | High |
| Tuned Random Forest | Week 6 set + 11 engineered features | 0.572 | 0.425 | 0.536 | 0.444 | 5/16 (31.2%) | 4.98 | 0.0078 | Medium |
| Tuned gradient boosting | Week 6 set + 11 engineered features | 0.623 | 0.460 | 0.588 | 0.485 | 6/16 (37.5%) | 28.63 | 0.0153 | Low |

Search time was 154.3 seconds for Random Forest and
108.2 seconds for gradient boosting. Search cost is separate
from the final training-time column.

## Recommendation

Carry **Week 6 tuned logistic** into Phase 3 shadow-mode testing. The strongest
complex candidate was **Tuned gradient boosting**, with a macro-F1 change of
-0.0162 and an ESI 1 recall
change of -6.2%
relative to the tuned logistic model. That is not enough evidence to accept
extra complexity for a clinician-facing prototype.

## Supporting artefacts

- [Executed notebook](../notebooks/week7_final_model_tradeoff.ipynb)
- [Model comparison](week7_final_model_comparison.png)
- [Confusion matrices](week7_final_confusion_comparison.png)
- [Random Forest feature importance](week7_final_feature_importance.png)
- [ESI 1 complaint patterns](week7_final_esi1_complaints.png)
- [Machine-readable benchmark](week7_final_benchmark.csv)
