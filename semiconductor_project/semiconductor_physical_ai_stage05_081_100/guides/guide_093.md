# 실습 093 — robust_covariance

## 1. 학습 목표
Robust Covariance로 다변량 타원형 정상 영역을 추정합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
MinCovDet를 사용해 6개 센서의 robust Mahalanobis distance를 계산하라.
거리 제곱의 97.5% 분위수를 임계값으로 사용하고 이상 여부를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex093_robust_covariance.py
```

## 4. 예상 결과
극단값 영향을 줄인 공분산 기반 다변량 이상이 탐지됩니다.

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
| 13 | `from sklearn.covariance import MinCovDet` | 필요한 라이브러리나 기능을 불러옵니다. |
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
| 26 | `x_scaled = StandardScaler().fit_transform(sensor_df[features])` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `model = MinCovDet(random_state=42).fit(x_scaled)` | 정상 패턴 또는 전체 데이터 구조를 모델이 학습합니다. |
| 29 | `distance_squared = model.mahalanobis(x_scaled)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `threshold = np.quantile(distance_squared, 0.975)` | 분포의 분위수를 이용해 임계값을 계산합니다. |
| 31 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 32 | `sensor_df["robust_mahalanobis_d2"] = distance_squared` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `sensor_df["robust_covariance_anomaly"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    distance_squared > threshold` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 35 | `).astype(int)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 36 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 37 | `print("임계값:", round(threshold, 4))` | 실행 결과를 콘솔에 출력합니다. |
| 38 | `print(` | 실행 결과를 콘솔에 출력합니다. |
| 39 | `    "Robust Covariance 이상 수:",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 40 | `    int(sensor_df["robust_covariance_anomaly"].sum()),` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 41 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?