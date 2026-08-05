# 자동차 Physical AI 하네스 엔지니어링
## 2단계 | 021~040제 | Python·NumPy·Pandas 자동차 센서 데이터 기초

이 패키지는 ROS2 Humble, MuJoCo, PyMC 실습 전에 필요한 Python 센서 데이터 처리 기초를 학습합니다.

## 권장 실행 순서
1. Anaconda Prompt 실행
2. 1단계에서 만든 `auto_physical_ai` 환경 활성화
3. 필요 시 `conda env update -f environment_stage2.yml --prune`
4. `00_run_all_examples.bat` 실행 또는 예제를 하나씩 실행

## 예제 목록
| 번호 | 주제 |
|---:|---|
| 021 | Python 변수와 자동차 센서 단위 |
| 022 | 리스트로 센서 시계열 다루기 |
| 023 | 딕셔너리로 센서 프레임 표현 |
| 024 | 조건문으로 안전거리 판정 |
| 025 | 반복문으로 센서 이상값 찾기 |
| 026 | 함수로 단위 변환하기 |
| 027 | NumPy 배열 생성과 형상 확인 |
| 028 | NumPy 벡터 연산 |
| 029 | NumPy 통계량 계산 |
| 030 | NumPy 마스킹으로 위험구간 추출 |
| 031 | CSV 파일 읽기 |
| 032 | DataFrame 구조와 자료형 확인 |
| 033 | 열 선택과 파생 변수 생성 |
| 034 | 행 필터링과 조건 결합 |
| 035 | 정렬과 상위 위험 샘플 |
| 036 | 그룹별 통계 |
| 037 | 이동평균으로 노이즈 완화 |
| 038 | 차분으로 급가속 탐지 |
| 039 | 센서 데이터 시각화 |
| 040 | 미니 통합 진단 리포트 |

## 폴더 구조
- `data/vehicle_sensor_log.csv`: 공통 자동차 센서 샘플 300행
- `common/`: 공통 경로와 데이터 로더
- `ex021`~`ex040`: 각 예제의 코드·하네스 프롬프트·라인별 해설
- `outputs/`: 그래프와 분석 결과가 저장되는 폴더

## Windows 실행
```bat
cd /d C:\work\automotive_physical_ai_stage2_021_040
conda activate auto_physical_ai
python ex031\main.py
```

## 주의
CSV의 값은 교육용 합성 데이터입니다. 실제 자동차 제어 판단에 직접 사용하지 마십시오.
