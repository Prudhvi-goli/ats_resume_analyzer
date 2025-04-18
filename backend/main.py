from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import spacy
import logging
from dotenv import load_dotenv
import os
import cohere
from backend.ats_analysis import analyze_resume

load_dotenv()
os.environ["CO_API_KEY"] = os.getenv("COHERE_API_KEY")  # manually set it
co = cohere.Client(os.getenv("COHERE_API_KEY"))

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

def improve_resume(resume_text: str, job_description: str) -> str:
    try:
        prompt = f"""
You are a resume optimization assistant for ATS systems.

Given this RESUME:
---------------------
{resume_text[:3000]}
---------------------

And this JOB DESCRIPTION:
---------------------
{job_description}
---------------------

👉 Rewrite the resume's key achievements in **bullet-point format** that:
- Uses action verbs
- Aligns with the job keywords
- Emphasizes impact and measurable results
- Is optimized for ATS systems

✅ Output 5–8 improved bullet points. Do NOT repeat the same text. Rewrite meaningfully.
"""
        response = co.generate(
            model="command",
            prompt=prompt.strip(),
            max_tokens=350,
            temperature=0.6
        )
        return response.generations[0].text.strip()
    except Exception as e:
        logger.exception("Cohere resume improvement failed")
        return f"Error improving resume: {str(e)}"


@app.post("/analyze")
async def analyze_resume_api(file: UploadFile = File(...), job_description: str = Form(...)):
    try:
        file_bytes = await file.read()
        filename = file.filename

        score, feedback = analyze_resume(file_bytes, job_description, filename)
        resume_text = feedback["resume_text"]

        suggestion_prompt = (
            f"Resume:\n{resume_text[:3000]}\n\n"
            f"Job Description:\n{job_description}\n\n"
            f"Suggest improvements to this resume to increase alignment with the job posting. "
            f"Focus on keyword inclusion, clarity, and ATS-optimized formatting."
        )

        suggestions = improve_resume(resume_text, job_description)

        return {
            "ATS Match Score": f"{score:.2f}%",
            "Matched Keywords": feedback["matched_keywords"],
            "Missing Keywords (Consider adding these)": feedback["missing_keywords"],
            "Suggestions": suggestions
        }

    except Exception as e:
        logger.exception("Resume analysis failed")
        return {"error": f"Analysis failed: {str(e)}"}

@app.get("/")
def read_root():
    return {"message": "ATS Analyzer API is running"}
