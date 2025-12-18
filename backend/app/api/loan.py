from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.agents.sales_agent import SalesAgent

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/apply-loan")
def apply_loan(payload: dict, db: Session = Depends(get_db)):
    agent = SalesAgent(db)

    customer, application = agent.create_customer_and_application(
        name=payload["name"],
        phone=payload["phone"],
        email=payload["email"],
        address=payload["address"],
        loan_amount=payload["loan_amount"],
        tenure_months=payload["tenure_months"]
    )

    return {
        "customer_id": customer.id,
        "application_id": application.id,
        "status": "Application created"
    }
