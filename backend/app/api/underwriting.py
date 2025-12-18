from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.agents.underwriting_agent import UnderwritingAgent

router = APIRouter(prefix="/underwrite", tags=["Underwriting"])

@router.post("/{application_id}")
def underwrite(application_id: int, db: Session = Depends(get_db)):
    agent = UnderwritingAgent(db)
    result = agent.evaluate(application_id)

    if not result:
        raise HTTPException(status_code=404, detail="Application not found")

    return {
        "application_id": application_id,
        "status": result["status"],
        "approved_amount": result.get("approved_amount")
    }
