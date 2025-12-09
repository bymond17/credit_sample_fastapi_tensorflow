# Credit Approval Prediction API (FastAPI + TensorFlow)

신용 승인 예측을 위한 머신러닝 API 예제입니다.  
FastAPI, TensorFlow 기반으로 도커 환경에서 완전 자동화 및 실무 구조로 구성되어 있습니다.

---

## 폴더 구조

```
credit_sample_fastapi_tensorflow/
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
├── app/
│   ├── main.py                # FastAPI 엔트리포인트
│   ├── api/
│   │   └── credit.py          # 예측 API 라우터
│   ├── models/
│   │   ├── credit_model.py    # 모델 로드(예측용)
│   │   └── train_credit_model.py # 모델 학습/저장(훈련용)
│   ├── schemas/
│   │   └── credit.py          # Pydantic 데이터 모델
│   └── services/
│       └── credit_service.py  # 예측 비즈니스 로직
├── tests/
│   └── test_credit.py         # 단위 테스트
```

---

## 주요 기능

- 신용 승인 예측 API (`/predict/credit`)
- TensorFlow 기반 모델 학습 및 저장
- FastAPI 실무 구조(모듈 분리, 서비스/스키마/라우터)
- 도커로 완전 자동화(빌드, 실행, 테스트)
- 테스트 코드 포함

---

## 빠른 시작

### 1. 도커로 전체 실행

```powershell
docker-compose up --build
```

- 빌드 및 실행이 완료되면 FastAPI 서버가 5000번 포트에서 동작합니다.

### 2. API 문서 확인

- 브라우저에서 [http://localhost:5000/docs](http://localhost:5000/docs) 접속

### 3. 예측 API 사용 예시

```http
POST /predict/credit
Content-Type: application/json

{
  "age": 30,
  "income": 5000,
  "loan_amount": 1000
}
```

---

## 모델 학습/저장

- `app/models/train_credit_model.py`에서 모델을 학습하고 `models/credit_model.h5`로 저장합니다.
- 도커 빌드 시 자동 실행됩니다.

---

## 테스트

```powershell
pytest tests/
```

- `tests/test_credit.py`에서 예측 함수에 대한 단위 테스트를 수행합니다.

---

## 기타

- 모델 파일(`models/credit_model.h5`)은 `.gitignore`로 관리되어 git에 포함되지 않습니다.
- 폴더 구조 및 코드 역할은 실무 기준에 맞게 분리되어 있습니다.