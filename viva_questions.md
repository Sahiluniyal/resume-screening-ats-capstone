# Viva Questions and Answers

# Resume Screening and Role Matching using NLP

**Company:** TalentBridge Solutions Pvt. Ltd.

**Project Type:** Data Science with GenAI Capstone Project

**Prepared By:** Sahil Uniyal

---

# Project Understanding

## 1. What is the objective of this project?

**Answer:**

The objective of this project is to automate resume screening and candidate-role matching using Natural Language Processing (NLP), Feature Engineering, and a Hybrid ATS Scoring Engine. The system helps recruiters identify the most suitable candidates efficiently while reducing manual effort and improving consistency in hiring.

---

## 2. Why did you choose this project?

**Answer:**

Resume screening is a real-world business problem faced by almost every organization. This project allowed me to apply Data Science, NLP, and Business Analytics to solve a practical recruitment challenge.

---

## 3. What business problem does this project solve?

**Answer:**

It reduces manual resume screening time, improves candidate-role matching, minimizes recruiter bias, and provides consistent and explainable candidate recommendations.

---

## 4. Who are the stakeholders?

**Answer:**

- Recruiters
- Hiring Managers
- HR Operations Team
- Business Leadership
- Technology & Analytics Team

---

## Dataset Questions

## 5. Which dataset did you use?

**Answer:**

The project uses `parsed_resumes.csv`, which contains 5000 structured candidate profiles with 34 attributes. The Data Definition.xlsx file was used to understand the meaning of each column.

---

## 6. Why was data validation necessary?

**Answer:**

Data validation ensures data quality by checking for missing values, duplicate records, incorrect data types, inconsistent education values, incomplete profiles, and skill formatting issues before building the model.

---

## 7. What validation checks did you perform?

**Answer:**

- Missing Value Analysis
- Duplicate Detection
- Resume Completeness Validation
- Keyword Density Validation
- Education Standardization
- Skill Normalization
- Data Type Verification

---

## Feature Engineering

## 8. What is Feature Engineering?

**Answer:**

Feature Engineering is the process of creating new meaningful features from existing data to improve model performance and business interpretation.

---

## 9. Name some engineered features.

**Answer:**

- Resume Quality Score
- ATS Readiness Score
- Technical Strength Score
- Leadership Score
- Domain Alignment Score
- Project Relevance Score
- Candidate Quality Index

---

## 10. Which engineered feature is the most important?

**Answer:**

Candidate Quality Index (CQI) because it combines multiple business-driven scores into one overall measure of candidate quality.

---

## NLP Questions

## 11. What is NLP?

**Answer:**

Natural Language Processing is a branch of Artificial Intelligence that enables computers to understand, process, and analyze human language.

---

## 12. Why did you use NLP in this project?

**Answer:**

Candidate resumes contain textual information such as skills, projects, and experience summaries. NLP helps compare this information with enterprise job role descriptions.

---

## 13. What preprocessing steps did you perform?

**Answer:**

- Lowercase conversion
- Special character removal
- Stopword removal
- Tokenization
- Text normalization

---

## 14. What is TF-IDF?

**Answer:**

TF-IDF (Term Frequency–Inverse Document Frequency) converts text into numerical vectors while assigning higher importance to unique and meaningful words.

---

## 15. Why did you choose TF-IDF?

**Answer:**

It is simple, efficient, interpretable, and works well for structured textual datasets like parsed resumes.

---

## 16. What is Cosine Similarity?

**Answer:**

Cosine Similarity measures the similarity between two text vectors. A higher similarity score indicates better alignment between a resume and a job role.

---

## ATS Scoring

## 17. What is ATS?

**Answer:**

ATS stands for Applicant Tracking System. It is software used by organizations to manage recruitment and filter resumes.

---

## 18. How is the Final ATS Score calculated?

**Answer:**

The Final ATS Score combines:

- Skill Match
- Experience Match
- Project Relevance
- Education Match
- ATS Readiness
- Leadership Score

into a single score between 0 and 100.

---

## 19. Why use a Hybrid ATS Scoring model?

**Answer:**

Keyword matching alone is insufficient. The hybrid approach combines business rules and NLP similarity, producing more balanced and explainable candidate rankings.

---

## Dashboard

## 20. Why did you build a Streamlit dashboard?

**Answer:**

The dashboard provides recruiters with an easy-to-use interface for viewing candidate rankings, searching profiles, role matching, and recruitment analytics.

---

## 21. What modules are available in the dashboard?

**Answer:**

- Executive Dashboard
- Candidate Search
- Role Matching
- Top Candidates
- Analytics

---

## Machine Learning & Technical

## 22. Did you train a Machine Learning model?

**Answer:**

No. This project primarily uses NLP similarity and a Hybrid ATS Scoring Engine because the dataset does not contain labeled hiring outcomes required for supervised learning.

---

## 23. Why didn't you use Deep Learning?

**Answer:**

Deep Learning models such as BERT require larger datasets, higher computational resources, and labeled data. For this capstone, TF-IDF provided a simpler and more explainable solution.

---

## 24. Why didn't you use ChatGPT or an LLM directly?

**Answer:**

The objective was to demonstrate a traditional NLP-based recruitment pipeline using structured data. Large Language Models are identified as a future enhancement.

---

## Business Questions

## 25. What are the business benefits of this project?

**Answer:**

- Faster screening
- Reduced recruiter workload
- Better candidate matching
- Improved hiring consistency
- Lower recruitment costs

---

## 26. What limitations does this project have?

**Answer:**

- Structured CSV data only
- No PDF parsing
- No real recruiter feedback
- No historical hiring labels
- No cloud deployment

---

## 27. How can this project be improved?

**Answer:**

Future enhancements include:

- Resume PDF Parsing
- BERT Embeddings
- Sentence Transformers
- LLM Integration
- Explainable AI
- Cloud Deployment
- Real-time ATS Integration

---

## Personal Questions

## 28. What was your biggest learning?

**Answer:**

I learned how Data Science, NLP, and Feature Engineering can be combined to solve real-world Human Resource Analytics problems through an end-to-end project.

---

## 29. Which part of the project was most challenging?

**Answer:**

Designing meaningful business-driven engineered features and building a balanced ATS scoring system that combines multiple evaluation criteria.

---

## 30. If you had one more month, what would you improve?

**Answer:**

I would implement PDF resume parsing, integrate transformer-based models such as BERT, deploy the application on the cloud, and add recruiter feedback to continuously improve recommendation accuracy.

---

# Final Interview Question

## 31. Explain your complete project in two minutes.

**Answer:**

This project is an enterprise-style Resume Screening and Role Matching System developed for TalentBridge Solutions. It uses a dataset of 5000 structured candidate profiles. First, the data is validated and cleaned to ensure quality. Then, several business-driven features such as Resume Quality Score, ATS Readiness Score, Technical Strength Score, Leadership Score, and Candidate Quality Index are created through feature engineering.

Next, Natural Language Processing techniques including text preprocessing, TF-IDF vectorization, and Cosine Similarity are used to compare candidate resumes with five predefined enterprise job roles. A Hybrid ATS Scoring Engine combines NLP similarity with business metrics to generate a Final Fit Score for every candidate.

Candidates are classified into four recommendation categories: Highly Recommended, Recommended, Consider, and Not Suitable. Finally, all results are presented through an interactive Streamlit dashboard that enables recruiters to search candidates, compare role matches, analyze hiring metrics, and make faster, more consistent recruitment decisions.
