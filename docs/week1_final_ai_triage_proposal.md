# Week 1 Final Proposal: AI-Assisted Emergency Triage

Student: Terry Benjamin Jr.  
Programme: CariSurg MedTech Pathways, Healthcare AI  
Date: 8 June 2026

## Project Direction

I am focusing on AI-assisted emergency triage as clinician-facing decision support. The prototype would help a triage nurse read routine patient information, flag patients who may need faster review, show why it flagged them, and leave the final decision with the clinician.

## Problem Statement

Emergency triage in busy EDs depends on rapid judgement from nurses working with incomplete data, crowding, and limited resources. Recent AI triage work reports improved prediction of acuity, disposition, and critical care need, but many studies rely on retrospective or single-setting datasets (Da'Costa et al., 2025; Porto, 2024; Tyler et al., 2024). This pilot will test whether clinician-in-the-loop support can flag high-risk patients from routine triage variables while keeping nurses responsible for the final decision.

Word count: 75

## Literature Summaries

Tyler et al. (2024) reviewed how AI and machine learning have been used in hospital emergency department triage. The problem they addressed was the pressure on ED staff to prioritise patients accurately during crowding, where subjective triage decisions can delay care or misclassify acuity. They reviewed 29 primary-data studies published between 2013 and 2023 and found that AI methods showed promise for risk assessment, patient prioritisation, hospitalisation prediction, and operational planning. Their main limitation was that much of the evidence came from retrospective or narrow datasets, with limited proof that these systems work safely in live triage workflows.

Da'Costa et al. (2025) reviewed AI-driven triage as a response to ED overcrowding, resource constraints, and variability in patient prioritisation. They synthesised peer-reviewed work from 2015 to 2024 across PubMed, Scopus, IEEE Xplore, and Google Scholar. The review found potential benefits in patient prioritisation, wait-time reduction, and resource allocation, especially when systems use real-time data such as vital signs, symptoms, and medical history. The authors also highlighted major barriers: poor data quality, algorithmic bias, clinician trust, ethical concerns, and the difficulty of integrating AI into real ED practice.

Araouchi and Adda (2024) built TriageIntelli, an AI-assisted multimodal triage system designed to predict triage levels in health centres. Their work addressed ED overcrowding and increasing case complexity by comparing several models, including SVM, Random Forest, neural networks, GBM, XGBoost, linear regression, and a stacking model. The strongest individual models were SVM and GBM, with accuracy around 79%, while the stacking model reached 80.05% accuracy. The study supports the idea that routine triage data can predict acuity, but the model still needs validation across different hospitals, patient populations, and clinical settings before anyone could treat it as reliable decision support.

Chang et al. (2024) studied whether machine learning and natural language processing could predict ED disposition from triage data more effectively than physician judgement alone. They used retrospective adult non-trauma data from two Taiwanese hospitals and combined structured data with free-text triage notes. Their models improved prediction of discharge, ward admission, and ICU admission, and the authors argued that combining structured vitals with unstructured clinical notes gave a fuller picture of patient risk. The study still had limits: rare outcomes were hard to learn, some confounders were unavailable at triage, and the two-hospital setting reduces generalisability.

Porto (2024) conducted a systematic review of machine learning and natural language processing methods for ED triage classification. The review followed PRISMA guidelines and included 60 studies covering 57 algorithms, with common predictors including demographics, vital signs, oxygen saturation, chief complaint, blood pressure, age, and mode of arrival. The review found that machine learning can improve triage classification and prediction of mortality or ICU admission, and that NLP can strengthen models by using nursing notes or chief complaints. At the same time, Porto found high risk of bias in many prediction studies, limited explainability work, and heavy reliance on retrospective data.

Cha and Kim (2025) reviewed ethical and legal issues around AI in emergency medicine triage and resource allocation. They searched literature after January 2020 and analysed 27 papers using a scoping review approach. The review found recurring concerns around data privacy, algorithmic bias, automation dependency, accountability, and explainability, with human-in-the-loop design and continuous validation appearing as common safeguards. The authors also found that patient and public involvement, social validation, generative AI risks, and persuasive AI risks have not been addressed deeply enough.

## Gaps Identified

### Gap 1: Local validation is missing for Caribbean-style ED workflows

The literature shows strong model performance in selected datasets, but it does not prove that the same models would behave well in a Caribbean ED. Porto (2024) found that many studies were retrospective, and Tyler et al. (2024) also showed that much of the field still tests models on existing data rather than live workflows. Chang et al. (2024) improved prediction by using structured data and triage notes, but their data came from two Taiwanese hospitals. Da'Costa et al. (2025) also warned that data quality and workflow integration remain barriers.

This matters because triage is shaped by local staffing, documentation habits, equipment, patient mix, and resource limits. A model trained or tested in a high-resource hospital may flag risk differently in a setting with different admission thresholds, bed pressure, transport delays, or missing clinical fields. The actionable gap is to test a small triage-support prototype against the kind of variables available in this programme, then make the limits visible instead of presenting the model as generally valid.

### Gap 2: Accuracy alone does not give nurses enough reason to trust the output

Several studies report accuracy, AUROC, F1 score, or similar metrics, but those numbers do not tell a triage nurse why a specific patient was flagged. Araouchi and Adda (2024) showed that model stacking can improve performance, and Chang et al. (2024) showed that NLP can improve disposition prediction, but neither result solves the bedside question of how a clinician should interpret one alert. Porto (2024) noted that explainable AI remains underexplored in this field. Cha and Kim (2025) also identified explainability, accountability, automation dependency, and human-in-the-loop design as key ethical concerns.

This matters because a hidden score can create two opposite risks. A nurse may ignore it because it gives no useful reason, or may over-trust it because it looks technical. A useful triage support tool should show the specific factors behind a flag, such as low SpO2, abnormal respiratory rate, hypotension, concerning chief complaint, or age plus abnormal vitals. It should also let the nurse override the system and record why.

## Proposed Solution

I propose a clinician-in-the-loop triage support prototype for routine ED triage data. The prototype would take structured triage variables such as age, sex if available, presenting complaint, mode of arrival, pulse, respiratory rate, blood pressure, temperature, SpO2, GCS, and pain score. Those variables match common predictors used in ED triage modelling, including vitals, chief complaint, blood pressure, oxygen saturation, age, and mode of arrival (Chang et al., 2024; Porto, 2024). It would output a risk band, a short explanation, and a recommended review priority. The output would stay framed as decision support, not a final diagnosis or autonomous triage decision.

The first version should combine a transparent rule-based baseline with a simple machine learning model if the Week 5 dataset supports it. The rule baseline would flag clinically defendable patterns such as severe hypoxia, very low GCS, hypotension, abnormal respiratory rate, fever with abnormal vitals, or multiple moderate abnormalities together. The model baseline could then be compared against those rules using sensitivity, specificity, precision, recall, confusion matrices, and calibration checks. This fits the literature because recent work has tested several machine learning approaches for triage, but reviewers still warn that many results come from retrospective datasets and need stronger validation before use in practice (Araouchi & Adda, 2024; Porto, 2024; Tyler et al., 2024).

The prototype should show its reasoning in plain language. For example, a patient might be flagged because "SpO2 is below 90%" or because "respiratory rate and pulse are both outside expected adult ranges." The nurse would see the flag, the reasons, and an option to accept, reject, or mark the case for review. The system should log overrides because those decisions are useful for later error analysis and for understanding where the model disagrees with clinical judgement. That human-in-the-loop design responds to published concerns about explainability, accountability, automation dependency, and clinician trust (Cha & Kim, 2025; Da'Costa et al., 2025; Porto, 2024).

This design answers the two gaps directly. Local validation is handled by testing the prototype on the dataset available in the programme and reporting where the data is too limited. Trust and explainability are handled by showing reason codes, keeping a human in the loop, and making the system's uncertainty visible (Cha & Kim, 2025; Da'Costa et al., 2025). It also fits the 12-week programme because it can be built as a small Python and GitHub-based project without real patient data or live deployment.

## Expected Output for the Portfolio Project

By the end of the project, the portfolio artefact could include:

- A cleaned triage dataset or synthetic triage-style dataset with documented assumptions.
- A rule-based triage risk baseline.
- A simple predictive model, if the dataset supports supervised learning.
- Evaluation tables showing where the system over-flags and under-flags risk.
- A small interface or notebook view that shows the patient risk band and the reasons for the flag.
- A README explaining the clinical limits, data limits, ethical safeguards, and why the tool must remain clinician-facing decision support.

## References

Araouchi, Z., & Adda, M. (2024). TriageIntelli: AI-assisted multimodal triage system for health centers. *Procedia Computer Science, 251*, 430-437. https://doi.org/10.1016/j.procs.2024.11.130

Cha, H., & Kim, J. (2025). Ethical considerations of artificial intelligence in emergency medicine for triage and resource allocation: A scoping review. *Clinical and Experimental Emergency Medicine, 12*(4), 306-319. https://doi.org/10.15441/ceem.25.199

Chang, Y.-H., Lin, Y.-C., Huang, F.-W., Chen, D.-M., Chung, Y.-T., Chen, W.-K., & Wang, C. C. N. (2024). Using machine learning and natural language processing in triage for prediction of clinical disposition in the emergency department. *BMC Emergency Medicine, 24*, Article 237. https://doi.org/10.1186/s12873-024-01152-1

Da'Costa, A., Teke, J., Origbo, J. E., Osonuga, A., Egbon, E., & Olawade, D. B. (2025). AI-driven triage in emergency departments: A review of benefits, challenges, and future directions. *International Journal of Medical Informatics, 197*, Article 105838. https://doi.org/10.1016/j.ijmedinf.2025.105838

Porto, B. M. (2024). Improving triage performance in emergency departments using machine learning and natural language processing: A systematic review. *BMC Emergency Medicine, 24*, Article 219. https://doi.org/10.1186/s12873-024-01135-2

Tyler, S., Olis, M., Aust, N., Patel, L., Simon, L., Triantafyllidis, C., Patel, V., Lee, D. W., Ginsberg, B., Ahmad, H., & Jacobs, R. J. (2024). Use of artificial intelligence in triage in hospital emergency departments: A scoping review. *Cureus, 16*(5), Article e59906. https://doi.org/10.7759/cureus.59906
