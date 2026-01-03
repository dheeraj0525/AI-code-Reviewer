from pydantic import BaseModel

class CodeRequest(BaseModel):
    code: str
    language: str

class CodeResponse(BaseModel):
    errors: str
    explanation: str
    corrected_code: str