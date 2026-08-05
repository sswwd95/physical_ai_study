# 예제 059 — 전처리 전후 시각화

## 학습 목표
- 자동차 센서 로그에서 전처리 전후 시각화 절차를 수행합니다.
- ROS2 토픽 또는 MuJoCo 센서 배열에 적용하기 전, 오프라인 CSV로 처리 원리를 확인합니다.

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage3_041_060
conda activate auto_physical_ai
python ex059\main.py
```

## 실무 체크포인트
- 원본 데이터는 보존합니다.
- 임계값은 센서 사양서와 차량 운행 조건에 맞게 조정합니다.
- 결측값을 무조건 채우지 말고 결측 지속 시간과 원인을 함께 기록합니다.
- 정제 결과와 함께 적용 규칙을 메타데이터로 남겨야 재현할 수 있습니다.

## 라인별 해설
| 줄 | 코드 | 설명 |
|---:|---|---|
| 1 | `from pathlib import Path` | 실습에 필요한 모듈이나 경로 도구를 불러옵니다. |
| 2 | `import sys` | 실습에 필요한 모듈이나 경로 도구를 불러옵니다. |
| 3 | `` | 코드 구간을 구분해 가독성을 높입니다. |
| 4 | `# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.` | 프로젝트 루트를 Python 모듈 검색 경로에 추가한다. |
| 5 | `PROJECT_ROOT = Path(__file__).resolve().parents[1]` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 6 | `if str(PROJECT_ROOT) not in sys.path:` | 조건을 만족할 때 경로 또는 처리 상태를 변경합니다. |
| 7 | `    sys.path.insert(0, str(PROJECT_ROOT))` | 해당 전처리 동작을 실행합니다. |
| 8 | `` | 코드 구간을 구분해 가독성을 높입니다. |
| 9 | `import matplotlib.pyplot as plt` | 실습에 필요한 모듈이나 경로 도구를 불러옵니다. |
| 10 | `from common.data_loader import load_sensor_log` | 실습에 필요한 모듈이나 경로 도구를 불러옵니다. |
| 11 | `from common.path_utils import OUTPUT_DIR` | 실습에 필요한 모듈이나 경로 도구를 불러옵니다. |
| 12 | `from common.preprocessing import hampel_filter` | 실습에 필요한 모듈이나 경로 도구를 불러옵니다. |
| 13 | `` | 코드 구간을 구분해 가독성을 높입니다. |
| 14 | `# 속도 데이터를 정렬하고 보간한다.` | 속도 데이터를 정렬하고 보간한다. |
| 15 | `df = load_sensor_log().sort_values("timestamp").drop_duplicates("timestamp").reset_index(drop=True)` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 16 | `df["speed_clean"] = df["vehicle_speed_kmh"].interpolate(limit=5)` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 17 | `df["speed_clean"] = hampel_filter(df["speed_clean"], window=9)` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 18 | `# 원본과 정제 결과를 한 그래프에 표시한다.` | 원본과 정제 결과를 한 그래프에 표시한다. |
| 19 | `plt.figure(figsize=(10, 4))` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 20 | `plt.plot(df["timestamp"], df["vehicle_speed_kmh"], label="raw", alpha=0.6)` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 21 | `plt.plot(df["timestamp"], df["speed_clean"], label="clean")` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 22 | `plt.xlabel("time")` | 해당 전처리 동작을 실행합니다. |
| 23 | `plt.ylabel("speed (km/h)")` | 해당 전처리 동작을 실행합니다. |
| 24 | `plt.legend()` | 해당 전처리 동작을 실행합니다. |
| 25 | `plt.tight_layout()` | 해당 전처리 동작을 실행합니다. |
| 26 | `path = OUTPUT_DIR / "ex059_speed_before_after.png"` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 27 | `plt.savefig(path, dpi=150)` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 28 | `print("saved:", path)` | 중간 결과 또는 검증 결과를 콘솔에 출력합니다. |

## 확인 문제
1. 이 예제의 처리 기준이 실제 차량에서 달라져야 하는 이유는 무엇인가요?
2. 이상값을 삭제하는 대신 대체하거나 플래그만 남겨야 하는 상황은 언제인가요?
3. 이 처리를 ROS2 센서 콜백에 적용할 때 추가로 고려할 항목은 무엇인가요?
