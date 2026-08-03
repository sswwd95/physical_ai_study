# 실습 237 — simple_survival_table

## 1. 학습 목표
주기별 생존율 표를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
장비 수명으로 10주기 간격 생존율 표를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage12
python examples\ex237_simple_survival_table.py
```

## 4. 예상 결과
요청한 예지보전 분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "predictive_maintenance_rul.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 예지보전 분석 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 예지보전 분석 단계를 수행합니다. |
| 12 | `        "data/predictive_maintenance_rul.csv 파일이 없습니다."` | 예지보전 분석 단계를 수행합니다. |
| 13 | `    )` | 예지보전 분석 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `pm_df=pd.read_csv(DATA_FILE)` | 예지보전용 CSV를 DataFrame으로 읽습니다. |
| 16 | `life=pm_df.groupby("equipment_id")["cycle"].max().add(1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `rows=[]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `for t in range(0,int(life.max())+1,10):` | 여러 장비 또는 설정에 같은 작업을 반복합니다. |
| 19 | `    rows.append({"cycle":t,"survival_probability":float((life>t).mean()),"equipment_at_risk":int((life>t).sum())})` | 예지보전 분석 단계를 수행합니다. |
| 20 | `out=pd.DataFrame(rows)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `print(out)` | 결과를 콘솔에 출력합니다. |
| 22 | `out.to_csv(OUTPUT_DIR/"ex237_survival_table.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. RUL 라벨은 실제 고장 또는 교체 시점과 어떻게 연결되었는가?
2. 장비 단위 데이터 누수를 방지했는가?
3. 정비 임계값은 비용과 안전을 함께 반영하는가?