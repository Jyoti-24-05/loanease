from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.agents.verification_agent import VerificationAgent

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/verify/{application_id}")
def verify_kyc(application_id: int, db: Session = Depends(get_db)):
    agent = VerificationAgent(db)
    verification = agent.perform_kyc(application_id)

    return {
        "application_id": application_id,
        "kyc_status": verification.kyc_status,
        "verified_at": verification.verified_at
    }
