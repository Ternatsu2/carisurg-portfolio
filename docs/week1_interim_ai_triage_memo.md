# Week 1 Interim Memo: AI-Assisted Emergency Triage

Student: Terry Benjamin Jr.  
Programme: CariSurg MedTech Pathways, Healthcare AI  
Date: 6 June 2026

## Working Project Direction

I am treating AI-assisted emergency triage as clinician-facing decision support. The useful question for this project is whether a small prototype can help flag higher-risk patients from routine triage information while still leaving the final triage decision with the clinician.

## Draft Problem Statement

Emergency triage in busy EDs depends on rapid judgement from nurses working with incomplete data, crowding, and limited resources. Recent AI triage studies report improved prediction of acuity, disposition, and critical care need, but many models rely on retrospective or single-setting datasets and do not show how they would fit Caribbean ED workflows. This pilot will test whether a clinician-in-the-loop triage support prototype can flag high-risk patients from routine triage variables while keeping the nurse responsible for the final decision.

Word count: 80

## Research Paper Summaries

Tyler and colleagues studied whether machine learning could improve ED triage where crowding and subjective prioritisation delay care. They reviewed 29 primary-data studies from 2013 to 2023 found through EMBASE, Ovid MEDLINE, and Web of Science. The review reported better discrimination, risk assessment, hospitalisation prediction, and resource allocation than conventional triage, but the authors noted retrospective single-site data, missing-data exclusions, and limited evidence from live clinical use.

Da'Costa and colleagues reviewed AI-driven triage as a response to ED overcrowding, resource pressure, and inconsistent patient prioritisation. They drew on peer-reviewed work from 2015 to 2024 across PubMed, Scopus, IEEE Xplore, and Google Scholar. The review reported potential gains in prioritisation, waiting times, and resource allocation, but highlighted data quality, bias, clinician trust, and ethics as barriers that require local validation.

Araouchi and Adda built TriageIntelli to predict ED acuity in the context of overcrowding and increasingly complex patient presentations. They compared SVM, Random Forest, neural network, GBM, linear regression, XGBoost, and stacking models for Korean Triage and Acuity Scale prediction. SVM and GBM reached about 79% accuracy and the stacking model reached 80.05% accuracy, but the approach still needs testing across other demographics, seasons, hospitals, and triage workflows before use in a Caribbean ED.

Chang and colleagues studied whether machine learning and NLP could predict ED disposition from triage data better than physician judgement. They used retrospective adult non-trauma data from two Taiwanese hospitals, combining structured variables with free-text notes and comparing six machine learning models against a triage-level logistic regression baseline and physician benchmark. The models had higher F1 scores than the benchmarks and Random Forest performed well on calibration and external validation, but rare outcomes, missing confounders, and the two-hospital setting limited generalisability.

Porto reviewed ML and NLP methods for ED triage classification using PRISMA across Web of Science, PubMed, Scopus, IEEE Xplore, and ACM Digital Library. The review covered 60 studies and 57 algorithms, with common predictors including demographics, vital signs, oxygen saturation, chief complaint, blood pressure, age, and mode of arrival. The review found that ML can outperform traditional approaches for triage classification, mortality prediction, and ICU admission prediction, but the evidence was heterogeneous, often biased, rarely prospective, and weak on explainability.

## Early Gap Direction

The papers point to two gaps that fit a 12-week pilot. First, AI triage models often report performance in one dataset or health-system context, so a Caribbean ED needs a small validation-focused project before anyone can trust the results locally. Second, model accuracy alone does not answer the workflow question: a useful tool has to show a triage nurse why a patient was flagged and let the clinician accept or reject that signal. These gaps fit the timeframe because the pilot can use published or simulated triage variables, build a small decision-support prototype, and test the explanation output without using real patient data or live deployment. Chang et al. and Porto make this clearer because they show both sides of the issue: stronger models can improve prediction, but generalisability, explainability, and clinical acceptance still decide whether the work can be used safely.

## AI Tool Use

I used AI tools as a checklist after reading the papers. I checked whether each summary covered the problem, method, outcome, and limitation, then revised the wording myself and checked the references against the paper records. I did not use real patient data.

## References

1. Tyler S, Olis M, Aust N, Patel L, Simon L, Triantafyllidis C, et al. Use of Artificial Intelligence in Triage in Hospital Emergency Departments: A Scoping Review. Cureus. 2024;16(5):e59906. doi:10.7759/cureus.59906.
2. Da'Costa A, Teke J, Origbo JE, Osonuga A, Egbon E, Olawade DB. AI-driven triage in emergency departments: A review of benefits, challenges, and future directions. International Journal of Medical Informatics. 2025;197:105838. doi:10.1016/j.ijmedinf.2025.105838.
3. Araouchi Z, Adda M. TriageIntelli: AI-Assisted Multimodal Triage System for Health Centers. Procedia Computer Science. 2024;251:430-437. doi:10.1016/j.procs.2024.11.130.
4. Chang YH, Lin YC, Huang FW, Chen DM, Chung YT, Chen WK, et al. Using machine learning and natural language processing in triage for prediction of clinical disposition in the emergency department. BMC Emergency Medicine. 2024;24:237. doi:10.1186/s12873-024-01152-1.
5. Porto BM. Improving triage performance in emergency departments using machine learning and natural language processing: a systematic review. BMC Emergency Medicine. 2024;24:219. doi:10.1186/s12873-024-01135-2.
