# 반도체 Physical AI 하네스 엔지니어링 — 10단계

실습 046~050은 시계열 데이터 분할, 데이터 누출 방지, 전처리 재사용, 스키마·품질 종합 검증을 다룹니다.

## 포함 내용
- 시간 순서 기반 train·validation·test 분할
- 데이터셋 시간 겹침과 timestamp 중복 검사
- 학습 데이터 전용 fit 원칙
- joblib 전처리 객체 저장·복원
- JSON 스키마 검증
- CSV·HTML 데이터 품질 종합 리포트
- Antigravity 하네스 프롬프트와 라인별 해설
- pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_046_time_based_split.py
python examples\example_047_data_leakage_check.py
python examples\example_048_save_and_restore_preprocessor.py
python examples\example_049_schema_validation.py
python examples\example_050_data_quality_report.py

pytest -q
```

모든 품질 점수와 기준은 교육용이며 실제 Fab 승인 기준이 아닙니다.
