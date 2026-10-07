from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from workflow.state import AgentState

class EvaluationOutput(BaseModel):
    score: int = Field(description="Match score from 0 to 100")
    missing_skills: list[str] = Field(description="Key skills from the job description missing in the resume")

def evaluator_node(state: AgentState) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    structured_llm = llm.with_structured_output(EvaluationOutput)
    
    prompt = f"""
    You are a Technical Lead. Compare the candidate's skills with the job requirements.
    Candidate skills: {state['parsed_skills']}
    Job description: {state['job_description']}
    
    Provide a score from 0 to 100 and list the critically missing skills.
    """
    
    response = structured_llm.invoke(prompt)
    
    return {
        "score": response.score,
        "missing_skills": response.missing_skills,
        "history": [f"[Tech Lead] Score: {response.score}/100. Missing: {', '.join(response.missing_skills)}"]
    }