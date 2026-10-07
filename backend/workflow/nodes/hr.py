from langchain_openai import ChatOpenAI
from workflow.state import AgentState

def hr_node(state: AgentState) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    
    prompt = f"""
    Write a polite rejection letter to the candidate. 
    Specify that we currently require experience with the following technologies: {', '.join(state['missing_skills'])}.
    The letter should be short and professional.
    
    Respond strictly in English.
    """
    
    response = llm.invoke(prompt)
    
    return {
        "final_response": response.content,
        "history": ["[HR] Generated a rejection letter."]
    }