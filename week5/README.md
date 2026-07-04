# Week 5: FraudShield Data Profiling and Feasibility

This folder contains my Week 5 interim and final work for the FraudShield case pack. The final submission focuses on whether the provided files can support a reviewer-facing fraud triage workflow.

## Final Deliverable

- `notebooks/week5_final_fraudshield_profile.ipynb`: final exploration notebook.
- `outputs/week5_data_quality_dashboard.svg`: data quality dashboard for missingness, evidence coverage, wallet sample checks, and feature readiness.
- `outputs/data_quality_checks.csv`: validation checks produced by the notebook.
- `reports/top10_feature_shortlist.csv`: feature shortlist with source, current support, reviewer reasoning, and governance notes.
- `reports/week5_final_feasibility_memo.md`: final feasibility memo.

## Interim Work

- `notebooks/week5_interim_data_profile.ipynb`: initial data profile.
- `outputs/missingness_summary.svg`: interim missingness visualisation.
- `reports/feasibility_memo_outline.md`: interim feasibility memo outline.

## Data Files

- `data/evidence_summary_ac_1589269.csv`: case evidence summary for AC-1589269.
- `data/wallet_import_ac_4471021.csv`: wallet import sample for AC-4471021.

## Data Note

The evidence summary and wallet import sample use different account IDs. I kept them separate and did not join them as one account. The files come from the provided FraudShield sample materials, and I did not add private credentials, personal files, or external customer records.
