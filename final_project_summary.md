# Final Project Summary

# Resume Screening and Role Matching using NLP

**Company:** TalentBridge Solutions Pvt. Ltd.

**Project Type:** Data Science with GenAI Capstone Project

**Prepared By:** Sahil Uniyal

---

# Project Overview

This capstone project presents an enterprise-style **Resume Screening and Role Matching System** developed for TalentBridge Solutions Pvt. Ltd. The objective of the project is to automate the resume screening process using **Natural Language Processing (NLP)**, business-driven **Feature Engineering**, and a **Hybrid Applicant Tracking System (ATS) Scoring Engine**.

Traditional recruitment systems often rely on manual resume screening or simple keyword matching, making the hiring process slow, inconsistent, and prone to overlooking qualified candidates. This project addresses these challenges by developing an intelligent candidate evaluation system capable of comparing resumes with predefined enterprise job roles and generating recruiter-friendly recommendations.

The solution demonstrates how Data Science and NLP techniques can improve hiring efficiency while providing explainable and consistent candidate rankings.

---

# Business Problem

TalentBridge Solutions processes thousands of resumes for multiple enterprise clients across IT, Data Science, Engineering, Analytics, and Corporate domains.

Recruiters face several operational challenges, including:

- High volume of resumes for every job opening.
- Time-consuming manual screening.
- Inconsistent candidate evaluation across recruiters.
- Traditional ATS systems relying only on keyword matching.
- Difficulty in identifying the most suitable candidates quickly.

The project aims to solve these problems by creating an AI-assisted recruitment solution capable of automatically ranking candidates according to enterprise hiring requirements.

---

# Project Objectives

The major objectives of this project were:

- Automate resume screening.
- Improve candidate-role matching.
- Reduce recruiter workload.
- Generate ATS-compatible Fit Scores.
- Build an explainable candidate ranking system.
- Develop an interactive recruiter dashboard.
- Demonstrate the practical application of NLP in Human Resource Analytics.

---

# Dataset Summary

The project uses the provided **parsed_resumes.csv** dataset containing:

- **5000 candidate profiles**
- **34 structured resume attributes**

The dataset includes:

- Candidate Information
- Technical Skills
- Experience Summary
- Education Details
- Project Information
- Leadership Indicators
- ATS Quality Metrics
- Resume Completeness Scores

The accompanying **Data Definition.xlsx** file was used to understand column definitions, relationships, and business meaning before preprocessing.

---

# Data Validation

The dataset was validated before any analysis or modeling.

Validation included:

- Missing Value Analysis
- Duplicate Candidate Detection
- Data Type Verification
- Resume Completeness Validation
- Keyword Density Validation
- Education Standardization
- Skill Normalization

After preprocessing:

- Total Records: **5000**
- Total Features: **34**
- Duplicate Candidate IDs: **0**
- Missing Values Remaining: **0**

This ensured that the dataset was reliable for downstream analysis.

---

# Feature Engineering

To improve recruiter decision-making, several business-driven engineered features were created.

These include:

- Resume Quality Score
- ATS Readiness Score
- Technical Strength Score
- Leadership Score
- Domain Alignment Score
- Project Relevance Score
- Certification Strength Score
- Skill Density Score
- Role Readiness Score
- Career Progression Score
- Education Strength Score
- Professional Maturity Score
- Candidate Quality Index (CQI)

These engineered features transform raw resume information into meaningful metrics that better represent candidate quality.

---

# NLP-Based Role Matching

Natural Language Processing was used to compare candidate resumes with predefined enterprise job roles.

The NLP pipeline includes:

- Text Cleaning
- Stopword Removal
- Tokenization
- TF-IDF Vectorization
- Cosine Similarity

Five enterprise job roles were manually designed:

- Data Scientist
- Data Analyst
- Machine Learning Engineer
- Business Analyst
- Cloud Data Engineer

Each role contains mandatory skills, optional skills, experience expectations, certifications, and leadership requirements, enabling realistic enterprise-style candidate matching.

---

# Hybrid ATS Scoring Engine

Instead of relying solely on keyword matching, the project combines multiple evaluation criteria to calculate a Final ATS Fit Score.

The scoring process considers:

- Technical Skill Match
- Experience Match
- Project Relevance
- Education Strength
- ATS Readiness
- Leadership Capability

Candidates are then classified into four recruiter-friendly categories:

- Highly Recommended
- Recommended
- Consider
- Not Suitable

This hybrid approach provides balanced, explainable, and business-oriented recommendations.

---

# Dashboard

An interactive Streamlit dashboard was developed to visualize recruitment analytics.

The dashboard includes five modules:

### Executive Dashboard

Provides high-level recruitment KPIs such as:

- Total Candidates
- Highest Fit Score
- Average Fit Score
- Candidate Distribution
- Role Allocation

### Candidate Search

Allows recruiters to search candidates using:

- Candidate Name
- Current Role
- Domain

### Role Matching

Displays the highest-ranked candidates for selected enterprise roles.

### Top Candidates

Shows the best-performing candidates based on Final ATS Scores.

### Analytics

Visualizes engineered metrics such as:

- Resume Quality
- ATS Readiness
- Technical Strength
- Candidate Quality Index
- Experience vs Candidate Quality

---

# Project Outputs

The project generates several deliverables:

- Ranked Candidate List
- Validation Report
- Enterprise Role Definitions
- Recruiter Dashboard
- Business Report
- Technical Documentation
- Presentation Material
- Jupyter Notebook
- ATS Recommendations

These outputs provide recruiters with meaningful insights and improve hiring efficiency.

---

# Business Impact

The proposed solution offers several practical benefits.

### Recruitment Benefits

- Faster Resume Screening
- Reduced Manual Effort
- Consistent Candidate Evaluation
- Improved Shortlisting Process

### Business Benefits

- Reduced Hiring Cost
- Improved Hiring Quality
- Faster Recruitment Cycle
- Better Candidate Experience

### Technical Benefits

- Explainable AI-based Recommendations
- Modular Architecture
- Reusable ATS Framework
- Scalable Design

---

# Project Limitations

Although the project successfully demonstrates an enterprise-style ATS workflow, several limitations remain.

- Only structured CSV resume data is supported.
- Resume PDF parsing is not implemented.
- Historical recruiter feedback was unavailable.
- Transformer-based NLP models such as BERT were outside the project scope.
- Live ATS integration was not included.

---

# Future Enhancements

Future versions of the project may include:

- Resume PDF Parsing
- BERT Embeddings
- Sentence Transformers
- Large Language Models (LLMs)
- Explainable AI
- Recruiter Feedback Learning
- Cloud Deployment
- REST APIs
- Real-Time ATS Integration
- Multi-language Resume Analysis

---

# Conclusion

This capstone project successfully demonstrates how Data Science, Feature Engineering, and Natural Language Processing can modernize enterprise recruitment workflows.

The developed system validates resume data, engineers meaningful business features, compares resumes with enterprise job roles using TF-IDF and Cosine Similarity, calculates Hybrid ATS Fit Scores, and generates recruiter-friendly recommendations through an interactive Streamlit dashboard.

By combining structured data analysis with explainable AI techniques, the project provides a scalable and practical solution for improving hiring efficiency, reducing recruiter workload, and supporting better talent acquisition decisions.

Overall, the project showcases the practical application of Data Science and NLP in Human Resource Analytics while delivering a complete end-to-end enterprise recruitment solution.
