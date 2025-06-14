from fastapi import FastAPI
from pydantic import BaseModel
from core.schema import PitchState
from agents.speech_agent import speech_node
from agents.content_agent import content_node
from agents.judge_agent import judge_node
from core.combine import combine_feedback

app = FastAPI()

class PitchRequest(BaseModel):
    transcript: str
    niche: str
    audience: str

@app.post("/evaluate")
def evaluate_pitch(payload: PitchRequest):
    state = PitchState(**payload.dict())
    state = state.model_copy(update=speech_node(state))
    state = state.model_copy(update=content_node(state))
    state = state.model_copy(update=judge_node(state))
    result = combine_feedback(state)
    return result
