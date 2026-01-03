from fastapi import FastAPI
from backend.schemas import CodeRequest, CodeResponse
from backend.prompts import code_review_prompt
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="AI Code Review Tool")

@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}

@app.post("/analyze", response_model=CodeResponse)
def analyze_code(request: CodeRequest):
    prompt = code_review_prompt(request.code, request.language)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    ai_output = response.choices[0].message.content

    return CodeResponse(
        errors="See explanation",
        explanation=ai_output,
        corrected_code="Included above"
    )