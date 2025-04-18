# Use Python 3.10
FROM python:3.10-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libffi-dev \
    libmagic-dev \
    poppler-utils \
    python3-dev \
    curl \
    && apt-get clean

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
    
RUN python -m spacy download en_core_web_sm && \
    python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
    
COPY . .
    
EXPOSE 8000
    
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
    
