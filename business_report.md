# Business Report

# Resume Screening and Role Matching using NLP

**Company:** TalentBridge Solutions Pvt. Ltd.

**Industry:** Enterprise HR Technology & Talent Analytics

**Prepared By:** Sahil Uniyal

**Project Type:** Data Science with NLP Capstone Project

---

# Executive Summary

TalentBridge Solutions Pvt. Ltd. manages recruitment operations for multiple enterprise clients across IT, consulting, engineering, analytics, and corporate domains. Due to rapid business growth, the recruitment team receives thousands of resumes for every hiring cycle. Manual screening of these resumes is time-consuming, inconsistent, and highly dependent on keyword-based evaluation.

The objective of this project is to develop an AI-assisted Resume Screening and Role Matching system capable of automatically evaluating candidate profiles, matching resumes with enterprise job roles, and generating recruiter-friendly candidate rankings.

The proposed solution combines Data Validation, Feature Engineering, Natural Language Processing (NLP), TF-IDF Vectorization, Cosine Similarity, and Hybrid ATS Scoring to create an explainable recruitment analytics platform.

The final solution is deployed through an interactive Streamlit dashboard that enables recruiters to search candidates, analyze role fit, and make informed hiring decisions.

---

# 1. Business Problem

Modern organizations receive a very large number of resumes for every job opening.

Traditional recruitment faces several challenges:

- Recruiters spend significant time reviewing resumes manually.
- Keyword-based ATS systems fail to understand contextual skills.
- Candidate evaluation varies across recruiters.
- High recruitment workload increases hiring time.
- Suitable candidates may be overlooked because of resume formatting or wording.

These challenges reduce hiring efficiency and increase recruitment costs.

TalentBridge Solutions required a scalable and explainable solution that could automatically identify candidates best suited for enterprise job roles.

---

# 2. Business Objectives

The primary objectives of this project are:

- Automate resume screening.
- Reduce recruiter workload.
- Improve candidate-role matching.
- Generate ATS-compatible fit scores.
- Improve hiring consistency.
- Provide explainable recruiter recommendations.
- Build an interactive analytics dashboard.
- Demonstrate NLP applications in Human Resource Analytics.

---

# 3. Project Scope

The project focuses on structured resume information available in the provided dataset.

The scope includes:

- Resume preprocessing
- Data validation
- Feature engineering
- NLP similarity computation
- Candidate scoring
- Role matching
- Dashboard visualization

The project does not include:

- Resume PDF parsing
- Live recruitment integration
- Online ATS deployment
- Interview scheduling

---

# 4. Dataset Overview

The project uses:

## parsed_resumes.csv

The dataset contains:

- 5000 candidate profiles
- 34 structured attributes

The information includes:

- Candidate Details
- Experience
- Technical Skills
- Tools
- Soft Skills
- Education
- Projects
- Achievements
- ATS Metrics
- Resume Quality Indicators
- Leadership Flags
- Domain Information

Data Definition.xlsx was used to understand every attribute before preprocessing.

---

# 5. Data Validation

Data quality is one of the most important phases of any Data Science project.

The following validation checks were performed:

## Missing Value Analysis

Checked every attribute for missing values.

Result:

No significant missing values remained after preprocessing.

---

## Duplicate Detection

Candidate IDs were examined for duplicates.

Result:

No duplicate candidate records were found.

---

## Text Standardization

Standardized:

- Education names
- Institution tiers
- Skill formatting
- Empty text fields

---

## Resume Quality Validation

Validated:

- Resume Length
- Keyword Density
- Profile Completeness

These metrics help estimate ATS compatibility.

---

## Validation Summary

| Validation | Result |
|------------|---------|
| Missing Values | Corrected |
| Duplicate Candidates | None |
| Resume Completeness | Standardized |
| Keyword Density | Validated |
| Education Data | Standardized |

---

# 6. Exploratory Data Analysis

EDA was performed to understand candidate characteristics.

The analysis included:

- Experience Distribution
- Role Distribution
- Domain Distribution
- Technical Skill Frequency
- Education Distribution
- Resume Quality
- ATS Readiness
- Leadership Experience
- Candidate Quality Index

The analysis provided valuable insights into candidate diversity and hiring trends.

---

# 7. Feature Engineering

Feature Engineering was the core component of this project.

Raw resume data cannot directly represent candidate quality.

Therefore, multiple business-driven features were created.

## Resume Quality Score

Measures:

- Resume Length
- Profile Completeness
- Keyword Density

---

## ATS Readiness Score

Represents how compatible a resume is with Applicant Tracking Systems.

---

## Technical Strength Score

Calculated using:

- Technical Skills
- Tools
- Cloud Experience
- Machine Learning Experience

---

## Leadership Score

Evaluates:

- Management Experience
- Stakeholder Management
- Mentoring
- Delivery Leadership

---

## Domain Alignment Score

Measures candidate suitability based on domain experience.

---

## Project Relevance Score

Evaluates:

- Project Management
- Agile Experience
- Resume Achievements

---

## Candidate Quality Index

A composite metric generated by combining multiple engineered features.

This score provides an overall assessment of candidate quality.

---

# 8. Enterprise Role Definitions

Since no Job Description dataset was provided, realistic enterprise roles were designed manually.

The following roles were created:

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
- Domain Preference
- Leadership Expectations

This enables realistic enterprise-style role matching.

---

# 9. NLP Methodology

Natural Language Processing was applied to understand resume content.

The NLP pipeline includes:

1. Text Cleaning
2. Lowercase Conversion
3. Stopword Removal
4. Tokenization
5. TF-IDF Vectorization
6. Cosine Similarity

TF-IDF converts textual resume information into numerical vectors.

Cosine Similarity measures semantic similarity between candidate resumes and enterprise role descriptions.

Higher similarity indicates better role alignment.

---

# 10. Hybrid ATS Scoring Model

Rather than relying solely on keyword matching, a Hybrid ATS model was designed.

The scoring engine combines multiple evaluation criteria.

| Component | Weight |
|------------|---------|
| Skill Match | 40% |
| Experience Match | 20% |
| Project Relevance | 15% |
| Education Match | 10% |
| ATS Readiness | 10% |
| Leadership Score | 5% |

The final output is a Fit Score ranging from 0 to 100.

---

# 11. Candidate Classification

Candidates are classified into four recruiter-friendly categories.

| Score | Recommendation |
|---------|----------------|
| 80+ | Highly Recommended |
| 65–79 | Recommended |
| 50–64 | Consider |
| Below 50 | Not Suitable |

This classification improves recruiter decision making.

---

# 12. Dashboard

The project includes an interactive Streamlit dashboard.

Dashboard modules include:

- Executive Dashboard
- Candidate Search
- Role Matching
- Top Candidates
- Analytics

Recruiters can:

- Search candidates
- Analyze role fit
- Compare ATS scores
- Explore hiring trends

---

# 13. Business Impact

The proposed solution offers several benefits.

### Operational Benefits

- Faster screening
- Reduced manual effort
- Consistent evaluation
- Improved recruiter productivity

### Business Benefits

- Better hiring quality
- Reduced hiring cost
- Faster recruitment cycle
- Improved candidate experience

### Technical Benefits

- Explainable AI
- Reusable ATS framework
- Modular architecture
- Scalable design

---

# 14. Limitations

The project has certain limitations.

- No real Job Description dataset was available.
- Resume parsing from PDF/DOC files was not included.
- Historical recruiter feedback was unavailable.
- Advanced transformer models such as BERT were not implemented.
- Live ATS deployment was outside the project scope.

---

# 15. Future Enhancements

The project can be extended using:

- Resume PDF Parsing
- Sentence Transformers
- BERT Embeddings
- Large Language Models (LLMs)
- Generative AI for Resume Understanding
- Cloud Deployment
- Recruiter Feedback Learning
- Explainable AI (XAI)
- Real-time ATS Integration

---

# 16. Conclusion

This project demonstrates how Data Science and Natural Language Processing can modernize enterprise recruitment.

The developed Hybrid ATS System combines structured resume analysis, feature engineering, NLP similarity, and business-driven scoring to provide recruiter-friendly candidate recommendations.

Compared with traditional keyword-based screening, the proposed solution provides more explainable, consistent, and scalable hiring decisions.

The project successfully addresses TalentBridge Solutions' recruitment challenges while showcasing the practical application of NLP and Machine Learning in Human Resource Analytics.