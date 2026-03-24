import streamlit as st
from resume_parser import extract_text
from skills import extract_skills
from job_recommender import recommend_jobs


st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>📄 AI Resume Analyzer & Job Recommender</h1>",
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)

    user_skills = extract_skills(text)

    # Handle empty skills
    if not user_skills:
        st.error("No skills found in resume")

    # Score FIRST calculate cheyali
    total_skills = 8
    score = int((len(user_skills) / total_skills) * 100)
    score = min(score, 100)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Extracted Skills")
        for skill in user_skills:
           st.write(f"✔ {skill}")

    with col2:
        st.subheader("📈 Skill Score")
        st.progress(score)
        st.write(f"{score}%")

    # Missing skills
    st.subheader("❗ Missing Skills Suggestions")

    all_skills = [
        "python", "sql", "excel", "pandas",
        "machine learning", "numpy", "html", "css", "javascript"
    ]
    total_skills = len(all_skills)
    score = int((len(user_skills) / total_skills) * 100)
    score = min(score, 100)
    
    missing = [skill for skill in all_skills if skill not in user_skills]

    for skill in missing:
        st.write(f"👉 Learn {skill}")

    # Job recommendation
    st.subheader("💼 Job Recommendations")

    jobs = recommend_jobs(user_skills)

    best_role = max(jobs, key=jobs.get)

    st.success(f"🎯 Best Matching Role: {best_role}  ({jobs[best_role]}% match)")

    for role, match in jobs.items():
        st.write(f"{role}: {match}% match")

    # Chart (IMPORTANT: inside block)
    import matplotlib.pyplot as plt

    st.subheader("📊 Job Match Visualization")

    roles = list(jobs.keys())
    scores = list(jobs.values())

    fig, ax = plt.subplots(figsize=(4,2.5))
    ax.bar(roles, scores)
    ax.set_xlabel("Roles")
    ax.set_ylabel("Match %")
    ax.set_title("Job Match")

    plt.xticks(rotation=20)  

    st.pyplot(fig, use_container_width=False)
    

    # Resume preview
    with st.expander("📄 Resume Text Preview"):
        st.text_area("Resume Content", text[:500], height=25)

# its mee
st.markdown("---")
st.markdown("👨‍💻 Developed by Vardhini | AI Project")

