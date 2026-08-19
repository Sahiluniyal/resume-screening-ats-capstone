import re
import math
import json
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
STOPWORDS = set(stopwords.words('english'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "parsed_resumes.csv")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def clean_text(text: str) -> str:
    if pd.isna(text):
        return ''
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    words = [w for w in text.split() if w not in STOPWORDS and len(w) > 2]
    return ' '.join(words)


def normalize_skills(raw: str) -> list:
    if pd.isna(raw):
        return []
    return [w.strip().lower() for w in str(raw).replace('/', ',').split(',') if w.strip()]


def build_role_descriptions(role_defs: dict) -> dict:
    role_text = {}
    for role, cfg in role_defs.items():
        text = ' '.join(cfg['mandatory_skills'] + cfg['optional_skills'])
        text += ' ' + cfg['experience_requirement'] + ' ' + cfg['domain_preference'] + ' ' + cfg['leadership_requirement']
        role_text[role] = text
    return role_text


def load_and_validate_data(path: str = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    original = df.copy()

    # Standardize missing text values
    text_columns = ['highest_education', 'education_field', 'technical_skills_raw', 'tools_platforms_raw', 'soft_skills_raw', 'experience_summary', 'project_summary', 'key_achievements']
    for col in text_columns:
        df[col] = df[col].fillna('')

    # Normalize obvious data quality issues
    df['highest_education'] = df['highest_education'].replace({'LLM': 'LLM', 'MBA': 'MBA', 'Masters': 'Masters', 'Bachelors': 'Bachelors'}).fillna('Unknown')
    df['education_field'] = df['education_field'].fillna('General')
    df['institution_tier'] = df['institution_tier'].fillna('Tier-3')
    df['resume_length_words'] = df['resume_length_words'].fillna(0).astype(int)
    df['keyword_density_score'] = df['keyword_density_score'].fillna(df['keyword_density_score'].mean())
    df['profile_completeness_score'] = df['profile_completeness_score'].fillna(df['profile_completeness_score'].mean())

    # Duplicates
    duplicate_rows = df.duplicated(subset=['candidate_id'], keep='first').sum()

    validation_report = {
        'rows': int(df.shape[0]),
        'columns': int(df.shape[1]),
        'duplicates_candidate_id': int(duplicate_rows),
        'missing_values': int(df.isna().sum().sum()),
        'missing_by_column': df.isna().sum().sort_values(ascending=False).to_dict(),
    }
    return df, validation_report, original


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['technical_skill_count'] = df['technical_skills_raw'].apply(lambda x: len(normalize_skills(x)))
    df['tool_count'] = df['tools_platforms_raw'].apply(lambda x: len(normalize_skills(x)))
    df['soft_skill_count'] = df['soft_skills_raw'].apply(lambda x: len(normalize_skills(x)))
    df['achievement_count'] = df['key_achievements'].astype(str).str.count(r'\d+%') + df['key_achievements'].astype(str).str.count(r'\d+ years')

    # Feature scores on 0-100 scale
    df['resume_quality_score'] = np.clip((df['resume_length_words'] / 60.0) * 25 + df['profile_completeness_score'] * 35 + df['keyword_density_score'] * 40, 0, 100)
    df['ats_readiness_score'] = np.clip((df['keyword_density_score'] * 50) + (df['profile_completeness_score'] * 50), 0, 100)
    df['technical_strength_score'] = np.clip((df['technical_skill_count'] * 8) + (df['tool_count'] * 4) + (df['cloud_experience_flag'] * 10) + (df['ml_experience_flag'] * 10), 0, 100)
    df['leadership_score'] = np.clip((df['management_experience_flag'] + df['people_management_flag'] + df['delivery_lead_experience_flag'] + df['mentoring_experience_flag']) * 12.5 + (df['stakeholder_management_experience_flag'] * 10), 0, 100)
    df['domain_alignment_score'] = np.clip((df['years_experience'] * 2.5) + (df['technical_strength_score'] * 0.25) + (df['ml_experience_flag'] * 15) + (df['compliance_experience_flag'] * 12), 0, 100)
    df['project_relevance_score'] = np.clip((df['project_management_experience_flag'] * 20) + (df['agile_scrum_experience_flag'] * 10) + (df['achievement_count'] * 12) + (df['resume_length_words'] / 10), 0, 100)
    df['certification_strength_score'] = np.clip((df['highest_education'].isin(['MBA', 'Masters']) * 20) + (df['institution_tier'].isin(['Tier-1']) * 20) + (df['years_experience'] * 0.8), 0, 100)
    df['experience_bucket'] = pd.cut(df['years_experience'], bins=[0, 2, 5, 8, 12, 100], labels=['Entry', 'Mid', 'Senior', 'Lead', 'Architect'], right=False)
    df['skill_density_score'] = np.clip((df['technical_skill_count'] + df['soft_skill_count']) / 2.0 * 10, 0, 100)
    experience_level_score = df['experience_bucket'].map({'Entry': 40, 'Mid': 60, 'Senior': 75, 'Lead': 85, 'Architect': 95}).astype(float)
    df['role_readiness_score'] = np.clip((experience_level_score * 0.6) + (df['technical_strength_score'] * 0.25) + (df['leadership_score'] * 0.15), 0, 100)
    df['career_progression_score'] = np.clip((df['years_experience'] * 4) + (df['delivery_lead_experience_flag'] * 25) + (df['mentoring_experience_flag'] * 15), 0, 100)
    df['education_strength_score'] = np.clip((df['highest_education'].map({'Bachelors': 55, 'Masters': 75, 'MBA': 80, 'LLM': 70}).fillna(50)) + (df['institution_tier'].map({'Tier-1': 20, 'Tier-2': 10, 'Tier-3': 5}).fillna(5)), 0, 100)
    df['professional_maturity_score'] = np.clip((df['years_experience'] * 3) + (df['stakeholder_management_experience_flag'] * 10) + (df['project_management_experience_flag'] * 8) + (df['client_facing_experience_flag'] * 8), 0, 100)
    df['profile_completeness_category'] = pd.cut(df['profile_completeness_score'], bins=[0, 0.4, 0.7, 1.0], labels=['Basic', 'Moderate', 'Strong'], include_lowest=True)
    df['candidate_seniority_category'] = pd.cut(df['years_experience'], bins=[0, 3, 6, 10, 100], labels=['Junior', 'Mid', 'Senior', 'Lead'], include_lowest=True)

    scaler = MinMaxScaler()
    metrics = ['resume_quality_score', 'ats_readiness_score', 'technical_strength_score', 'leadership_score', 'domain_alignment_score', 'project_relevance_score', 'certification_strength_score', 'skill_density_score', 'role_readiness_score', 'career_progression_score', 'education_strength_score', 'professional_maturity_score']
    scaled = scaler.fit_transform(df[metrics])
    df['candidate_quality_index'] = np.sum(scaled, axis=1) / len(metrics) * 100
    return df


def generate_corpus(df: pd.DataFrame) -> list:
    return (df['primary_role'].astype(str) + ' ' + df['experience_summary'].astype(str) + ' ' + df['project_summary'].astype(str) + ' ' + df['key_achievements'].astype(str) + ' ' + df['technical_skills_raw'].astype(str)).apply(clean_text).tolist()


def compute_similarity_scores(df: pd.DataFrame, role_texts: dict) -> pd.DataFrame:
    corpus = generate_corpus(df)
    vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 2), stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)

    role_vectors = vectorizer.transform([clean_text(v) for v in role_texts.values()])
    sims = cosine_similarity(tfidf_matrix, role_vectors)
    role_names = list(role_texts.keys())
    for idx, role in enumerate(role_names):
        df[f'{role.lower().replace(" ", "_")}_similarity'] = sims[:, idx] * 100
    return df


def compute_skill_match(candidate_skills: list, role_skills: list) -> float:
    cand = set(candidate_skills)
    req = set(role_skills)
    if not req:
        return 0.0
    overlap = len(cand.intersection(req))
    return min(100.0, (overlap / max(1, len(req))) * 100.0)


def compute_role_fit(df: pd.DataFrame, role_defs: dict) -> pd.DataFrame:
    for role, cfg in role_defs.items():
        role_key = role.lower().replace(' ', '_')
        sim_col = f'{role_key}_similarity'
        df[role_key + '_fit'] = 0.0
        for i, row in df.iterrows():
            cand_skills = normalize_skills(row['technical_skills_raw']) + normalize_skills(row['tools_platforms_raw']) + normalize_skills(row['soft_skills_raw'])
            skill_fit = compute_skill_match(cand_skills, cfg['mandatory_skills'] + cfg['optional_skills'])
            exp_fit = min(100.0, row['years_experience'] * 8.0)
            project_fit = row[sim_col]
            education_fit = 70 if row['highest_education'] in ['Masters', 'MBA', 'LLM'] else 55
            ats_fit = row['ats_readiness_score']
            leadership_fit = row['leadership_score']
            final = (skill_fit * 0.40) + (exp_fit * 0.20) + (project_fit * 0.15) + (education_fit * 0.10) + (ats_fit * 0.10) + (leadership_fit * 0.05)
            df.at[i, role_key + '_fit'] = final
    return df


def classify_candidates(df: pd.DataFrame) -> pd.DataFrame:
    def bucket(x):
        if x >= 80:
            return 'Highly Recommended'
        if x >= 65:
            return 'Recommended'
        if x >= 50:
            return 'Consider'
        return 'Not Suitable'
    # Use best role fit across roles
    fit_cols = [c for c in df.columns if c.endswith('_fit')]
    df['best_fit_score'] = df[fit_cols].max(axis=1)
    df['best_role'] = df[fit_cols].idxmax(axis=1).str.replace('_fit', '').str.replace('_', ' ').str.title()
    df['recommendation_bucket'] = df['best_fit_score'].apply(bucket)
    return df


def run_pipeline() -> None:
    df, validation_report, original = load_and_validate_data()
    df = engineer_features(df)
    role_defs = __import__('src.role_catalog', fromlist=['ROLE_DEFINITIONS']).ROLE_DEFINITIONS
    role_texts = build_role_descriptions(role_defs)
    df = compute_similarity_scores(df, role_texts)
    df = compute_role_fit(df, role_defs)
    df = classify_candidates(df)

    # Save outputs
    df.to_csv(os.path.join(OUTPUT_DIR, 'ranked_candidates.csv'), index=False)
    pd.DataFrame([validation_report]).to_csv(os.path.join(OUTPUT_DIR, 'validation_report.csv'), index=False)
    with open(os.path.join(OUTPUT_DIR, 'role_definitions.json'), 'w', encoding='utf-8') as f:
        json.dump(role_defs, f, indent=2)
    print('Pipeline completed successfully.')
    print('Validation report:', validation_report)


if __name__ == '__main__':
    run_pipeline()
