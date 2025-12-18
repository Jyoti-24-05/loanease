from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.database import SessionLocal
from app.agents.master_agent import MasterAgent

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def chat(payload: dict, db: Session = Depends(get_db)):
    try:
        master_agent = MasterAgent(db)
        result = master_agent.process_loan(payload)

        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        # Temporary safety for Phase 1
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
