from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# -------- Schemas --------
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

# -------- Routes --------
@router.post("/", response_model=ChatResponse)
def chat(payload: ChatRequest):
    """
    Chat endpoint (Phase 1: stub)
    Phase 3: Will delegate to MasterAgent
    """
    return ChatResponse(
        reply="Hello! LoanEase assistant is active and ready to help."
    )
