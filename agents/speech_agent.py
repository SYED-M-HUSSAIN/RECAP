from langchain_core.prompts import PromptTemplate
from core.config import llm
from core.schema import PitchState

prompt_template = PromptTemplate.from_template("""
You are a speech delivery coach.

Transcript:
{transcript}

Evaluate the speaker's delivery with focus on:
1. **Voice Clarity**
2. **Confidence and Tone**
3. **Pacing and Pauses**
4. **Use of Body Language and Eye Contact** (if inferable)

Provide feedback in the following format:
- What was done well?
- What could be improved?
- Practical tips to enhance delivery.

Respond in a clear and constructive tone.
""")

def speech_node(state: PitchState) -> dict:
    prompt = prompt_template.format(
        transcript=state.transcript
    )
    result = llm.invoke(prompt)
    return {"speech_feedback": result.content.strip()}
