import requests
from sqlalchemy.orm import Session
from app.core import models


class UnderwritingAgent:
    def __init__(self, db: Session):
        self.db = db

    def evaluate(self, application_id: int, loan_amount: float):
        response = requests.get(
            f"http://127.0.0.1:8000/mock/credit-score/{application_id}"
        )

        credit_data = response.json()
        score = credit_data["credit_score"]
        limit = credit_data["credit_limit"]

        if score < 700:
            eligible = False
            remarks = "Low credit score"
        elif loan_amount <= limit:
            eligible = True
            remarks = "Instant approval"
        elif loan_amount <= 2 * limit:
            eligible = True
            remarks = "Salary slip required"
        else:
            eligible = False
            remarks = "Loan amount exceeds eligibility"

        evaluation = models.CreditEvaluation(
            application_id=application_id,
            credit_score=score,
            eligible=str(eligible),
            remarks=remarks
        )

        self.db.add(evaluation)
        self.db.commit()
        self.db.refresh(evaluation)

        return evaluation
