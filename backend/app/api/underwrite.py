from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.agents.underwriting_agent import UnderwritingAgent

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/underwrite/{application_id}")
def underwrite(application_id: int, db: Session = Depends(get_db)):
    agent = UnderwritingAgent(db)
    evaluation = agent.evaluate(application_id)

    return {
        "application_id": application_id,
        "credit_score": evaluation.credit_score,
        "eligible": evaluation.eligible,
        "remarks": evaluation.remarks
    }
