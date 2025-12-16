from sqlalchemy.orm import Session
from app.core import models


class SanctionAgent:
    def __init__(self, db: Session):
        self.db = db

    def generate(self, application_id: int):
        sanction = models.SanctionLetter(
            application_id=application_id,
            pdf_path=f"/sanctions/loan_{application_id}.pdf"
        )

        self.db.add(sanction)
        self.db.commit()
        self.db.refresh(sanction)

        return sanction
