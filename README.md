# Credit Sample FastAPI TensorFlow

이 프로젝트는 FastAPI와 TensorFlow를 활용한 신용 승인 예측 API 예제입니다.  
나이, 소득, 대출금액을 입력받아 승인/미승인을 예측합니다.

## 구성

- Python 3.x
- FastAPI
- TensorFlow, Pandas, Numpy
- Docker/Docker Compose 지원
- REST API (POST 방식)

## 실행 방법

### 1. Docker로 실행

```bash
docker-compose up --build
```

- 기본적으로 5000번 포트에서 FastAPI 서버가 실행됩니다.

### 2. API 테스트

#### PowerShell에서 테스트

```powershell
curl -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"age":30,"income":6000,"loan_amount":1200}' http://localhost:5000/predict
```

#### 크롬 콘솔에서 테스트

```javascript
fetch('http://localhost:5000/predict', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({age:30,income:6000,loan_amount:1200})}).then(res=>res.json()).then(console.log);
```

## API 설명

- **POST /predict**  
  - 요청 예시(JSON):
    ```json
    {
      "age": 30,
      "income": 6000,
      "loan_amount": 1200
    }
    ```
  - 응답 예시(JSON):
    ```json
    {
      "result": 1 // 1: 승인, 0: 미승인
    }
    ```

## 주요 파일

- `credit_model.py` : TensorFlow 모델 생성 및 학습
- `credit_api.py` : FastAPI 기반 API 서버
- `Dockerfile` : Python 및 패키지 환경 설정
- `docker-compose.yml` : 컨테이너 실행 설정

## 참고

- FastAPI 공식 문서: https://fastapi.tiangolo.com/
- TensorFlow 공식 문서: https://www.tensorflow.org/
- Python 공식 문서: https://www.python.org/