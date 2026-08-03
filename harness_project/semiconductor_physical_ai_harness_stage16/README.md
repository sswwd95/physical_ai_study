# 반도체 Physical AI 하네스 엔지니어링 — 16단계

실습 076~080은 정규성 가정, 비정규 공정 능력, Bootstrap Cpk 신뢰구간과 종합 판정을 다룹니다.

## 포함 내용
- Shapiro-Wilk와 D'Agostino K² 검정
- 왜도와 초과첨도
- 정규 가정 Ppk와 분위수 기반 능력지수
- 2000회 Bootstrap Cpk 95% 신뢰구간
- 권장 지수 선택
- CAPABLE·MARGINAL·NOT_CAPABLE 판정
- HTML·CSV·JSON 종합 리포트
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_076_normality_tests.py
python examples\example_077_nonnormal_capability.py
python examples\example_078_bootstrap_cpk_interval.py
python examples\example_079_capability_uncertainty_comparison.py
python examples\example_080_capability_decision_report.py

pytest -q
```

모든 판정 기준은 교육용입니다. 실제 Fab 승인에는 공정 안정성, 측정시스템 분석, 고객 규격과 표본 설계를 함께 검토해야 합니다.
