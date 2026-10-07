from typing import TypedDict, Annotated, List
import operator

class AgentState(TypedDict):
    # Input data (does not mutate during the process)
    resume_text: str
    job_description: str
    
    # Data from the Extractor node
    parsed_skills: List[str]
    
    # Data from the Evaluator node (Tech Lead)
    score: int
    
    missing_skills: Annotated[List[str], operator.add]
    
    final_response: str
    
    history: Annotated[List[str], operator.add]