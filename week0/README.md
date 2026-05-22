# Week 0

This folder contains the onboarding work for Week 0.

Current notebook:

- notebooks/day1_clean_gender.ipynb
- notebooks/day2_clean_pulse.ipynb
- notebooks/day3_visualization.ipynb

The Day 1 notebook loads the reduced emergency triage dataset, checks the original "Gender" values, maps the known variants to "1" and "0", and checks the result.

The Day 2 notebook cleans GCS, SBP, Temp, and Pulse. Pulse is cleaned by converting values to numbers, replacing values outside the valid range with missing values, and filling them with the median.

The Day 3 notebook uses the cleaned Pulse column for one histogram and one scatter plot.
