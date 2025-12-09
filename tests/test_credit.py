from app.services.credit_service import predict_credit
from app.schemas.credit import CreditRequest

def test_predict_credit():
    req = CreditRequest(age=30, income=5000, loan_amount=1000)
    res = predict_credit(req)
    assert isinstance(res.approved, bool)
    assert 0.0 <= res.probability <= 1.0