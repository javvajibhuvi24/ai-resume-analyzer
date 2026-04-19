import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from utils.text_extractor import extract_text
from utils.preprocess import clean_text
from utils.matcher import keyword_match
from models.tfidf_model import compute_similarity

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume against a job description using AI")

# Layout: 2 columns
col1, col2 = st.columns(2)

# LEFT SIDE → Resume Upload
with col1:
    st.subheader("Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

# RIGHT SIDE → Job Description
with col2:
    st.subheader("Job Description")
    jd_text = st.text_area("Paste Job Description here", height=300)

# Analyze Button
if st.button("Analyze Resume"):

    if uploaded_file is not None and jd_text.strip() != "":

        # Extract text
        resume_text = extract_text(uploaded_file)

        # Preprocess
        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(jd_text)

        # Keyword match
        score, missing_keywords = keyword_match(resume_clean, jd_clean)

        # TF-IDF similarity
        similarity = compute_similarity(resume_clean, jd_clean)

        st.success("Analysis Complete!")

        # Results Section
        st.subheader("📊 Results")

        col3, col4 = st.columns(2)

        with col3:
            st.metric("Keyword Match Score", f"{score:.2f}%")

        with col4:
            st.metric("Semantic Similarity", f"{similarity:.2f}%")

        # Missing Keywords
        st.subheader("❌ Missing Keywords")
        st.write(list(missing_keywords)[:20])

    else:
        st.error("Please upload resume and paste job description")
