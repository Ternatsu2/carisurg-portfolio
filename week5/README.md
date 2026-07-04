# Week 5: AI-Assisted Triage Data Exploration

This folder contains my Week 5 final work for the clinical triage feasibility task. I used the TenX Week 5 triage CSV and focused on whether the data is ready for a first baseline triage-support model.

## Main Files

- "notebooks/week5_final_triage_profile.ipynb": full exploration notebook.
- "reports/week5_final_feasibility_memo.md": final feasibility memo for the ED Board.
- "reports/week5_top10_feature_shortlist.csv": ranked feature shortlist with clinical reasons.
- "outputs/week5_data_quality_dashboard.svg": four-plot data quality dashboard.
- "outputs/week5_missingness_summary.svg": missingness check.
- "outputs/week5_feature_signal_summary.svg": feature signal plot.
- "outputs/week5_chief_complaint_distribution.svg": chief complaint distribution.
- "outputs/week5_demographics_review.svg": race and ethnicity field review.
- "data/column_schema.csv": schema and missingness table.
- "data/yaleemmlc_triage_sample.csv": small sample for structure review.

## Data Note

The full CSV is not committed because it is a large clinical dataset. The notebook expects the full file at the programme data path or a local path supplied by the user.
