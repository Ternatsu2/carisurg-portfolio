# Week 7 Cost-Benefit Memo

**To:** Dr. De Freitas, Mercer General ED Board, and Martina Griffith, Clinical IT  
**From:** Terry Benjamin Jr.  
**Date:** 20 July 2026  
**Subject:** Model choice for the Phase 3 emergency-triage prototype

## Verdict

I recommend carrying the tuned logistic model into Phase 3 as a clinician-facing shadow-mode comparator, not as an autonomous triage tool.

## Dataset and method

I used the 55,121-visit Yale emergency-triage dataset from Weeks 5 and 6. The
comparison keeps the Week 6 split unchanged: 44,096 training visits and 11,025
test visits, including 16 ESI 1 visits. The logistic row uses the original 209
numeric features. The two complex models add 11 transparent features, including
shock index, pulse pressure, an oxygen-to-respiratory-rate ratio, and flags for
hypoxia, fast breathing, fever, hypothermia, slow heart rate, and high glucose.

Random Forest and histogram gradient boosting were tuned with three-fold
cross-validation on the training set. The held-out test patients were not used
to choose settings. Accuracy is the overall share of correct predictions.
Macro precision, recall, and F1 average the five ESI classes equally, so the
common middle classes cannot drown out the rare classes. Training time covers
one final fit. Inference time is the median of seven full-holdout prediction
runs divided by 11,025 patients.

## Seven-dimension benchmark

| Model | Accuracy | Macro precision | Macro recall | Macro F1 | ESI 1 caught | Train (s) | Inference (ms/patient) | Interpretability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Week 6 tuned logistic | 0.681 | 0.553 | 0.511 | 0.501 | 7/16 | 3.36 | 0.0012 | High |
| Tuned Random Forest | 0.572 | 0.425 | 0.536 | 0.444 | 5/16 | 4.98 | 0.0078 | Medium |
| Tuned gradient boosting | 0.623 | 0.460 | 0.588 | 0.485 | 6/16 | 28.63 | 0.0153 | Low |

The strongest complex candidate was **Tuned gradient boosting**. Against the tuned
logistic model, it changed macro F1 by -0.0162 and ESI 1 recall by
-6.2%. It took 8.5 times as long to train and
13.3 times as long to infer, although the absolute inference
times were below one millisecond per patient on this machine.

## Three arguments for the recommendation

### 1. It gives the strongest available urgent-class signal

It caught 7 of 16 ESI 1 visits (43.8%), compared with 6 for the strongest complex candidate.

### 2. The extra complexity did not buy enough

The strongest complex model changed macro F1 by only -0.016 and ESI 1 recall by -6.2%. That is not a material clinical gain.

### 3. It is easier to explain, audit, and operate

Its scaled coefficients give a direct, reviewable account of which features pushed a prediction towards each ESI class. For Martina's governance review, the simpler dependency chain
and shorter training path also reduce the number of components that must be
versioned and monitored.

## Three arguments against the recommendation

### 1. ESI 1 performance remains inadequate

It still missed 9 of 16 ESI 1 visits. That failure rate prevents any autonomous use.

### 2. The model form is restrictive

A linear decision boundary can miss interactions among complaints, oxygen status, age, and vital-sign combinations that tree ensembles can represent.

### 3. The evidence is thin where the consequence is highest

The recommendation rests on only 16 ESI 1 test visits. One case moves recall by 6.25 percentage points, so the ranking is not stable enough for a deployment decision.

## Cost and benefit in practice

The choice is not being driven by raw speed. All three models predicted the
11,025-patient holdout in well under one millisecond per patient on the test
machine. The meaningful cost is the work needed to understand, validate, monitor,
and defend each model. Random Forest and gradient boosting can represent
nonlinear interactions, but neither converted that flexibility into a better
combination of macro F1 and ESI 1 recall on this holdout.

The logistic model's benefit is therefore practical rather than absolute. It
provides the strongest current urgent-class result, a direct coefficient-based
review path, and a stable reference against which later models can be tested.
Its cost is equally clear: it cannot express complex interactions and its
9 missed ESI 1 visits make it unsuitable for autonomous use.

For Phase 3, a replacement model should improve both ESI 1 recall and macro F1
on external or prospective data, not merely improve accuracy or one common
class. It must also provide patient-level explanations that clinicians can
review and remain within the same workflow and latency constraints.

## Critical error review

The recommended model caught 7 of the 16 held-out
ESI 1 visits and under-triaged 9. Under the
notebook's transparent near-normal screen, 3 of 9 missed
visits had heart rate 60-100, respiratory rate 12-20, oxygen saturation at least
94%, systolic pressure at least 100, and temperature 96.8-100.4 F. The same was
true for 3 of 7 caught visits.

The most common complaint flags among misses were other (4 missed), shortness of breath (2 missed), altered mental status (1 missed), dizziness (1 missed), hypotension (1 missed). These are
aggregate counts, not proof that a complaint causes the error. They point to a
feature and data problem worth testing: some critical presentations may not look
critical from arrival vitals alone, and a broad binary complaint flag may not
carry enough context.

## Risks and unknowns

1. **External validity:** the data come from a Yale emergency department. The
   result has not been tested on Mercer General or another Caribbean ED.
2. **Rare-class uncertainty:** only 16 ESI 1 visits are in the holdout. Confidence
   in class-specific recall is therefore low.
3. **Label and feature limits:** the recorded ESI label can vary by local practice,
   and free-text nuance, clinician concern, medication, and oxygen context are not
   fully represented in the modelling table.
4. **Unfinished safety work:** calibration, subgroup performance, drift,
   prospective latency, and human-factors testing remain undone.
5. **Timing portability:** the reported time is from one laptop and one software
   environment. It is suitable for relative comparison, not capacity planning.

## Phase 3 evidence plan

1. **Local validation:** freeze the feature definitions and test on a
   representative Mercer General sample. Report raw ESI 1 counts and uncertainty,
   not only percentages.
2. **Safety review:** review under-triaged cases with ED clinicians, test
   calibration and subgroup performance, and document whether oxygen support,
   medication, and complaint detail explain recurring misses.
3. **Shadow workflow test:** run beside nurse-led triage, measure data failures,
   latency, disagreement, and override handling, and keep every model output out
   of the live ESI decision until the review is complete.

## Recommendation

Carry the **Week 6 tuned logistic** into Phase 3 only as a shadow-mode decision
support comparator. It should run behind the normal nurse-led triage process and
must not delay, replace, or automatically downgrade a clinician's ESI decision.

Before any live pilot, collect more ESI 1 examples, validate on local data, test
calibration and subgroup performance, review the missed complaint patterns with
ED clinicians, and define a fail-safe route for missing or out-of-range inputs.
A complex model should replace this choice only if it produces a repeatable,
clinically material gain in ESI 1 recall and macro F1 on external or prospective
data while meeting the same explanation and latency requirements.

## Supporting artefacts

- [Executed final notebook](../notebooks/week7_final_model_tradeoff.ipynb)
- [Machine-readable benchmark](week7_final_benchmark.csv)
- [Model comparison](week7_final_model_comparison.png)
- [Confusion matrices](week7_final_confusion_comparison.png)
- [Random Forest feature importance](week7_final_feature_importance.png)
- [ESI 1 complaint analysis](week7_final_esi1_complaints.png)
- [Decision journal](decisions/2026-week-7-model-choice.md)
