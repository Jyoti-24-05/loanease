from fastapi import APIRouter

router = APIRouter()

@router.get("/kyc/{customer_id}")
def mock_kyc_service(customer_id: str):
    """
    Simulates CRM / KYC verification
    """
    return {
        "customer_id": customer_id,
        "kyc_status": "VERIFIED"
    }

@router.get("/credit-score/{customer_id}")
def mock_credit_bureau(customer_id: str):
    """
    Simulates credit bureau response
    """
    return {
        "customer_id": customer_id,
        "credit_score": 750,
        "credit_limit": 500000
    }
