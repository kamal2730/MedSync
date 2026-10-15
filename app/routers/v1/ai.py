from fastapi import APIRouter
from app.schemas import AiRequest
from app.service.groq_service import evaluvate_claim_risk

router=APIRouter(prefix="/ai")

@router.post("/AiRiskChecker")
async def ai(request: AiRequest):
    response = await evaluvate_claim_risk(request)
    return response