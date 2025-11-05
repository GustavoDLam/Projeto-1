# backend/routes/submission.py

from fastapi import APIRouter, HTTPException, Header, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Submission
from backend.schemas import SubmissionIn, SubmissionOut

router = APIRouter()

API_KEY = "YOUR_DEV_API_KEY"

@router.post("/submit", response_model=SubmissionOut)
def submit_form(
    submission: SubmissionIn,
    db: Session = Depends(get_db),
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Chave de API inválida")

    new_entry = Submission(**submission.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry

