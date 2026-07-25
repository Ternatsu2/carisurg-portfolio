# Week 8 interim: reproducible triage pipeline

**Student:** Terry Benjamin Jr.

**Programme:** CariSurg MedTech Pathways

**Date:** 25 July 2026

## Submission

I moved the final Week 7 model path out of the notebook and into a small,
config-driven Python package. The original notebooks remain unchanged as the
exploration and decision record.

| Rubric area | Evidence |
| --- | --- |
| `src/` layout refactor | [`src/data.py`](../src/data.py) handles loading, validation, and the fixed split. [`src/model.py`](../src/model.py) builds and evaluates the pinned model. [`src/features.py`](../src/features.py) preserves feature selection and the Week 7 feature functions. |
| Draft model-selection table | [`docs/model-selection.md`](model-selection.md) records the Week 6 and Week 7 runs, settings, headline metrics, ESI 1 result, training time, and inference time. |
| Handover outline | [`HANDOVER.md`](../HANDOVER.md) covers the project, model verdict, run steps, data governance, three limitations, and ownership. |
| Notebook preservation and discipline | All prior notebooks remain under [`notebooks/`](../notebooks/). The pinned dependencies are in [`requirements.txt`](../requirements.txt), model settings are in [`config.yaml`](../config.yaml), the entry point is [`scripts/train.py`](../scripts/train.py), and the two checks are in [`tests/test_pipeline.py`](../tests/test_pipeline.py). |

## Reproduction check

The refactored command ran against all 55,121 records and reproduced the Week 7
holdout result:

- 44,096 training visits and 11,025 test visits
- 209 numeric input features
- accuracy `0.680544`
- macro F1 `0.500879`
- ESI 1 recall `0.4375`, or 7 of 16 visits
- test-index SHA-256 `5e31ff9f74281290a36280585ecab4a22f5cb2b1ca48a6c2d1f7aed85422fa47`

The machine-readable values are in
[`docs/week8_reproduction_metrics.json`](week8_reproduction_metrics.json).
Both `pytest` checks pass on a fresh 50-row synthetic fixture without requiring
the private programme CSV.
