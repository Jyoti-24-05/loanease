from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.mock_services import router as mock_router

app = FastAPI(title="LoanEase API")

# Register API routers
app.include_router(chat_router, prefix="/chat", tags=["Chat"])
app.include_router(mock_router, prefix="/mock", tags=["Mock Services"])

@app.get("/")
def health_check():
    return {"status": "LoanEase backend running"}

