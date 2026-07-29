# Week 8 final: reproducible triage handover

**Student:** Terry Benjamin Jr.

**Programme:** CariSurg MedTech Pathways

**Date:** 29 July 2026

## What I completed

I moved the selected Week 7 model into a config-driven Python pipeline and kept
the original notebooks as the exploration record. A reviewer can now install
the pinned environment, run one training command, and reproduce the same
holdout result without selecting notebook cells by hand.

## Review map

| Rubric area | Evidence |
| --- | --- |
| Modular layout and config-driven pipeline | [`src/data.py`](../src/data.py), [`src/features.py`](../src/features.py), [`src/model.py`](../src/model.py), and [`src/utils.py`](../src/utils.py) hold the reusable functions. [`scripts/train.py`](../scripts/train.py) is the single entry point and [`config.yaml`](../config.yaml) pins the selected model and split. |
| Reproducibility and environment setup | [`requirements.txt`](../requirements.txt) pins the package versions. The setup and training commands are in the [`README`](../README.md) and [`HANDOVER.md`](../HANDOVER.md). |
| Pytest sanity checks | [`tests/test_pipeline.py`](../tests/test_pipeline.py) checks the data contract and runs a 50-row train-and-predict smoke test. The same checks run through [GitHub Actions](../.github/workflows/tests.yml). |
| Model-selection results | [`docs/model-selection.md`](model-selection.md) records all Week 6 and Week 7 model runs, their settings, headline metrics, ESI 1 result, and timing. |
| Handover and writing quality | [`HANDOVER.md`](../HANDOVER.md) gives the project summary, final model verdict, run steps, data rules, three known limitations, and ownership contacts. |

## Final model

I kept the tuned multinomial logistic regression with ESI 1 weighted at 8. On
the unchanged test set it caught 7 of 16 ESI 1 visits, reached a macro F1 of
0.501, and remained easier to explain than the tree ensembles. The model is a
shadow-mode candidate only; the nurse or clinician keeps the triage decision.

## Reproduction result

The refactored command ran against all 55,121 records and returned:

- 44,096 training visits and 11,025 test visits
- 209 numeric input features
- accuracy `0.680544`
- macro F1 `0.500879`
- ESI 1 recall `0.4375`, or 7 of 16 visits
- test-index SHA-256 `5e31ff9f74281290a36280585ecab4a22f5cb2b1ca48a6c2d1f7aed85422fa47`

The saved values are in
[`docs/week8_reproduction_metrics.json`](week8_reproduction_metrics.json).
Both pytest checks pass without the private programme CSV.
