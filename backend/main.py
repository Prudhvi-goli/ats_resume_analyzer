from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import spacy
import pdfminer.high_level
import docx2txt
import io
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
import openai
import os
from backend.ats_analysis import analyze_resume
import pdfplumber
import docx
from dotenv import load_dotenv

load_dotenv() 

app = FastAPI(title="ATS Analyzer API", docs_url="/docs", redoc_url="/redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

nlp = spacy.load("en_core_web_sm")

openai.api_key = os.getenv("OPENAI_API_KEY") 

async def extract_text(file: UploadFile) -> str:
    try:
        file_bytes = await file.read()
        file_stream = io.BytesIO(file_bytes)
        if file.filename.endswith(".pdf"):
            return pdfminer.high_level.extract_text(file_stream)
        elif file.filename.endswith(".docx"):
            return docx2txt.process(file_stream)
        else:
            return "Error: Unsupported file format"
    except Exception as e:
        logger.exception("Error processing uploaded file")
        return f"Error processing file: {str(e)}"

def extract_text_from_file(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")

def improve_resume(text: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Improve the resume text for ATS compatibility."},
                {"role": "user", "content": text}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        logger.exception("OpenAI resume improvement failed")
        return f"Error improving resume: {str(e)}"

def match_job_description(resume_text: str, job_description: str) -> float:
    try:
        corpus = [resume_text, job_description]
        vectorizer = TfidfVectorizer().fit_transform(corpus)
        similarity = (vectorizer * vectorizer.T).toarray()
        return float(similarity[0][1])
    except Exception as e:
        logger.exception("TF-IDF similarity failed")
        return 0.0

@app.post("/match")
async def match_resume(file: UploadFile = File(...), job_description: str = ""):
    resume_text = await extract_text(file)
    if resume_text.startswith("Error"):
        return {"error": resume_text}
    score = match_job_description(resume_text, job_description)
    return {"match_score": score}

@app.post("/analyze")
async def analyze_resume_api(file: UploadFile = File(...), job_description: str = Form(...)):
    text = await extract_text(file)
    if text.startswith("Error"):
        return {"error": text}
    try:
        result = analyze_resume(text, job_description)
        return result
    except Exception as e:
        logger.exception("Resume analysis failed")
        return {"error": f"Analysis failed: {str(e)}"}

@app.get("/")
def read_root():
    return {"message": "ATS Analyzer API is running"}