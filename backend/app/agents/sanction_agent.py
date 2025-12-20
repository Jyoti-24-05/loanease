from sqlalchemy.orm import Session
from app.core import models
from app.services.pdf_service import generate_sanction_pdf


class SanctionAgent:
    def __init__(self, db: Session):
        self.db = db

    def generate(self, application_id: int):
        application = self.db.query(models.LoanApplication).get(application_id)
        customer = application.customer

        pdf_path = generate_sanction_pdf(
            application_id=application.id,
            customer_name=customer.name,
            amount=application.loan_amount
        )

        sanction = models.SanctionLetter(
            application_id=application.id,
            pdf_path=pdf_path
        )

        self.db.add(sanction)
        self.db.commit()
        self.db.refresh(sanction)

        application.status = "SANCTIONED"
        self.db.commit()

        return sanction
