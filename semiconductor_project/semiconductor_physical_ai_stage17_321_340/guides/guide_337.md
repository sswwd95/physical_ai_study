# 실습 337 — bayesian_confidence_score

## 1. 학습 목표
HDI 폭을 이용한 베이지안 신뢰도 점수를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
HDI 폭을 사용해 0~1 베이지안 신뢰도 점수를 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage17
python examples\ex337_bayesian_confidence_score.py
```

## 4. 예상 결과
요청한 베이지안 센서 융합·디지털 트윈 불확실성 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import arviz as az` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_sensor_fusion.csv"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 11 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 12 | `sensor_df = pd.read_csv(DATA_FILE)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `fusion=pd.read_csv(OUTPUT_DIR/"ex336_credible_interval_fusion.csv") if (OUTPUT_DIR/"ex336_credible_interval_fusion.csv").exists() else None` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 15 | `if fusion is None:` | 베이지안 센서 융합 또는 트윈 불확실성 분석을 수행합니다. |
| 16 | `    raise FileNotFoundError("먼저 실습 336을 실행하세요.")` | 베이지안 센서 융합 또는 트윈 불확실성 분석을 수행합니다. |
| 17 | `fusion["hdi_width"]=fusion["hdi_high"]-fusion["hdi_low"]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 18 | `scale=fusion["hdi_width"].median()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 19 | `fusion["bayesian_confidence"]=np.exp(-fusion["hdi_width"]/(scale+1e-9))` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 20 | `print(fusion.head(10).round(4))` | 결과를 콘솔에 출력합니다. |
| 21 | `fusion.to_csv(OUTPUT_DIR/"ex337_bayesian_confidence.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 센서 바이어스와 실제 공정 변화를 구분했는가?
2. 사후예측구간이 너무 좁거나 넓지 않은가?
3. 이상확률을 자동 제어에 사용할 때 안전 임계값이 있는가?