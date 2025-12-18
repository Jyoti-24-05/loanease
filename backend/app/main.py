from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.mock_services import router as mock_router
from app.api.loan import router as loan_router
from app.api.verification import router as verification_router
from app.api.underwriting import router as underwriting_router
from app.api.sanction import router as sanction_router

app = FastAPI(title="LoanEase API")

app.include_router(chat_router, prefix="/chat", tags=["Chat"])

app.include_router(verification_router, tags=["Verification"])

app.include_router(loan_router, tags=["Loan APIs"])

app.include_router(underwriting_router)

app.include_router(sanction_router)

app.include_router(mock_router, prefix="/mock", tags=["Mock Services"])


@app.get("/")
def health_check():
    return {"status": "LoanEase backend running"}
