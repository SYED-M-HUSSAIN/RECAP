from pydantic import BaseModel
from core.schema import PitchState

class StructuredFeedback(BaseModel):
    speech_feedback: str
    content_feedback: str
    judge_feedback: str

    def render_summary(self) -> str:
        return f"""
📢 **Speech Feedback:**
{self.speech_feedback}

📝 **Content Feedback:**
{self.content_feedback}

👩‍⚖️ **Judge Feedback:**
{self.judge_feedback}
""".strip()

def combine_feedback(state: PitchState) -> dict:
    structured = StructuredFeedback(
        speech_feedback=state.speech_feedback,
        content_feedback=state.content_feedback,
        judge_feedback=state.judge_feedback
    )
    return {"final_feedback": structured.render_summary()}