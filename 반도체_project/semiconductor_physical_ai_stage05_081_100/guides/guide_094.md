# 실습 094 — pca_reconstruction_error

## 1. 학습 목표
PCA 재구성 오차로 정상 저차원 구조에서 벗어난 시점을 찾습니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
StandardScaler 후 PCA(n_components=3)를 적용하라.
역변환 결과와 원본 표준화 데이터의 평균제곱오차를 행별 reconstruction_error로 계산하고
97.5% 분위수 이상을 이상으로 표시하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex094_pca_reconstruction_error.py
```

## 4. 예상 결과
정상 저차원 패턴으로 잘 복원되지 않는 시점이 이상으로 탐지됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `from sklearn.decomposition import PCA` | 필요한 라이브러리나 기능을 불러옵니다. |
| 14 | `from sklearn.preprocessing import StandardScaler` | 필요한 라이브러리나 기능을 불러옵니다. |
| 15 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 16 | `sensor_df = pd.read_csv(DATA_FILE)` | 센서 CSV를 DataFrame으로 읽습니다. |
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `features = [` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    "chamber_temp_c",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 20 | `    "chamber_pressure_pa",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 21 | `    "rf_power_w",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 22 | `    "gas_flow_sccm",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 23 | `    "vibration_g",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 24 | `    "particle_count",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 25 | `]` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `x_scaled = StandardScaler().fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 29 | `pca = PCA(n_components=3, random_state=42)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `score = pca.fit_transform(x_scaled)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `reconstructed = pca.inverse_transform(score)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 33 | `error = np.mean(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    (x_scaled - reconstructed) ** 2,` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 35 | `    axis=1,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 37 | `threshold = np.quantile(error, 0.975)` | 분포의 분위수를 이용해 임계값을 계산합니다. |
| 38 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 39 | `sensor_df["pca_reconstruction_error"] = error` | 계산 결과나 설정값을 변수에 저장합니다. |
| 40 | `sensor_df["pca_reconstruction_anomaly"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `    error > threshold` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 42 | `).astype(int)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 43 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 44 | `print("PCA 재구성 이상 수:", int(` | 실행 결과를 콘솔에 출력합니다. |
| 45 | `    sensor_df["pca_reconstruction_anomaly"].sum()` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 46 | `))` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?