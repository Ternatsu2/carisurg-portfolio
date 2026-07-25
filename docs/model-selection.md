# Model selection record

**Decision date:** 20 July 2026

**Refactor check:** 25 July 2026

**Held-out set:** 11,025 visits, including 16 ESI 1 visits

All rows use the same stratified holdout created with `random_state=42`.
Week 6 timings below were rerun on 25 July with the pinned environment; Week 7
timings are the values recorded in the corresponding executed notebooks.

| Model run | Key settings | Accuracy | Macro precision | Macro recall | Macro F1 | ESI 1 caught | Train (s) | Inference (ms/patient) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Stratified dummy | `strategy=stratified` | 0.375 | 0.204 | 0.204 | 0.204 | 0/16 | 0.00 | 0.0002 |
| Logistic baseline | scaled, `max_iter=1500` | 0.683 | 0.607 | 0.476 | 0.508 | 4/16 | 2.55 | 0.0063 |
| Decision tree baseline | `max_depth=5` | 0.547 | 0.262 | 0.239 | 0.207 | 0/16 | 0.55 | 0.0012 |
| **Tuned logistic - selected** | scaled, `class_weight={1: 8}`, `max_iter=1500` | **0.681** | **0.553** | 0.511 | **0.501** | **7/16** | 3.44 | 0.0012 |
| Tuned decision tree | `max_depth=12`, `min_samples_leaf=10`, `class_weight=balanced` | 0.497 | 0.399 | 0.430 | 0.356 | 6/16 | 0.96 | 0.0006 |
| Initial Random Forest | 250 trees, leaf 2, `sqrt`, balanced subsample | 0.623 | 0.475 | 0.548 | 0.493 | 5/16 | 9.59 | 0.0184 |
| Macro-F1 Random Forest + 11 features | 200 trees, leaf 4, features 0.6, balanced | 0.642 | 0.498 | 0.509 | 0.502 | 5/16 | 31.17 | 0.0108 |
| ESI 1-sensitive Random Forest + 11 features | 300 trees, depth 14, leaf 8, `sqrt`, balanced subsample | 0.522 | 0.392 | 0.545 | 0.396 | 7/16 | 3.43 | 0.0060 |
| Final tuned Random Forest + 11 features | 150 trees, leaf 8, `sqrt`, balanced | 0.572 | 0.425 | 0.536 | 0.444 | 5/16 | 4.98 | 0.0078 |
| Final tuned gradient boosting + 11 features | 200 iterations, 63 leaves, leaf 10, rate 0.08, L2 1.0 | 0.623 | 0.460 | **0.588** | 0.485 | 6/16 | 28.63 | 0.0153 |

## Decision

The tuned logistic model remains the shadow-mode candidate. It matched the
highest observed ESI 1 recall at 7 of 16 cases, retained the strongest macro F1
among the final Week 7 candidates, and offers a more direct explanation path
than the tree ensembles. The one complex run with a marginally higher macro F1
caught only 5 ESI 1 cases, so that difference did not justify the safety and
interpretability trade-off.

The exact final configuration is pinned in [`config.yaml`](../config.yaml).
The reasoning and unresolved questions remain in the
[Week 7 decision journal](decisions/2026-week-7-model-choice.md).

## Source records

- [Week 6 aggregate metrics](w6_final_metrics.csv)
- [Week 6 per-class metrics](w6_per_class_metrics.csv)
- [Week 7 interim benchmark](week7_benchmark_metrics.csv)
- [Week 7 final benchmark](week7_final_benchmark.csv)
- [Executed Week 6 notebook](../notebooks/week6_final_baseline_models.ipynb)
- [Executed Week 7 interim notebook](../notebooks/week7_interim_complex_model.ipynb)
- [Executed Week 7 final notebook](../notebooks/week7_final_model_tradeoff.ipynb)
