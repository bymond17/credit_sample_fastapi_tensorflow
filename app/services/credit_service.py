import numpy as np
from app.models.credit_model import model
from app.schemas.credit import CreditRequest, CreditResponse

def predict_credit(req: CreditRequest) -> CreditResponse:
    x = np.array([[req.age, req.income, req.loan_amount]], dtype=np.float32)
    prob = model.predict(x)[0][0]
    result = bool(prob > 0.5)
    return CreditResponse(approved=result, probability=float(prob))