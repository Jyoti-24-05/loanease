import requests
from sqlalchemy.orm import Session
from datetime import datetime
from app.core import models


class VerificationAgent:
    def __init__(self, db: Session):
        self.db = db

    def perform_kyc(self, application_id: int):
        # Mock KYC API
        response = requests.get(
            f"http://127.0.0.1:8000/mock/kyc/{application_id}"
        )

        kyc_result = response.json()

        verification = models.Verification(
            application_id=application_id,
            kyc_status=kyc_result["kyc_status"],
            verified_at=datetime.utcnow()
        )

        self.db.add(verification)
        self.db.commit()
        self.db.refresh(verification)

        return verification
