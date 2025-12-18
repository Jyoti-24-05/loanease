import requests
from datetime import datetime
from sqlalchemy.orm import Session

from app.core import models


class VerificationAgent:
    def __init__(self, db: Session):
        self.db = db

    def perform_kyc(self, application_id: int):
        # 1️⃣ Call mock KYC service safely
        try:
            response = requests.get(
                f"http://127.0.0.1:8000/mock/kyc/{application_id}",
                timeout=5
            )
            response.raise_for_status()
            kyc_result = response.json()
        except Exception:
            # Fallback if mock service fails
            kyc_result = {"kyc_status": "PENDING"}

        # 2️⃣ Check if verification already exists
        verification = (
            self.db.query(models.Verification)
            .filter(models.Verification.application_id == application_id)
            .first()
        )

        if not verification:
            verification = models.Verification(
                application_id=application_id
            )
            self.db.add(verification)

        # 3️⃣ Update verification details
        verification.kyc_status = kyc_result.get("kyc_status", "PENDING")
        verification.verified_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(verification)

        return verification
