from langchain_core.prompts import PromptTemplate
from core.config import llm
from core.schema import PitchState

prompt_template = PromptTemplate.from_template("""
You are acting as a critical and constructive judge in the startup domain.

Context:
- Domain/Niche: {niche}
- Audience Role: {audience}
- Transcript:
{transcript}

As a domain expert, provide a detailed evaluation in the following format:

1. **Strengths** (at least 3 bullet points)
2. **Weaknesses or unclear parts** (at least 3 bullet points)
3. **Final Verdict**:
   - Would you invest or support this idea? Why or why not?

Respond in a professional tone.
""")

def judge_node(state: PitchState) -> dict:
    prompt = prompt_template.format(
        niche=state.niche,
        audience=state.audience,
        transcript=state.transcript
    )
    result = llm.invoke(prompt)
    return {"judge_feedback": result.content.strip()}
