from sqlalchemy.orm import Session
from app.agents.sales_agent import SalesAgent
from app.agents.verification_agent import VerificationAgent
from app.agents.underwriting_agent import UnderwritingAgent
from app.agents.sanction_agent import SanctionAgent


class MasterAgent:
    def __init__(self, db: Session):
        self.sales_agent = SalesAgent(db)
        self.verification_agent = VerificationAgent(db)
        self.underwriting_agent = UnderwritingAgent(db)
        self.sanction_agent = SanctionAgent(db)

    def process_loan(self, payload: dict):
        # Step 1: Sales Agent
        customer, application = self.sales_agent.create_customer_and_application(
            name=payload.get("name"),
            phone=payload.get("phone"),
            email=payload.get("email"),
            address=payload.get("address"),
            loan_amount=payload.get("loan_amount"),
            tenure_months=payload.get("tenure_months")
        )

        # Step 2: Verification Agent
        verification = self.verification_agent.perform_kyc(application.id)

        # Step 3: Underwriting Agent
        evaluation = self.underwriting_agent.evaluate(
            application.id,
            payload.get("loan_amount")
        )

        # Step 4: Sanction Agent (conditional)
        sanction = None
        if evaluation.eligible:   # <-- FIXED (boolean-safe)
            sanction = self.sanction_agent.generate(application.id)

        return {
            "customer_id": customer.id,
            "application_id": application.id,
            "kyc_status": verification.kyc_status,
            "credit_score": evaluation.credit_score,
            "decision": evaluation.remarks,
            "sanction_letter": sanction.pdf_path if sanction else None
        }
