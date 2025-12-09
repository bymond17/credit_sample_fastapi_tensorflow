from pydantic import BaseModel

class CreditRequest(BaseModel):
    age: int
    income: float
    loan_amount: float

class CreditResponse(BaseModel):
    approved: bool
    probability: float