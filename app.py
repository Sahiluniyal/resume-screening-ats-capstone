import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='TalentBridge ATS', layout='wide')

DATA = 'outputs/ranked_candidates.csv'

@st.cache_data
def load_data():
    return pd.read_csv(DATA)


df = load_data()

st.title('TalentBridge Solutions - Resume Screening & Role Matching')
st.caption('Hybrid NLP + ATS scoring dashboard for enterprise candidate screening.')

tabs = st.tabs(['Executive Dashboard', 'Candidate Search', 'Role Matching', 'Top Candidates', 'Analytics'])

with tabs[0]:
    c1, c2, c3 = st.columns(3)
    c1.metric('Candidates', f"{len(df):,}")
    c2.metric('Top Fit Score', round(df['best_fit_score'].max(), 2))
    c3.metric('Avg. Fit Score', round(df['best_fit_score'].mean(), 2))
    fig = px.histogram(df, x='best_fit_score', nbins=20, title='Distribution of Final Fit Scores')
    st.plotly_chart(fig, use_container_width=True)
    role_counts = df['best_role'].value_counts().reset_index()
    role_counts.columns = ['Role', 'Candidates']
    st.plotly_chart(px.bar(role_counts, x='Role', y='Candidates', title='Role Allocation'), use_container_width=True)

with tabs[1]:
    query = st.text_input('Search by candidate name, role or domain')
    if query:
        filtered = df[df.apply(lambda r: query.lower() in ' '.join(r.astype(str).fillna('')).lower(), axis=1)]
    else:
        filtered = df
    st.dataframe(filtered[['candidate_id', 'candidate_name', 'primary_role', 'primary_domain', 'years_experience', 'best_role', 'best_fit_score', 'recommendation_bucket']].sort_values('best_fit_score', ascending=False).head(100), use_container_width=True)

with tabs[2]:
    role = st.selectbox('Select target role', sorted(df['best_role'].unique().tolist()))
    role_df = df[df['best_role'] == role].sort_values('best_fit_score', ascending=False).head(20)
    st.dataframe(role_df[['candidate_id', 'candidate_name', 'primary_role', 'years_experience', 'best_fit_score', 'recommendation_bucket']], use_container_width=True)

with tabs[3]:
    top = df.sort_values('best_fit_score', ascending=False).head(20)
    st.dataframe(top[['candidate_id', 'candidate_name', 'primary_role', 'primary_domain', 'years_experience', 'best_role', 'best_fit_score', 'recommendation_bucket']], use_container_width=True)

with tabs[4]:
    st.write('Feature insights from engineered ATS scores')
    cols = ['resume_quality_score', 'ats_readiness_score', 'technical_strength_score', 'leadership_score', 'candidate_quality_index']
    st.bar_chart(df[cols].mean().sort_values(ascending=False))
    st.plotly_chart(px.scatter(df, x='years_experience', y='candidate_quality_index', color='recommendation_bucket', title='Experience vs Candidate Quality Index'), use_container_width=True)

st.sidebar.header('Recruiter Quick Actions')
st.sidebar.info('Use this dashboard for shortlist validation, role fit analysis and recruiter recommendations.')
