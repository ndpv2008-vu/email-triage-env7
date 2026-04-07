# Email Triage OpenEnv

## Description
Simulates email classification and prioritization.

## Tasks
- Easy: Spam detection
- Medium: Important classification
- Hard: Priority + classification

## Run locally
pip install -r requirements.txt
uvicorn app:app --reload

## Docker
docker build -t email-env .
docker run -p 8000:8000 email-env

## API
POST /reset
POST /step
GET /state