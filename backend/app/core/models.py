from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    loan_applications = relationship(
        "LoanApplication",
        back_populates="customer",
        cascade="all, delete"
    )


class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    loan_amount = Column(Float, nullable=False)
    tenure_months = Column(Integer, nullable=False)
    status = Column(String, default="PENDING")

    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="loan_applications")

    verification = relationship(
        "Verification",
        back_populates="application",
        uselist=False,
        cascade="all, delete"
    )

    credit_evaluation = relationship(
        "CreditEvaluation",
        back_populates="application",
        uselist=False,
        cascade="all, delete"
    )

    sanction_letter = relationship(
        "SanctionLetter",
        back_populates="application",
        uselist=False,
        cascade="all, delete"
    )


class Verification(Base):
    __tablename__ = "verifications"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("loan_applications.id"))

    kyc_status = Column(String, default="PENDING")
    verified_at = Column(DateTime)

    application = relationship("LoanApplication", back_populates="verification")


class CreditEvaluation(Base):
    __tablename__ = "credit_evaluations"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("loan_applications.id"))

    credit_score = Column(Integer)
    eligible = Column(String)
    remarks = Column(String)

    application = relationship("LoanApplication", back_populates="credit_evaluation")


class SanctionLetter(Base):
    __tablename__ = "sanction_letters"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("loan_applications.id"))

    pdf_path = Column(String)
    generated_at = Column(DateTime, default=datetime.utcnow)

    application = relationship("LoanApplication", back_populates="sanction_letter")
