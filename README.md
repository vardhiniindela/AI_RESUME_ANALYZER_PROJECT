# 📄 AI Resume Analyzer & Job Recommendation System

## 🚀 Project Overview
This is an AI-powered Resume Analyzer that extracts skills from resumes, calculates a skill score, and recommends suitable job roles.

## 💡 Features
- 📄 Upload Resume (PDF)
- 🧠 Skill Extraction using NLP logic
- 📊 Skill Score Calculation
- ❗ Missing Skills Suggestions
- 💼 Job Recommendations
- 📊 Visualization of job match (bar chart)
- 🖥️ Interactive UI using Streamlit

## 🛠️ Tech Stack
- Python
- Pandas
- PyPDF2
- Streamlit
- Matplotlib
  
## 💡 Project Idea

This project helps job seekers analyze their resumes and understand their strengths and missing skills. 
It also recommends suitable job roles based on skill matching, making it useful for career guidance.

## 📁 Project Structure
resume_ai_project/
│
├── app.py
├── resume_parser.py
├── skills.py
├── job_recommender.py
├── requirements.txt

## ▶️ How to Run

1. Clone the repository:

2. Navigate to project folder:

3. Install dependencies:
  pip install -r requirements.txt

4. Run the app:
  python -m streamlit run app.py

5. Open in browser:
  http://localhost:8501


## 🎥 Demo

### 🔹 Quick Demo Steps

1. Download the sample resume from below:
👉 [Download Sample Resume](sample_resume.pdf)

2. Run the application:
streamlit run app.py

3. Upload the sample resume

4. View:
- Extracted Skills
- Skill Score
- Job Recommendations
- Graph Visualization

### 💡 Example Output

- Skills: Python, SQL, HTML, CSS  
- Score: 70–90%  
- Recommended Role: Data Analyst / Web Developer
