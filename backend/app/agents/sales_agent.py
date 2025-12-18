from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
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
        # 1️⃣ Check if customer already exists by phone
        customer = (
            self.db.query(models.Customer)
            .filter(models.Customer.phone == phone)
            .first()
        )

        # 2️⃣ Create customer if not exists
        if not customer:
            customer = models.Customer(
                name=name,
                phone=phone,
                email=email,
                address=address
            )

            try:
                self.db.add(customer)
                self.db.commit()
                self.db.refresh(customer)
            except IntegrityError:
                # Handles rare case: email already exists
                self.db.rollback()
                customer = (
                    self.db.query(models.Customer)
                    .filter(models.Customer.email == email)
                    .first()
                )

        # 3️⃣ Create loan application
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
