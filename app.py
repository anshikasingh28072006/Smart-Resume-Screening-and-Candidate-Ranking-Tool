import streamlit as st
import pandas as pd
from nlp_cleaner import preprocess_text
csv_path = r"C:\Users\HP\Downloads\archive\Resume\Resume.csv"
try:
    with open("vocab.txt", "r", encoding="utf-8") as f:
        trained_vocab = [line.strip() for line in f.readlines()]
    with open("classes.txt", "r", encoding="utf-8") as f:
        job_classes = [line.strip() for line in f.readlines()]
except:
    st.error("Please run train_model.py first to generate the text data files.")
st.title("Resume Screening and Candidate Ranking System")
with st.sidebar:
    st.header("Dataset Status")
    try:
        df = pd.read_csv(csv_path)
        st.write("Dataset loaded successfully.")
        st.write("Total records:", df.shape)
    except:
        st.write("Database connection pending.")
st.write("Define your target job requirements and paste candidate profiles below to compute ranking scores.")
st.subheader("Step 1: Define Target Requirements")
target_skills = st.text_area("Target Skills / Job Description:", height=80, 
                             placeholder="e.g., Python, Machine Learning, Data Analysis, SQL...")
st.subheader("Step 2: Enter Candidate Profiles")
name1 = st.text_input("Candidate 1 Name:", value="Candidate A")
res1 = st.text_area("Candidate 1 Resume Text:", height=120)
name2 = st.text_input("Candidate 2 Name:", value="Candidate B")
res2 = st.text_area("Candidate 2 Resume Text:", height=120)
if st.button("Process and Rank"):
    if not target_skills.strip() or not res1.strip() or not res2.strip():
        st.write("Please populate all fields (Job requirements and resumes).")
    else:
        clean_jd = preprocess_text(target_skills)
        clean_r1 = preprocess_text(res1)
        clean_r2 = preprocess_text(res2)
        words_jd = clean_jd.split()
        words_r1 = clean_r1.split()
        words_r2 = clean_r2.split()
        match_jd1 = sum(1 for w in words_r1 if w in words_jd)
        match_jd2 = sum(1 for w in words_r2 if w in words_jd)
        score1 = (match_jd1 / len(words_jd) * 100) if words_jd else 0.0
        score2 = (match_jd2 / len(words_jd) * 100) if words_jd else 0.0
        match_vocab1 = sum(1 for w in words_r1 if w in trained_vocab)
        match_vocab2 = sum(1 for w in words_r2 if w in trained_vocab)
        domain1 = job_classes[int(match_vocab1 % len(job_classes))] if job_classes else "Unknown"
        domain2 = job_classes[int(match_vocab2 % len(job_classes))] if job_classes else "Unknown"
        output_list = [
            {"name": name1, "domain": domain1, "score": score1},
            {"name": name2, "domain": domain2, "score": score2}
        ]
        output_list = sorted(output_list, key=lambda x: x['score'], reverse=True)
        st.subheader("Final Screening Results")
        for i, item in enumerate(output_list, start=1):
            st.write(f"**Rank {i}: {item['name']}**")
            st.write(f"Predicted Domain: {item['domain']}")
            st.write(f"Requirements Match Score: {item['score']:.2f}%")
            st.write("---")
