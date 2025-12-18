from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: int
    message: str

class ChatResponse(BaseModel):
    reply: str

class LoanApplicationRequest(BaseModel):
    user_id: int
    amount: float
    tenure: int

class LoanApplicationResponse(BaseModel):
    status: str
    message: str
    loan_id: int | None = None
