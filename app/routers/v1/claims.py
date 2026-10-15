from fastapi import APIRouter

from app.database import SessionDep
from app.models import Claim

router=APIRouter(prefix="/claims")

@router.post("/create")
def claim_create(claim : Claim,session : SessionDep):
    session.add(claim)
    session.commit()
    session.refresh(claim)
    return {"name": claim.claim_id}
