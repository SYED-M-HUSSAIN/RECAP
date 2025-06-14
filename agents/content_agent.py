from langchain_core.prompts import PromptTemplate
from core.config import llm
from core.schema import PitchState

prompt_template = PromptTemplate.from_template("""
You are an expert startup content reviewer.

Transcript:
{transcript}

Evaluate the content based on:
1. **Clarity of Problem and Solution**
2. **Market Opportunity and Uniqueness**
3. **Business Model and Scalability**
4. **Call to Action / Ask**

Provide your evaluation with:
- Key strengths
- Major gaps or unclear points
- Suggestions to refine the content

Keep the tone advisory and constructive.
""")

def content_node(state: PitchState) -> dict:
    prompt = prompt_template.format(
        transcript=state.transcript
    )
    result = llm.invoke(prompt)
    return {"content_feedback": result.content.strip()}
