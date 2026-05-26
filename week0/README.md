# Week 0

This folder contains the onboarding work for Week 0.

## Notebooks

- notebooks/day1_clean_gender.ipynb
- notebooks/day2_clean_pulse.ipynb
- notebooks/day3_visualization.ipynb

The Day 1 notebook loads the reduced emergency triage dataset, checks the original "Gender" values, maps the known variants to "1" and "0", and checks the result.

The Day 2 notebook cleans GCS, SBP, Temp, and Pulse. Pulse is cleaned by converting values to numbers, replacing values outside the valid range with missing values, and filling them with the median.

The Day 3 notebook uses the cleaned Pulse column for one histogram and one scatter plot.

## Reports

- reports/assignment4_vital_sign_description.pdf
- reports/assignment5_unconsidered_metrics.pdf
- reports/assignment6_triage_pseudocode.pdf

Assignment 4 describes Pulse as a triage vital sign. Assignment 5 explains why SpO2 should be included as another triage measure. Assignment 6 ties the Week 0 vital signs into a rule-based triage pseudocode design.
