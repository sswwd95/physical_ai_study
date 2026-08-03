# 반도체 Physical AI 하네스 엔지니어링 — 9단계

실습 041~045는 센서 스케일링, 파생 변수 생성, 통합 전처리 파이프라인을 다룹니다.

## 포함 내용
- StandardScaler 표준화
- Min-Max 정규화
- Robust Scaling
- 변화량·이동평균·이동표준편차·복합 부하 특징
- Pipeline과 ColumnTransformer 기반 통합 전처리
- 스케일러 파라미터와 전처리 메타데이터 저장
- Antigravity용 생성·검증 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_041_standard_scaling.py
python examples\example_042_minmax_normalization.py
python examples\example_043_robust_scaling.py
python examples\example_044_feature_engineering.py
python examples\example_045_integrated_preprocessing_pipeline.py

pytest -q
```

스케일러는 학습 데이터에서만 fit하고 검증·운영 데이터에는 transform만 적용해야 합니다.
