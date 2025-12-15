from sqlalchemy.orm import Session
from app.core import models


class SalesAgent:
    def __init__(self, db: Session):
        self.db = db

    def create_customer_and_application(
        self,
        name: str,
        phone: str,
        email: str,
        address: str,
        loan_amount: float,
        tenure_months: int
    ):
        # Check if customer exists
        customer = (
            self.db.query(models.Customer)
            .filter(models.Customer.phone == phone)
            .first()
        )

        if not customer:
            customer = models.Customer(
                name=name,
                phone=phone,
                email=email,
                address=address
            )
            self.db.add(customer)
            self.db.commit()
            self.db.refresh(customer)

        application = models.LoanApplication(
            customer_id=customer.id,
            loan_amount=loan_amount,
            tenure_months=tenure_months,
            status="PENDING"
        )

        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)

        return customer, application
