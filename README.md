## 🧠 ATS Resume Analyzer

A full-stack AI-powered platform that analyzes resumes against job descriptions, providing ATS match scores, missing keywords, and improvement suggestions using GPT-4.

### 🚀 Features

- **Resume-to-Job Match Scoring**: Uses TF-IDF and OpenAI embeddings to calculate how well a resume aligns with a given job description.
- **Keyword Gap Analysis**: Highlights matched vs missing keywords with visual feedback.
- **Resume Enhancer**: GPT-4 suggests improvements to make resumes more tailored and ATS-friendly.
- **Multi-format Support**: Accepts `.pdf` and `.docx` resumes; parses using spaCy, regex, and text extraction pipelines.
- **FastAPI Backend + Streamlit UI**: Built for clean API integration and easy deployment.

### 🛠️ Tech Stack

- **Backend**: Python, FastAPI, spaCy, OpenAI API (text-embedding-ada-002)
- **Frontend**: Streamlit (for interactive UI)
- **NLP**: TF-IDF, keyword extraction, NER, tokenization
- **File Handling**: PyMuPDF, python-docx
- **Dev Tools**: Git, CORS, virtualenv

### 📊 Sample Output

```
Resume Match Score: 82%
Top Missing Keywords: ['Kubernetes', 'NLP', 'CI/CD']
Suggestions: Add more detail on your project involving Docker and ML pipelines.
```

### 💡 Why I Built This

I wanted to bridge the gap between generic resumes and tailored applications by helping users understand how their resume stacks up—just like an ATS system would. I built this from scratch using only open-source tools and the OpenAI API.
