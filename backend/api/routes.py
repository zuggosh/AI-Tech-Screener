from fastapi import APIRouter, HTTPException
from api.schemas import ScreenRequest, ScreenResponse
from workflow.graph import app as agent_app 

router = APIRouter()

@router.post("/screen", response_model=ScreenResponse)
async def screen_candidate(request: ScreenRequest):
    try:
        initial_state = {
            "resume_text": request.resume_text,
            "job_description": request.job_description,
            "parsed_skills": [],
            "score": 0,
            "missing_skills": [],
            "final_response": "",
            "history": ["[API] Request received. Starting screening..."]
        }
        
        final_state = agent_app.invoke(initial_state)
        
        return ScreenResponse(
            score=final_state["score"],
            missing_skills=final_state["missing_skills"],
            final_response=final_state["final_response"],
            history=final_state["history"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))