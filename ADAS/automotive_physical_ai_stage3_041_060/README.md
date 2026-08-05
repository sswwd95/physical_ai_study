# 자동차 Physical AI 하네스 엔지니어링 3단계

## 범위
- 041~060제
- 자동차 센서 로그 전처리
- 결측값 진단과 처리
- 이상값 탐지와 완화
- 시계열 정렬과 통합 전처리 파이프라인

## 권장 환경
- Windows 10
- Anaconda
- Python 3.11
- NumPy / Pandas / Matplotlib / SciPy / scikit-learn
- 이후 MuJoCo 3.6.0, PyMC, robotis_tb3 Burger 실습과 연계

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage3_041_060
conda activate auto_physical_ai
python ex041\main.py
```

전체 실행:
```bat
00_run_all_examples.bat
```

## 예제 구성
각 예제 폴더에는 다음 파일이 있습니다.
- `main.py`: 실행 코드
- `HARNESS_PROMPT.md`: Antigravity에서 재생성·확장할 때 사용할 하네스 프롬프트
- `README.md`: 목표, 절차, 라인별 해설, 실무 포인트
