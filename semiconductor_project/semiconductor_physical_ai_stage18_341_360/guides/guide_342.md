# 실습 342 — severity_rule_engine

## 1. 학습 목표
센서 임계값으로 심각도 등급을 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도·압력·진동·입자·인터록 조건으로 0~5 심각도를 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage18
python examples\ex342_severity_rule_engine.py
```

## 4. 예상 결과
요청한 이상 대응·안전 의사결정 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "safety_decision_stream.csv"` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/safety_decision_stream.csv 파일이 없습니다.")` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `safe_df=pd.read_csv(DATA_FILE)` | 안전 의사결정 센서 스트림을 읽습니다. |
| 14 | `score=np.zeros(len(safe_df),dtype=int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 15 | `score+=(safe_df["temperature_c"]>75).astype(int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 16 | `score+=(safe_df["temperature_c"]>79).astype(int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 17 | `score+=(safe_df["pressure_pa"]>19).astype(int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 18 | `score+=(safe_df["pressure_pa"]>20.5).astype(int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 19 | `score+=(safe_df["vibration_rms_g"]>.12).astype(int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 20 | `score+=(safe_df["particle_count"]>15).astype(int)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 21 | `score+=(safe_df["door_closed"].eq(0)).astype(int)*3` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 22 | `score+=(safe_df["cooling_ok"].eq(0)).astype(int)*2` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 23 | `score+=(safe_df["vacuum_ok"].eq(0)).astype(int)*2` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 24 | `safe_df["calculated_severity"]=np.clip(score,0,5)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 25 | `print(pd.crosstab(safe_df["severity_level"],safe_df["calculated_severity"]))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 자동 정지 조건이 안전 규정과 일치하는가?
2. 경보 미탐과 오탐의 비용을 별도로 평가했는가?
3. 센서 불확실성·통신지연·수동 개입 절차를 반영했는가?