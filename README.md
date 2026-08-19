# TalentBridge Solutions – Resume Screening & Role Matching using NLP

> **Enterprise-Style AI-Powered Applicant Tracking System (ATS) Prototype for Automated Resume Screening and Candidate Ranking**

---

# Project Overview

The recruitment process in modern organizations involves screening thousands of resumes for multiple job openings. Manual resume screening is time-consuming, inconsistent, and often depends heavily on keyword matching, which can overlook highly qualified candidates.

This project presents an **Enterprise Resume Screening and Role Matching System** developed for **TalentBridge Solutions Pvt. Ltd.** The solution demonstrates how **Natural Language Processing (NLP)** and **business-driven ATS scoring** can automate candidate evaluation and improve hiring efficiency.

The project combines:

- Data Validation
- Feature Engineering
- TF-IDF based NLP Similarity
- Hybrid ATS Scoring
- Candidate Ranking
- Streamlit Dashboard

to create an end-to-end recruitment analytics solution.

---

# Business Problem

TalentBridge Solutions receives thousands of resumes from applicants applying to different technology and business roles.

Recruiters face several operational challenges:

- Manual resume screening requires significant time.
- Keyword-based ATS systems fail to understand contextual skills.
- Different recruiters may shortlist candidates differently.
- High recruitment workload delays hiring.
- Candidate-job alignment is difficult to evaluate objectively.

The organization required an intelligent system capable of automatically evaluating candidate resumes, matching them with enterprise job roles, and producing explainable recruiter recommendations.

---

# Project Objectives

The primary objectives of this project are:

- Automate resume screening.
- Reduce recruiter workload.
- Improve candidate-role matching.
- Generate ATS-style fit scores.
- Rank candidates based on multiple business factors.
- Build an interactive recruiter dashboard.
- Demonstrate the use of NLP in recruitment analytics.

---

# Dataset Overview

The project uses the provided **parsed_resumes.csv** dataset consisting of:

- **5000 Candidate Profiles**
- **34 Structured Resume Attributes**

The dataset contains information such as:

- Candidate ID
- Resume Metadata
- Technical Skills
- Tools & Platforms
- Soft Skills
- Experience Summary
- Project Summary
- Education Details
- Domain
- Role
- Leadership Indicators
- ATS Quality Indicators
- Resume Completeness Score
- Keyword Density Score

A separate **Data Definition.xlsx** file was used to understand every column before performing preprocessing and analysis.

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-learn | TF-IDF & Cosine Similarity |
| NLTK | Text Cleaning |
| Streamlit | Dashboard |
| Plotly | Interactive Charts |
| Matplotlib | Visualizations |
| JSON | Role Definitions |

---

# Project Workflow

```
Resume Dataset
       │
       ▼
Data Validation
       │
       ▼
Data Cleaning
       │
       ▼
Feature Engineering
       │
       ▼
Enterprise Job Role Creation
       │
       ▼
NLP Processing
       │
       ▼
TF-IDF Vectorization
       │
       ▼
Cosine Similarity
       │
       ▼
Hybrid ATS Scoring
       │
       ▼
Candidate Ranking
       │
       ▼
Recruiter Dashboard
```

---

# Data Validation

Before building the NLP model, the dataset underwent comprehensive validation.

The following quality checks were performed:

- Missing Value Analysis
- Duplicate Candidate Detection
- Resume Completeness Validation
- Experience Consistency Checks
- Education Standardization
- Skill Normalization
- Keyword Density Validation
- Profile Completeness Validation

After preprocessing:

- Total Candidates: **5000**
- Duplicate Candidate IDs: **0**
- Missing Values: **0**

This ensured that the dataset was reliable before feature engineering and modeling.

---

# Feature Engineering

One of the major strengths of this project is the creation of business-driven engineered features.

The following features were created:

- Resume Quality Score
- ATS Readiness Score
- Technical Strength Score
- Leadership Score
- Domain Alignment Score
- Project Relevance Score
- Certification Strength Score
- Experience Bucket
- Skill Density Score
- Role Readiness Score
- Career Progression Score
- Education Strength Score
- Professional Maturity Score
- Candidate Quality Index

These engineered features transform raw resume information into meaningful business indicators that improve candidate evaluation.

---

# Enterprise Job Roles

Since the dataset did not include Job Descriptions, five realistic enterprise roles were designed manually:

- Data Scientist
- Data Analyst
- Machine Learning Engineer
- Business Analyst
- Cloud Data Engineer

Each role contains:

- Mandatory Skills
- Optional Skills
- Experience Requirements
- Certifications
- Domain Preferences
- Leadership Expectations

This enables realistic resume-to-role matching similar to enterprise ATS platforms.

---

# NLP Pipeline

The project applies Natural Language Processing (NLP) to compare resumes with enterprise job descriptions.

The pipeline includes:

1. Text Cleaning
2. Lowercase Conversion
3. Stopword Removal
4. Tokenization
5. TF-IDF Vectorization
6. Cosine Similarity

TF-IDF converts resume text into numerical vectors.

Cosine Similarity measures the similarity between candidate resumes and enterprise role descriptions.

Higher similarity scores indicate better candidate-role alignment.

---

# Hybrid ATS Scoring Engine

Unlike traditional keyword-based ATS systems, this project combines multiple business factors.

The final candidate score is calculated using:

- Skill Match
- Experience Match
- Project Relevance
- Education Match
- ATS Readiness
- Leadership Score

This hybrid approach provides a more balanced and explainable candidate evaluation process.

---

# Candidate Classification

Candidates are classified into four categories:

- Highly Recommended
- Recommended
- Consider
- Not Suitable

The classification is based on the final ATS Fit Score.

---

# Dashboard Features

The Streamlit dashboard contains five interactive sections.

### Executive Dashboard

Displays:

- Total Candidates
- Highest Fit Score
- Average Fit Score
- Distribution of ATS Scores
- Role Allocation

---

### Candidate Search

Allows recruiters to search candidates using:

- Candidate Name
- Primary Role
- Domain

---

### Role Matching

Allows recruiters to:

- Select a target role
- View the highest-ranked candidates
- Compare ATS scores

---

### Top Candidates

Displays the highest-ranked candidates across all roles.

---

### Analytics

Provides:

- Feature Importance
- Engineered ATS Metrics
- Candidate Quality Distribution
- Experience vs Candidate Quality Index

---

# Project Outputs

The project generates:

- Ranked Candidate List
- Validation Report
- Role Definitions
- Recruiter Dashboard
- Business Report
- Documentation
- Presentation Material

---

# Future Improvements

The current project can be extended by integrating:

- Resume PDF Parsing
- BERT Embeddings
- Sentence Transformers
- Large Language Models (LLMs)
- Real Enterprise Job Descriptions
- Recruiter Feedback Learning
- Explainable AI (XAI)
- Cloud Deployment

---

# Conclusion

This project demonstrates how NLP and business-driven feature engineering can significantly improve the resume screening process.

Instead of relying only on keyword matching, the system combines technical skills, experience, education, leadership indicators, ATS quality metrics, and semantic text similarity to produce explainable candidate rankings.

The solution provides recruiters with a scalable, transparent, and enterprise-style ATS prototype capable of improving hiring efficiency and decision-making.

---

# Author

**Sahil Uniyal**

B.Tech Computer Science & Engineering

Data Science & Machine Learning Enthusiast

Capstone Project – Career247 Data Science and machine learning with GenAI