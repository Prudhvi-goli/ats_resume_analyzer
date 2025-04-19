## 📄 ATS Resume Analyzer

**ATS Resume Analyzer** is an AI-powered web application that helps job seekers optimize their resumes by extracting relevant keywords, matching job descriptions, and suggesting improvements — all while simulating real-world Applicant Tracking Systems (ATS) used by companies.

![Python](https://img.shields.io/badge/python-3.10-blue)
![Streamlit](https://img.shields.io/badge/built%20with-streamlit-orange)
![FastAPI](https://img.shields.io/badge/api-fastapi-green)
![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen)
![OpenAI](https://img.shields.io/badge/powered%20by-openai-ff69b4)

---

### 🚀 Features

- 📄 **Resume Parser**: Supports both `.pdf` and `.docx` formats
- 🧠 **Keyword Extraction**: NLP-based keyword extraction from resume
- 🧾 **Job Match Score**: Calculates similarity between resume and job description
- 💡 **ATS Optimization Tips**: Highlights missing keywords
- 🤖 **AI Suggestions**: Optionally integrates with OpenAI to suggest resume improvements
- 🌐 **Streamlit UI**: Simple, elegant, interactive user interface
- ⚡ **FastAPI Backend**: Handles resume processing and keyword analysis

---

## 🔗 Live Demo
- 🧠 [FastAPI Backend (Render)](https://ats-resume-analyzer-backend.onrender.com/docs)
- 🎨 [Frontend (Streamlit)](https://your-streamlit-app.streamlit.app)

---
### Features:

-Resume parsing from PDF/DOCX
-Job description matching
-Keyword analysis
-Cohere-powered resume improvement suggestions
-Dockerized backend (deployable anywhere)

### Deployment instructions:

```bash
Copy code
docker build -t ats-analyzer .
docker run -d -p 8000:8000 --env-file .env ats-analyzer
```
---
### 🛠️ Tech Stack

| Layer        | Tools Used                           |
|--------------|---------------------------------------|
| Frontend     | Streamlit                            |
| Backend/API  | FastAPI, Uvicorn                     |
| NLP & AI     | SpaCy, NLTK, scikit-learn, OpenAI API|
| Parsing      | pdfminer, python-docx, pdfplumber    |
| Others       | Python, Git, VS Code, dotenv         |
<<<<<<< HEAD

---

### 📁 Project Structure

```
ats_resume_analyzer/
├── backend/
│   └── main.py            # FastAPI backend
│   └── ats_analysis.py    # Keyword extraction + scoring
├── frontend/
│   └── ui.py              # Streamlit UI
├── .env.example           # Environment variable template
├── requirements.txt       # Dependencies
├── README.md              # Project overview
```

---

### ⚙️ Setup & Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/Prudhvi-goli/ats_resume_analyzer.git
cd ats_resume_analyzer
```

#### 2. Create Virtual Environment

```bash
python -m venv myvenv
source myvenv/bin/activate        # Linux/Mac
myvenv\Scripts\activate           # Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Add Your `.env` File

Create a file named `.env` in the root folder:

```env
CONERE_API_KEY=your_conere_api_key_here
```
---

### 🚦 How to Run

#### Start the Backend API (FastAPI)
```bash
uvicorn backend.main:app --reload
```

#### Start the Frontend UI (Streamlit)
```bash
streamlit run frontend/ui.py
```

---

### 🧪 Example Job Description Input
> Paste a JD in the input area like this:

```text
We are hiring a Python backend engineer with experience in FastAPI, NLP, and OpenAI APIs to build scalable AI products. Knowledge of ATS is a bonus.
```

---

### ✅ Output

- Extracted Resume Keywords
- Missing Keywords
- ATS Match Score (e.g., `78%`)
- Optional AI Suggestions for improvements

---

### 📌 Future Improvements

- Support for multiple job descriptions
- UI enhancements with theme customization
- Export ATS analysis as PDF
- Add login/user profiles

---

### 📝 License

This project is licensed under the [MIT License](LICENSE).

---

### 👤 Author

**Goli Prudhvi**  
🔗 [LinkedIn](https://www.linkedin.com/in/prudhvi-goli/)  
💻 [GitHub](https://github.com/Prudhvi-goli)
