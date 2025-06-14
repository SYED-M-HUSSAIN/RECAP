from pydantic import BaseModel
from typing import Optional

class PitchState(BaseModel):
    transcript: str
    niche: str
    audience: str
    speech_feedback: Optional[str] = None
    content_feedback: Optional[str] = None
    judge_feedback: Optional[str] = None
    final_feedback: Optional[str] = None

class FinalFeedback(BaseModel):
    speech: str
    content: str
    judge: str
