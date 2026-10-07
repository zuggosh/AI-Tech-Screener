from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from workflow.state import AgentState

class SkillsOutput(BaseModel):
    skills: list[str] = Field(description="Array of the candidate's technical skills")

def extractor_node(state: AgentState) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    structured_llm = llm.with_structured_output(SkillsOutput)
    
    prompt = f"""
    Analyze the resume text and extract all technical skills, programming languages, and frameworks.
    Resume: {state['resume_text']}
    """
    
    response = structured_llm.invoke(prompt)
    
    return {
        "parsed_skills": response.skills,
        "history": [f"[Data Extractor] Extracted {len(response.skills)} skills."]
    }