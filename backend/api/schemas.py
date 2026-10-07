from pydantic import BaseModel, Field
from typing import List

class ScreenRequest(BaseModel):
    resume_text: str = Field(..., min_length=10, description="Raw text of the candidate's resume")
    job_description: str = Field(..., min_length=10, description="Job description")

class ScreenResponse(BaseModel):
    score: int = Field(ge=0, le=100, description="Final score from 0 to 100")
    missing_skills: List[str]
    final_response: str
    history: List[str]