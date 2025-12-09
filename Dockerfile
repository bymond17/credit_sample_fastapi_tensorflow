# Dockerfile
FROM python:3.10

WORKDIR /app

COPY credit_model.py credit_api.py ./

# 필수 패키지 설치
RUN pip install --upgrade pip \
    && pip install tensorflow fastapi uvicorn pydantic pandas numpy

# 모델 학습 및 저장
RUN python credit_model.py

# FastAPI 서버 실행
CMD ["uvicorn", "credit_api:app", "--host", "0.0.0.0", "--port", "5000"]