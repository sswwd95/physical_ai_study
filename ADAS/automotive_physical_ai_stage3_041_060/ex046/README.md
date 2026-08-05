# 예제 046 — 선형 보간으로 연속 센서 복원

## 학습 목표
- 자동차 센서 로그에서 선형 보간으로 연속 센서 복원 절차를 수행합니다.
- ROS2 토픽 또는 MuJoCo 센서 배열에 적용하기 전, 오프라인 CSV로 처리 원리를 확인합니다.

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage3_041_060
conda activate auto_physical_ai
python ex046\main.py
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
| 9 | `from common.data_loader import load_sensor_log` | 실습에 필요한 모듈이나 경로 도구를 불러옵니다. |
| 10 | `` | 코드 구간을 구분해 가독성을 높입니다. |
| 11 | `# 데이터를 시간순으로 정렬한다.` | 데이터를 시간순으로 정렬한다. |
| 12 | `df = load_sensor_log().sort_values("timestamp").reset_index(drop=True)` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 13 | `# 속도와 거리 센서의 짧은 결측 구간을 선형 보간한다.` | 속도와 거리 센서의 짧은 결측 구간을 선형 보간한다. |
| 14 | `for column in ["vehicle_speed_kmh", "front_distance_m"]:` | 지정한 항목을 차례대로 반복 처리합니다. |
| 15 | `    df[column + "_interp"] = df[column].interpolate(method="linear", limit=5)` | 처리 결과를 변수나 데이터 열에 저장합니다. |
| 16 | `print(df[["vehicle_speed_kmh", "vehicle_speed_kmh_interp"]].iloc[20:32])` | 중간 결과 또는 검증 결과를 콘솔에 출력합니다. |

## 확인 문제
1. 이 예제의 처리 기준이 실제 차량에서 달라져야 하는 이유는 무엇인가요?
2. 이상값을 삭제하는 대신 대체하거나 플래그만 남겨야 하는 상황은 언제인가요?
3. 이 처리를 ROS2 센서 콜백에 적용할 때 추가로 고려할 항목은 무엇인가요?
