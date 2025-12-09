from fastapi import APIRouter
from app.schemas.credit import CreditRequest, CreditResponse
from app.services.credit_service import predict_credit

router = APIRouter()

@router.post("/predict/credit", response_model=CreditResponse)
def predict(req: CreditRequest):
    return predict_credit(req)