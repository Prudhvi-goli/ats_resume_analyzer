import os
import streamlit as st
import requests

API_URL = os.getenv("CO_API_URL", "http://localhost:8000/analyze")  # fallback for local dev

st.set_page_config(page_title="ATS Resume Analyzer", layout="centered")
st.title("📄 ATS Resume Analyzer")

st.markdown("Upload your resume and paste the job description. This app will show your ATS match score, missing keywords, and GPT-powered suggestions to improve your resume.")

# File and input
uploaded_file = st.file_uploader("📎 Upload your Resume", type=["pdf", "docx"])
job_description = st.text_area("📝 Paste the Job Description Here")

if uploaded_file and job_description:
    with st.spinner("🔍 Analyzing your resume..."):
        try:
            response = requests.post(
                API_URL,
                files={"file": uploaded_file},
                data={"job_description": job_description}
            )
            if response.status_code == 200:
                data = response.json()
                if "error" in data:
                    st.error(f"❌ {data['error']}")
                else:
                    st.success("✅ Analysis Complete")

                    st.metric("📊 ATS Match Score", data["ATS Match Score"])

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("### ✅ Matched Keywords")
                        st.code(", ".join(data["Matched Keywords"]), language="text")
                    with col2:
                        st.markdown("### ❌ Missing Keywords")
                        st.code(", ".join(data["Missing Keywords (Consider adding these)"]), language="text")

                    if "Suggestions" in data:
                        st.markdown("### 💡 AI-Powered Resume Suggestions")
                        st.info(data["Suggestions"])
                    else:
                        st.warning("No suggestions provided by the backend.")
            else:
                st.error("🚫 Backend error. Try again later.")
        except Exception as e:
            st.error(f"❌ Request failed: {e}")
