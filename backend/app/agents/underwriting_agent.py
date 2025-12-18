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

        # 🔑 FIX: check existing evaluation
        evaluation = (
            self.db.query(models.CreditEvaluation)
            .filter(models.CreditEvaluation.application_id == application_id)
            .first()
        )

        if not evaluation:
            evaluation = models.CreditEvaluation(
                application_id=application_id
            )
            self.db.add(evaluation)

        evaluation.credit_score = score
        evaluation.eligible = eligible
        evaluation.remarks = remarks

        self.db.commit()
        self.db.refresh(evaluation)

        return evaluation
