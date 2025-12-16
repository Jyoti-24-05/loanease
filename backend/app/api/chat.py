from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.agents.master_agent import MasterAgent

router = APIRouter(prefix="/chat", tags=["Chat"])


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def chat(payload: dict, db: Session = Depends(get_db)):
    master_agent = MasterAgent(db)
    result = master_agent.process_loan(payload)
    return {
        "status": "success",
        "data": result
    }
