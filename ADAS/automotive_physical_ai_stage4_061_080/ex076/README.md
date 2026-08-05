# 예제 076 — 배터리 전압 강하 분석

## 학습 목표
자동차 센서 로그에서 **배터리 전압 강하 분석** 작업을 수행하고, 결과를 ROS2 주행 데이터 분석에 연결합니다.

## 실행 방법

```bat
cd /d C:\work\automotive_physical_ai_stage4_061_080
conda activate auto_physical_ai
python ex076\main.py
```

## 입력과 출력
- 입력: `data/vehicle_sensor_log.csv`
- 출력: 실행 후 `outputs` 폴더에 CSV 생성
- 원본 데이터는 수정하지 않습니다.

## 실무 연결
모터 전류 구간별 배터리 전압을 비교하면 부하 증가에 따른 전압 강하와 전원 계통 이상 징후를 확인할 수 있습니다.

## 라인별 해설

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import pandas as pd` | 실습에 필요한 라이브러리 또는 공통 함수를 불러옵니다. |
| 2 | `from common.data_utils import load_vehicle_data, output_path` | 실습에 필요한 라이브러리 또는 공통 함수를 불러옵니다. |
| 3 | `` | 코드 구간을 구분하는 빈 줄입니다. |
| 4 | `df = load_vehicle_data()` | 공통 자동차 센서 CSV를 DataFrame으로 읽습니다. |
| 5 | `df["voltage_drop_v"] = df["battery_voltage_v"].max() - df["battery_voltage_v"]` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 6 | `summary = df.groupby(pd.cut(df["motor_current_a"], bins=4, duplicates="drop")).agg(` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 7 | `    samples=("battery_voltage_v", "size"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 8 | `    mean_current_a=("motor_current_a", "mean"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 9 | `    mean_voltage_v=("battery_voltage_v", "mean"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 10 | `    mean_drop_v=("voltage_drop_v", "mean"),` | 분석에 필요한 변수·파생 열·조건·집계 결과를 계산합니다. |
| 11 | `)` | 현재 분석 절차를 실행합니다. |
| 12 | `path = output_path("ex076_voltage_drop_summary.csv")` | 결과가 공통 outputs 폴더에 저장되도록 경로를 만듭니다. |
| 13 | `summary.to_csv(path, encoding="utf-8-sig")` | 분석 결과를 파일로 저장합니다. |
| 14 | `print(summary)` | 실행 결과와 핵심 요약값을 콘솔에 출력합니다. |
| 15 | `print(f"saved: {path}")` | 실행 결과와 핵심 요약값을 콘솔에 출력합니다. |

## 확인 문제
1. 전류 구간을 4개로 나누는 방식의 장단점은 무엇인가?
2. 배터리 온도와 충전상태를 추가하면 분석이 어떻게 달라지는가?
3. 전압 강하 경고를 ROS2 진단 토픽으로 발행하려면 어떤 임계값이 필요한가?
