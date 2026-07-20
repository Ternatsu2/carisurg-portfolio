# Decision Journal: Week 7 Model Choice

**Date:** 20 July 2026  
**Decision owner:** Terry Benjamin Jr.  
**Status:** Accepted for Phase 3 shadow-mode prototyping

## Context

- The ED Board asked whether a more sophisticated classifier produces enough
  clinical benefit to justify added compute and reduced interpretability.
- Week 6 tuning improved ESI 1 recall, but the held-out test set contains only
  16 ESI 1 visits and every model still misses critical cases.

## Alternatives

- Keep the Week 6 tuned logistic model with the original numeric feature set.
- Use the cross-validated Random Forest with 11 engineered clinical features.
- Use the cross-validated histogram gradient-boosting model with the same
  engineered feature set.

## Decision

Carry **Week 6 tuned logistic** into Phase 3 as a clinician-facing shadow-mode
comparator, not as an autonomous triage system.

## Reasoning

- It caught 7 of 16 ESI 1 visits, while the
  strongest complex candidate caught 6.
- The strongest complex candidate changed macro F1 by -0.0162;
  that does not justify a weaker explanation path for the current prototype.
- The selected model is the most defensible option for clinician review and IT
  governance while all absolute performance remains exploratory.

## Unknowns

- Performance on Mercer General or another Caribbean ED may differ from the
  Yale holdout because case mix, labelling, workflow, and measurement differ.
- More ESI 1 data, calibration, subgroup analysis, and prospective shadow-mode
  testing could change the model ranking.

## Evidence

- [Final benchmark](../week7_final_benchmark.md)
- [Cost-benefit memo](../week-7-cost-benefit.md)
- [Executed notebook](../../notebooks/week7_final_model_tradeoff.ipynb)
