## 📄 ATS Resume Analyzer

**ATS Resume Analyzer** is a full-stack AI-powered application that helps job seekers optimize their resumes by evaluating job match, extracting relevant keywords, and suggesting impactful improvements — simulating how real-world Applicant Tracking Systems (ATS) work.

![Python](https://img.shields.io/badge/python-3.10-blue)
![Streamlit](https://img.shields.io/badge/built%20with-streamlit-orange)
![FastAPI](https://img.shields.io/badge/api-fastapi-green)
![Cohere](https://img.shields.io/badge/powered%20by-cohere-purple)
![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen)

---

### 🚀 Key Features

- 📄 **Smart Resume Parser**: Parses `.pdf` and `.docx` resumes with support for modern formats
- 🧠 **Keyword Extraction Engine**: Uses NLP (SpaCy + NLTK + scikit-learn) for precision keyword targeting
- 📊 **ATS Match Score**: Calculates similarity between resume and job description based on real ATS logic
- 💡 **Keyword Gap Analysis**: Highlights missing skills/phrases recruiters expect
- ✍️ **Cohere-Powered Suggestions**: AI suggests 5–8 bullet-pointed improvements for better impact
- ⚡ **FastAPI Backend**: Lightweight and production-ready REST API
- 🌐 **Streamlit Frontend**: Polished user interface that’s interactive and mobile-friendly
- 🐳 **Dockerized Deployment**: One-command containerization for portability

---

## 🔗 Live Demo

- 🧠 [FastAPI Backend (Render)](https://ats-resume-analyzer-backend.onrender.com)
- 🎨 [Frontend (Streamlit)](https://atsresumeanalyzer-hsg3k9omj4yppd4gll3aef.streamlit.app/)

---

## 🛠️ Tech Stack

| Layer        | Tools Used                               |
|--------------|-------------------------------------------|
| Frontend     | Streamlit                                |
| Backend/API  | FastAPI, Uvicorn                         |
| NLP & AI     | SpaCy, NLTK, scikit-learn, Cohere API    |
| File Parsing | pdfplumber, python-docx                  |
| Deployment   | Docker, Render, Streamlit Cloud          |

---

## 📁 Project Structure

```
ats_resume_analyzer/
├── backend/
│   ├── main.py           # FastAPI backend
│   └── ats_analysis.py   # Keyword extraction + scoring
├── frontend/
│   └── ui.py             # Streamlit UI
├── .env.example          # Environment variable template
├── Dockerfile            # Containerization setup
├── requirements.txt      # Dependencies
├── README.md             # Project overview
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Prudhvi-goli/ats_resume_analyzer.git
cd ats_resume_analyzer
```

### 2. Create Virtual Environment
```bash
python -m venv myvenv
# Linux/macOS:
source myvenv/bin/activate
# Windows:
myvenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your `.env` File
```env
COHERE_API_KEY=your_cohere_api_key_here
```

---

## 🐳 Docker Deployment
```bash
docker build -t ats-analyzer .
docker run -d -p 8000:8000 --env-file .env ats-analyzer
```

---

## 🚦 How to Run Locally

### Start Backend
```bash
uvicorn backend.main:app --reload
```

### Start Frontend
```bash
streamlit run frontend/ui.py
```

---

## 🧪 Sample Job Description Input
```text
We are hiring a Python backend engineer with experience in FastAPI, NLP, and Cohere APIs to build scalable AI products. Knowledge of ATS is a bonus.
```

---

## ✅ Output Sample
- **Matched Keywords**
- **Missing Keywords**
- **ATS Score** (e.g., 82%)
- **Suggested Resume Improvements**

---

## 🌟 Highlights for Recruiters

- Built with **production-ready backend (FastAPI)** and **interactive frontend (Streamlit)**
- Fully **Dockerized** for cloud deployment in CI/CD workflows
- Utilizes **NLP + AI** for real-time resume intelligence
- Demonstrates ability to integrate **third-party APIs (Cohere)**
- Clear separation of concerns (UI/API/NLP modules)
- ⚡ Fast, functional, and ready for **real users**

---

## 📌 Future Roadmap

- [ ] Support for multiple job descriptions
- [ ] Export analysis reports as PDF
- [ ] Enhanced UI themes + dark mode
- [ ] Add user authentication + history tracking

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Goli Prudhvi**  
🔗 [LinkedIn](https://www.linkedin.com/in/prudhvi-goli/)  
💻 [GitHub](https://github.com/Prudhvi-goli)
