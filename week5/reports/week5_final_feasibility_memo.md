# Week 5 Final Feasibility Memo: FraudShield Reviewer Triage

Student: Terry Benjamin Jr.  
Case pack: FraudShield AC-1589269 evidence summary and AC-4471021 wallet import sample  
Submission date: 4 July 2026

## 1. Project Question

Can the provided FraudShield files support a reviewer-facing fraud triage workflow that profiles case evidence, checks data quality, shortlists useful features, and gives an analyst enough context to decide whether enhanced KYC or source-of-funds review is needed?

## 2. Data Reviewed

I reviewed two files. The evidence summary belongs to case AC-1589269 and contains six evidence records covering account status, wallet activity, cash movement, device and location behaviour, and betting activity. The wallet import sample belongs to AC-4471021 and contains five transaction rows with deposits, withdrawals, payment brand, card BIN, amount, and chargeback-linked fields.

The account IDs do not match, so I treated the wallet import as a separate sample. Joining it directly to AC-1589269 would create a bad data link. That matters because a reviewer tool should preserve evidence traceability instead of making the case look stronger than it really is.

## 3. Exploration Summary

The evidence summary is small but useful. It shows that AC-1589269 is under review, has 501 deposits totalling 30,577.94, 174 withdrawals totalling 19,035.22, and 163 withdrawals within 24 hours of a previous deposit. It also records five devices, 277 IP addresses, seven cities, and 19,936 bets with 313,143.36 total stake.

The wallet import sample is too small to model from, but it is still useful for data-quality checks. It has no duplicate wallet row IDs, all timestamps parsed, all transaction amounts were positive, and card deposits had card BIN values present. The two missing card BIN values were both on ACH withdrawals, where a card BIN is not expected.

## 4. Data Quality Dashboard Findings

The final dashboard checks four things:

- Missingness by file and field.
- Wallet activity over time in the sample import.
- Evidence source coverage across the case summary.
- Feature readiness for the top-10 shortlist.

The main data-quality finding is not simple missingness. It is data context. A blank card BIN is acceptable for an ACH withdrawal, but it would be a problem for a card deposit. The larger gap is that important review tables are not present, including a separate chargeback or dispute table, withdrawal destination details, KYC documents, source-of-funds documents, and customer correspondence.

## 5. Top-10 Feature Shortlist

| Feature | Source | Current support | Why it matters |
|---|---|---|---|
| account_status_under_review | Evidence summary | Ready now | Sets the review queue and keeps the case from being treated as normal traffic. |
| kyc_status_unknown | Analyst note | Needs structured KYC field | Unknown KYC status changes the reviewer action from payout release to enhanced identity review. |
| risk_score | Analyst note | Ready for display, not enough for training | A 62 out of 100 score gives a case-level prior, but it still needs evidence-level reasons. |
| deposit_total | Evidence summary | Ready now | High funding volume can trigger source-of-funds review. |
| withdrawal_total | Evidence summary | Ready now | High payout movement creates exposure if the account later fails review. |
| withdrawal_to_deposit_ratio | Evidence summary | Ready now | A 62 percent withdrawal-to-deposit ratio shows cash-out pressure. |
| fast_withdrawals_24h | Evidence summary | Ready now | Withdrawals soon after deposits are one of the clearest review triggers in this pack. |
| payment_instrument_pattern | Wallet import | Prototype only | Repeated card BINs, ACH withdrawals, and chargeback-linked deposits help a reviewer inspect funding behaviour. |
| device_ip_city_spread | Evidence summary | Ready now | Five devices, 277 IPs, and seven cities may point to access churn, proxy use, travel, or account sharing. |
| betting_volume_and_rejected_wagers | Evidence summary | Ready now | Bet count, total stake, and rejected wagers help compare payment behaviour with platform usage. |

## 6. Feasibility Decision

This case pack can support a narrow reviewer-facing prototype. A useful first version would show a case profile, evidence IDs, a data-quality panel, the top feature signals, and a short reviewer note explaining why enhanced KYC or source-of-funds review is reasonable.

It cannot support reliable model training yet. There is only one case summary and a five-row wallet sample, the wallet sample belongs to a different account, there are no confirmed fraud or non-fraud labels, and several important review tables are missing. A model built from this alone would not be defensible.

## 7. Safety and Reviewer Framing

I would treat the tool as decision support. The clinical parallel is triage: flag urgency and uncertainty, then leave the final decision to a trained reviewer. It should organise the evidence, show what is missing, and help the analyst move faster. It should not approve, restrict, or clear an account by itself.

The reviewer should always see the reason behind a flag and the data gap behind a weak recommendation. For this case, the strongest defensible action is not an automatic fraud decision. It is escalation for enhanced KYC and source-of-funds review before clearing payout activity.

## 8. Next Build Step

The next step would be to load more cases with consistent account IDs, raw wallet transactions, chargeback or dispute outcomes, KYC status, withdrawal destination details, and final analyst decisions. With those fields in place, the project could move from a case-review dashboard into a measurable triage model.
