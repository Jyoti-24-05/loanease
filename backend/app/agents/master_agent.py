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
        customer, application = self.sales_agent.create_customer_and_application(
            name=payload["name"],
            phone=payload["phone"],
            email=payload["email"],
            address=payload["address"],
            loan_amount=payload["loan_amount"],
            tenure_months=payload["tenure_months"]
        )

        verification = self.verification_agent.perform_kyc(application.id)

        evaluation = self.underwriting_agent.evaluate(
            application.id, payload["loan_amount"]
        )

        sanction = None
        if evaluation.eligible == "True":
            sanction = self.sanction_agent.generate(application.id)

        return {
            "customer_id": customer.id,
            "application_id": application.id,
            "kyc_status": verification.kyc_status,
            "credit_score": evaluation.credit_score,
            "decision": evaluation.remarks,
            "sanction_letter": sanction.pdf_path if sanction else None
        }
