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

Tyler et al. reviewed whether AI and machine learning can improve emergency department triage, where crowding and subjective prioritisation can delay care. They ran a structured search of EMBASE, Ovid MEDLINE, and Web of Science, then selected 29 peer-reviewed primary-data studies from 2013 to 2023 after screening and appraisal. The review found that machine learning models often outperformed conventional triage systems for discrimination, risk assessment, hospitalisation prediction, and resource allocation. The main limitations were that the evidence depended heavily on retrospective studies, single-site datasets, missing-data exclusions, and limited proof that models would change clinician behaviour safely in live triage settings.

Da'Costa et al. reviewed AI-driven triage systems as a response to ED overcrowding, resource pressure, and inconsistent patient prioritisation. Their narrative review drew on peer-reviewed papers published between 2015 and 2024 from PubMed, Scopus, IEEE Xplore, and Google Scholar. They reported potential benefits such as better patient prioritisation, reduced waiting times, and improved resource allocation, but they also treated data quality, algorithmic bias, clinician trust, and ethical concerns as major barriers to adoption. For this project, the key limitation is that the review explains what AI triage could support, but it does not prove that a model will work in a specific local ED workflow without validation and clinician buy-in.

Araouchi and Adda built TriageIntelli to address ED overcrowding and the pressure placed on triage systems by ageing populations and more complex cases. They evaluated Support Vector Machines, Random Forests, Artificial Neural Networks, Gradient Boosting Machines, Linear Regression, XGBoost, and a stacking model for predicting Korean Triage and Acuity Scale levels. The reported results were promising, with SVM and GBM reaching accuracies of 79% and 78.7%, while the stacking model reached 80.05% accuracy, 80.27% precision, 73.26% recall, and a 74.41% F1-score. The main limitation for this project is generalisation: the model is tied to KTAS-style data and needs testing across different demographics, seasons, hospital contexts, and triage workflows before it could support a Caribbean ED.

Chang et al. studied whether machine learning and natural language processing could predict ED disposition better than physician judgement based on triage data alone. They used retrospective non-trauma adult ED data from two Taiwanese hospitals, combining structured triage variables with free-text notes processed through NLP, then compared six machine learning models and a triage-level logistic regression model. The primary outcome was death in the ED or ICU admission, and the secondary outcome was general ward admission or transfer to another hospital. All machine learning models had higher F1 scores than the emergency physician benchmark and the triage-level-only model, while Random Forest performed well on calibration and external validation. The authors still noted important limits: rare outcomes were hard to learn, some confounders were unavailable at triage, and using only two neighbouring hospitals limited generalisability.

Porto reviewed machine learning and NLP approaches for ED triage classification using PRISMA methods across Web of Science, PubMed, Scopus, IEEE Xplore, and ACM Digital Library. The review included 60 studies and 57 algorithms, with Logistic Regression appearing most often while XGBoost, Gradient Boosting, LightGBM, and deep neural networks showed strong performance. Common predictors included demographics, vital signs, oxygen saturation, chief complaint, systolic blood pressure, age, and mode of arrival. The review concluded that ML models can outperform traditional triage approaches for classification, mortality prediction, and ICU admission prediction. Its limitation was the evidence base: the studies were too heterogeneous for meta-analysis, many had high risk of bias, few were prospective, and explainable AI was still underused.

## Early Gap Direction

The papers point to two gaps that fit a 12-week pilot. First, AI triage models often report performance in one dataset or health-system context, so a Caribbean ED needs a small validation-focused project before anyone can trust the results locally. Second, model accuracy alone does not answer the workflow question: a useful tool has to show a triage nurse why a patient was flagged and let the clinician accept or reject that signal. Chang et al. and Porto make this clearer because they show both sides of the issue: stronger models can improve prediction, but generalisability, explainability, and clinical acceptance still decide whether the work can be used safely.

## References

1. Tyler S, Olis M, Aust N, Patel L, Simon L, Triantafyllidis C, et al. Use of Artificial Intelligence in Triage in Hospital Emergency Departments: A Scoping Review. Cureus. 2024;16(5):e59906. doi:10.7759/cureus.59906.
2. Da'Costa A, Teke J, Origbo JE, Osonuga A, Egbon E, Olawade DB. AI-driven triage in emergency departments: A review of benefits, challenges, and future directions. International Journal of Medical Informatics. 2025;197:105838. doi:10.1016/j.ijmedinf.2025.105838.
3. Araouchi Z, Adda M. TriageIntelli: AI-Assisted Multimodal Triage System for Health Centers. Procedia Computer Science. 2024;251:430-437. doi:10.1016/j.procs.2024.11.130.
4. Chang YH, Lin YC, Huang FW, Chen DM, Chung YT, Chen WK, et al. Using machine learning and natural language processing in triage for prediction of clinical disposition in the emergency department. BMC Emergency Medicine. 2024;24:237. doi:10.1186/s12873-024-01152-1.
5. Porto BM. Improving triage performance in emergency departments using machine learning and natural language processing: a systematic review. BMC Emergency Medicine. 2024;24:219. doi:10.1186/s12873-024-01135-2.
