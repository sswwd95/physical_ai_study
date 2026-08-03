# 반도체 Physical AI 하네스 엔지니어링 — 6단계

실습 026~030은 반도체 장비 센서의 이상값 탐지와 보정 품질 검증을 다룹니다.

## 포함 내용
- 센서별 물리 범위 검사
- IQR 기반 이상값 후보 탐지
- Z-score 기반 이상 행 탐지
- Hampel 필터 기반 국소 이상값 보정
- 중앙값·선형 보간·Hampel 복원 품질 비교
- 완전 데이터와 이상값 주입 데이터
- Antigravity 생성·검증 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_026_physical_range_check.py
python examples\example_027_iqr_outlier_detection.py
python examples\example_028_zscore_outlier_detection.py
python examples\example_029_hampel_filter.py
python examples\example_030_compare_outlier_correction.py

pytest -q
```

## 주의
통계적 이상값이 반드시 불량이나 고장을 의미하지는 않습니다. 실제 공정에서는 Lot, Recipe, 공정 전환, 장비 이벤트와 함께 검토해야 합니다.
