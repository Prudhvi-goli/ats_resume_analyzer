import streamlit as st
import requests

st.title("ATS Resume Analyzer")

uploaded_file = st.file_uploader("Upload your Resume", type=["pdf", "docx"])
job_description = st.text_area("Paste the Job Description")

if uploaded_file and job_description:
    with st.spinner("Analyzing resume..."):
        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            files={"file": uploaded_file},
            data={"job_description": job_description}
        )

    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            st.error(data["error"])
        else:
            st.success("Analysis Complete")
            st.metric("ATS Match Score", data["ATS Match Score"])
            st.write("### ✅ Matched Keywords")
            st.write(data["Matched Keywords"])
            st.write("### ❌ Missing Keywords (Consider adding these)")
            st.write(data["Missing Keywords (Consider adding these)"])
    else:
        st.error("Failed to analyze resume")
