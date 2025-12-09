import tensorflow as tf
import numpy as np
import pandas as pd

# 랜덤 샘플 3000개 생성
np.random.seed(42)
data = []
for _ in range(3000):
    age = np.random.randint(18, 70)
    income = np.random.randint(1000, 20000)
    loan_amount = np.random.randint(100, 10000)
    approved = int(income > loan_amount * 1.5)  # 예시 규칙
    data.append(
        {"age": age, "income": income, "loan_amount": loan_amount, "approved": approved}
    )

df = pd.DataFrame(data)

# 입력값(X), 레이블(y) 추출
X = df[["age", "income", "loan_amount"]].values
y = df["approved"].values

# 심화 모델 구조 (기존과 동일)
model = tf.keras.Sequential(
    [
        tf.keras.layers.InputLayer(input_shape=(3,)),   # 입력층
        tf.keras.layers.Dense(32, activation="relu"),   # 은닉층 1
        tf.keras.layers.BatchNormalization(),           # 배치 정규화
        tf.keras.layers.Dropout(0.3),                   # 드롭아웃
        tf.keras.layers.Dense(16, activation="relu"),   # 은닉층 2
        tf.keras.layers.BatchNormalization(),           # 배치 정규화
        tf.keras.layers.Dropout(0.2),                   # 드롭아웃
        tf.keras.layers.Dense(8, activation="tanh"),    # 은닉층 2
        tf.keras.layers.Dense(1, activation="sigmoid"), # 출력층
    ]
)

# 모델 컴파일
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.005),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

# 모델 학습
model.fit(X, y, epochs=100, batch_size=2, verbose=1)

# 모델 저장
model.save("credit_model.h5")