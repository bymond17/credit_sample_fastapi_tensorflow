# Dockerfile
FROM python:3.10

WORKDIR /app

COPY app/ ./app/

# 필수 패키지 설치
RUN pip install --upgrade pip \
    && pip install tensorflow fastapi uvicorn pydantic pandas numpy

# 모델 학습 및 저장
RUN python app/models/train_credit_model.py

# FastAPI 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]