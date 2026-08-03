# 검증 보고서

- Python 예제: 20개
- 라인별 해설 가이드: 20개
- Python 문법 컴파일: 전체 통과
- 수명 데이터: 24행 × 10열
- RUL 스냅샷: 143행 × 7열
- 수명 데이터 장비 수: 24대
- RUL 스냅샷 장비 수: 12대
- 우측 검열 장비 수: 4대
- Exponential·Weibull·검열·계층 수명모형 포함
- 생존확률·중앙수명·그룹 효과·AFT 회귀 포함
- 베이지안 RUL·고장 임박 확률·LOO·MCMC 진단 포함
- 정비 비용 의사결정과 Excel 자동 보고서 포함
- 전체 MCMC 실행은 제작 환경의 실행시간 제약으로 수행하지 않음

## 실행 권장
```bat
conda env create -f environment.yml
conda activate semi-physical-ai-stage13
python verify_environment.py
run_all_windows.bat
```
