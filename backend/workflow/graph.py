from langgraph.graph import StateGraph, START, END
from workflow.state import AgentState

from workflow.nodes.extractor import extractor_node
from workflow.nodes.evaluator import evaluator_node
from workflow.nodes.hr import hr_node
from workflow.nodes.interviewer import interviewer_node

def route_evaluation(state: AgentState) -> str:
    if state["score"] >= 60:
        return "interviewer"
    return "hr"

workflow = StateGraph(AgentState)

workflow.add_node("extractor", extractor_node)
workflow.add_node("evaluator", evaluator_node)
workflow.add_node("hr", hr_node)
workflow.add_node("interviewer", interviewer_node)

workflow.add_edge(START, "extractor")
workflow.add_edge("extractor", "evaluator")

workflow.add_conditional_edges(
    "evaluator",
    route_evaluation,
    {
        "interviewer": "interviewer",
        "hr": "hr"
    }
)

workflow.add_edge("hr", END)
workflow.add_edge("interviewer", END)

app = workflow.compile()