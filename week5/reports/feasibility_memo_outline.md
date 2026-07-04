# Week 5 Interim Feasibility Memo Outline

Student: Terry Benjamin Jr.  
Case pack: FraudShield AI, AC-1589269 and AC-4471021

## 1. Working Question

Can a small fraud review dataset support a first-pass analyst workflow that profiles account risk evidence, highlights missing fields, and points reviewers toward cases that need enhanced KYC or source-of-funds review?

## 2. Data Reviewed

I reviewed two provided files:

- Evidence summary for account AC-1589269, with six evidence records tied to risk score, account status, wallet activity, geolocation activity, and betting activity.
- Wallet import sample for account AC-4471021, with five transaction rows covering deposits and withdrawals.

The evidence summary has no missing fields. The wallet import sample has two missing card BIN values, both on ACH withdrawal rows. I treated those as expected missingness for that payment type, not as a failed data entry issue.

## 3. Early Feasibility Read

The dataset can support a narrow interim prototype. A reviewer could use it to check whether each case has enough structured evidence for a fraud review note, identify fields that need follow-up, and separate expected missingness from missingness that blocks a decision.

The evidence summary already contains useful case-level signals: account status, risk score, wallet activity, geolocation spread, and betting activity. The wallet import file adds transaction-level detail, but the sample is too small for model training or serious benchmarking.

## 4. Missingness and Data Quality Risks

The main missingness issue is context-dependent. A blank card BIN on an ACH withdrawal makes sense because ACH does not use a card BIN. A blank card BIN on a card deposit would need follow-up.

The current case pack also has bigger feasibility gaps:

- No separate chargeback or dispute table is included.
- Withdrawal destination details are limited.
- KYC documents, source-of-funds files, and customer messages are not loaded.

Those gaps matter because a fraud system should support the analyst, not make a final enforcement decision from partial evidence.

## 5. Proposed Interim Workflow

1. Load the evidence summary and wallet import files.
2. Check row counts, column types, duplicates, missing values, and key value ranges.
3. Create a missingness visualisation for both files.
4. Flag missingness by field and business meaning.
5. Produce an analyst-facing feasibility note with what the data can support and what still needs human review.

## 6. Next Steps for the Final Submission

For the final Week 5 deliverable, I would expand this into a cleaner feasibility report and notebook. I would also add simple validation rules, such as checking that deposits with card payment brands have card BIN values, withdrawals have plausible amounts, and each evidence row links back to the expected account.
