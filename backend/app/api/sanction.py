from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.agents.sanction_agent import SanctionAgent

router = APIRouter(prefix="/sanction", tags=["Sanction"])

@router.post("/{application_id}")
def sanction(application_id: int, db: Session = Depends(get_db)):
    agent = SanctionAgent(db)
    sanction = agent.generate(application_id)

    if not sanction:
        raise HTTPException(status_code=404, detail="Application not approved")

    return {
        "application_id": application_id,
        "sanction_status": "ISSUED",
        "sanction_letter_id": sanction.id
    }
