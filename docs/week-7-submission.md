# Week 7 Final Submission

**Student:** Terry Benjamin Jr.  
**Programme:** CariSurg MedTech Pathways  
**Date:** 20 July 2026

## Decision

I recommend carrying the tuned logistic model into Phase 3 as a clinician-facing shadow-mode comparator, not as an autonomous triage tool.

## Deliverables

- [Executed model notebook](../notebooks/week7_final_model_tradeoff.ipynb)
- [Three-page cost-benefit memo (PDF)](week-7-cost-benefit.pdf)
- [Cost-benefit memo (Markdown)](week-7-cost-benefit.md)
- [Decision journal](decisions/2026-week-7-model-choice.md)
- [Seven-dimension benchmark](week7_final_benchmark.md)

## Evidence by assessment area

| Assessment area | Evidence |
| --- | --- |
| Complex model implementation and reproducibility | The notebook reproduces the Week 6 split, engineers 11 features, and tunes Random Forest and histogram gradient boosting with training-only cross-validation. |
| Benchmark and interpretability | The benchmark reports accuracy, macro precision, macro recall, macro F1, final training time, inference time per patient, and a model-specific interpretability assessment. |
| Cost-benefit recommendation | The three-page memo opens with the verdict, gives the benchmark, presents three arguments for and against, reviews clinical risk, and gives a Phase 3 recommendation. |
| Decision journal | The dated journal records context, alternatives, the decision, reasoning, unknowns, and evidence. |
| Repo discipline and writing | Files are under `notebooks/` and `docs/`; the full clinical CSV and local environment are excluded from Git. |

## Reproduce the notebook

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export CARISURG_TRIAGE_CSV=/path/to/yaleemmlc_admissionprediction_triage.csv
jupyter notebook notebooks/week7_final_model_tradeoff.ipynb
```

The submitted notebook was executed with the same 44,096/11,025 stratified
split used in Week 6. Its test-index SHA-256 is
`5e31ff9f74281290a36280585ecab4a22f5cb2b1ca48a6c2d1f7aed85422fa47`.
