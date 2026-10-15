from groq import AsyncGroq
from app.settings import setting
from app.schemas import RiskAssesment,AiRequest
import json

client=AsyncGroq(api_key=setting.GROQ_API_KEY)

async def evaluvate_claim_risk(request: AiRequest) -> RiskAssesment:
    prompt = f"""
    You are a medical claims auditing engine. Evaluate the clinical consistency between the ICD-10 code and clinical notes.
    ICD-10 Code: {request.diagnosis_code}
    Clinical Notes: "{request.clinical_notes}"
    
    Return pure JSON with keys: risk_score (0.0 to 100.0), risk_level ("Low", "Medium", "High"), and audit_recommendation.
    """
    chat_completion= await client.chat.completions.create(
        model=setting.GROQ_MODEL,
        messages=[{"role":"user","content":prompt}],
        response_format={"type":"json_object"},
        temperature=0.1
    )
    data=json.loads(chat_completion.choices[0].message.content)

    return RiskAssesment.model_validate(data)