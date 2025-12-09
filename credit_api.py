from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

# FastAPI 앱 및 모델 로드
app = FastAPI()
model = tf.keras.models.load_model("credit_model.h5")

# 입력 데이터 모델 정의
class CreditRequest(BaseModel):
    age: int
    income: float
    loan_amount: float

# 신용 승인 예측 엔드포인트
@app.post("/predict/credit")
def predict_credit(req: CreditRequest):
    # 입력 데이터 배열로 변환
    x = np.array([[req.age, req.income, req.loan_amount]], dtype=np.float32)
    # 예측
    prob = model.predict(x)[0][0]
    result = int(prob > 0.5)
    return {"approved": bool(result), "probability": float(prob)}
