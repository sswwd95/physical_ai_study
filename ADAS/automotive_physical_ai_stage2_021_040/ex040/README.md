# 실습 040 | 미니 통합 진단 리포트

## 핵심 주제
센서 로그를 요약하고 위험 행을 CSV로 저장한다.

## 실행 방법
프로젝트 루트에서 Anaconda Prompt를 열고 다음을 실행합니다.

```bat
conda activate auto_physical_ai
cd /d C:\work\automotive_physical_ai_stage2_021_040
python ex040\main.py
```

## 기대 결과
코드가 오류 없이 실행되고, 계산 결과 또는 생성 파일 경로가 출력되어야 합니다.

## 실무 연결
이 예제는 ROS2 토픽 또는 MuJoCo 센서 배열을 받기 전에 Python 자료구조와 데이터 처리 흐름을 연습하는 단계입니다. 실제 차량 프로젝트에서는 단위, 시간축, 임계값, 결측값을 항상 함께 확인해야 합니다.

## 라인별 해설
- **01행** `from common.load_data import load_vehicle_log` — 필요한 라이브러리 또는 공통 함수를 불러옵니다.
- **02행** `from common.paths import OUTPUT_DIR` — 필요한 라이브러리 또는 공통 함수를 불러옵니다.
- **04행** `df = load_vehicle_log()` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **06행** `df["speed_kph"] = df["speed_mps"] * 3.6` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **07행** `df["risk"] = (df["front_distance_m"] < 3.0) | (df["motor_temp_c"] > 32.2)` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **08행** `risk_rows = df.loc[df["risk"]].copy()` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **10행** `print("=== 자동차 센서 진단 리포트 ===")` — 계산 결과나 상태를 화면에 출력해 확인합니다.
- **11행** `print("전체 샘플:", len(df))` — 계산 결과나 상태를 화면에 출력해 확인합니다.
- **12행** `print("평균 속도(km/h):", round(df["speed_kph"].mean(), 2))` — 계산 결과나 상태를 화면에 출력해 확인합니다.
- **13행** `print("최소 전방 거리(m):", round(df["front_distance_m"].min(), 2))` — 계산 결과나 상태를 화면에 출력해 확인합니다.
- **14행** `print("최대 모터 온도(C):", round(df["motor_temp_c"].max(), 2))` — 계산 결과나 상태를 화면에 출력해 확인합니다.
- **15행** `print("위험 샘플:", len(risk_rows))` — 계산 결과나 상태를 화면에 출력해 확인합니다.
- **17행** `output_path = OUTPUT_DIR / "ex040_risk_rows.csv"` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **18행** `risk_rows.to_csv(output_path, index=False, encoding="utf-8-sig")` — 센서 값, 조건식 또는 계산 결과를 변수에 저장합니다.
- **19행** `print("저장:", output_path)` — 계산 결과나 상태를 화면에 출력해 확인합니다.

## 확인 문제
1. 입력 단위가 바뀌면 어느 부분을 수정해야 합니까?
2. 임계값을 너무 낮게 설정하면 어떤 오경보가 발생할 수 있습니까?
3. 이 결과를 ROS2 메시지로 전달하려면 어떤 필드가 필요합니까?
