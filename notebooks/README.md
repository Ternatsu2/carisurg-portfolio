# Notebooks

Week 0 notebooks:

- `day1_clean_gender.ipynb`: cleans the Gender column and checks the mapped values.
- `day2_clean_pulse.ipynb`: cleans GCS, SBP, Temp, and Pulse.
- `day3_visualization.ipynb`: creates a Pulse histogram and an Age vs Pulse scatter plot.

These notebooks expect the reduced emergency triage dataset from the programme.

Week 5 through Week 7 notebooks:

- `week5_final_triage_profile.ipynb`: profiles the full triage dataset and identifies data quality risks.
- `week6_final_baseline_models.ipynb`: trains the Week 6 baselines, selects class-weight and tree settings on an inner validation split, evaluates once on the held-out test set, and reviews the ESI 1 errors.
- `week7_interim_complex_model.ipynb`: adds and tunes Random Forest models on the unchanged Week 6 split, benchmarks performance and timing, and saves the draft comparison artefacts.
