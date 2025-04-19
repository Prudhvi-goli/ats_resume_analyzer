import streamlit as st
import requests
import os

st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("📄 ATS Resume Analyzer")
st.markdown("Upload your resume and paste the job description to analyze your match.")

resume_file = st.file_uploader("📎 Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("📝 Paste the Job Description Here")

if st.button("Analyze") and resume_file and job_description:
    with st.spinner("Analyzing..."):
        try:
            files = {
                "file": (resume_file.name, resume_file, resume_file.type or "application/octet-stream")
            }
            data = {
                "job_description": job_description
            }

            response = requests.post(f"{API_URL}/analyze", files=files, data=data)
            response.raise_for_status()
            result = response.json()

            st.success("✅ Analysis Complete!")

            st.subheader("📌 ATS Match Score")
            st.write(result.get("ATS Match Score", "N/A"))

            st.subheader("📌 Matched Keywords")
            st.write(", ".join(result.get("Matched Keywords", [])))

            st.subheader("❌ Missing Keywords (Consider adding)")
            st.write(", ".join(result.get("Missing Keywords (Consider adding these)", [])))

            st.subheader("💡 Suggestions")
            st.markdown(result.get("Suggestions", "No suggestions available."))

        except Exception as e:
            st.error(f"❌ Request failed: {e}")
