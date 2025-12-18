from fastapi import APIRouter
import random

router = APIRouter()


@router.get("/kyc/{application_id}")
def mock_kyc(application_id: int):
    return {
        "application_id": application_id,
        "kyc_status": "VERIFIED"
    }


@router.get("/credit-score/{application_id}")
def mock_credit_score(application_id: int):
    return {
        "application_id": application_id,
        "credit_score": random.randint(720, 820),
        "credit_limit": 300000
    } 