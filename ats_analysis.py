import re
import nltk
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import pdfplumber
import docx

nltk.data.path.append("C:\\Users\\prudh\\nltk_data")
nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english')).union(ENGLISH_STOP_WORDS)
    return [word for word in tokens if word not in stop_words and len(word) > 2]

def extract_keywords(text):
    words = clean_text(text)
    return Counter(words)

def calculate_match(resume_keywords, job_keywords):
    resume_set = set(resume_keywords.keys())
    job_set = set(job_keywords.keys())
    matched = resume_set.intersection(job_set)
    match_percentage = (len(matched) / len(job_set)) * 100 if job_set else 0
    missing_keywords = sorted(job_set - resume_set)
    return match_percentage, sorted(matched), missing_keywords

def extract_text_from_file(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")

def analyze_resume(resume_text: str, job_description: str) -> dict:
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)
    match_score, matched, missing = calculate_match(resume_keywords, job_keywords)
    return {
        "ATS Match Score": f"{match_score:.2f}%",
        "Matched Keywords": matched,
        "Missing Keywords (Consider adding these)": missing,
    }

if __name__ == "__main__":
    resume_text = input("Paste your resume text: ")
    job_description = input("Paste the job description: ")
    result = analyze_resume(resume_text, job_description)
    print(f"\nATS Match Score: {result['ATS Match Score']}")
    print("\nMatched Keywords:", ', '.join(result['Matched Keywords']))
    print("\nMissing Keywords (Consider adding these):", ', '.join(result['Missing Keywords (Consider adding these)']))
