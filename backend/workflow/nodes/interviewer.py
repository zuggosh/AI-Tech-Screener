from langchain_openai import ChatOpenAI
from workflow.state import AgentState

def interviewer_node(state: AgentState) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    
    prompt = f"""
    The candidate passed the initial screening (Score: {state['score']}/100).
    Their stack: {', '.join(state['parsed_skills'])}.
    Weaknesses relative to the job description: {', '.join(state['missing_skills']) if state['missing_skills'] else 'none obvious'}.
    
    Write 3 complex technical questions for the upcoming interview to test their real experience, 
    paying special attention to their weaknesses.
    
    Respond strictly in English.
    """
    
    response = llm.invoke(prompt)
    
    return {
        "final_response": response.content,
        "history": ["[Interviewer] Prepared technical questions."]
    }