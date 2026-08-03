# 반도체 Physical AI 하네스 엔지니어링 — 17단계

실습 081~085는 불량 라벨 생성과 공정 조건별 불량 위험 분석을 다룹니다.

## 포함 내용
- 규칙 기반 생성 불량 라벨
- 기존 검사 라벨과 일치율
- 센서 4분위 구간별 불량률
- Recipe·Tool 교차표와 카이제곱 검정
- 조건별 위험비와 위험차
- HTML 불량 분석 대시보드
- 합성 Wafer 공정·품질 데이터
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_081_generate_defect_labels.py
python examples\example_082_feature_bin_defect_rates.py
python examples\example_083_chi_square_crosstab.py
python examples\example_084_condition_risk_ratio.py
python examples\example_085_defect_analysis_dashboard.py

pytest -q
```

통계적 연관성은 인과관계가 아닙니다. 실제 개선 조치는 DOE, 장비 이력, 품질 전문가 검토 후 결정해야 합니다.
