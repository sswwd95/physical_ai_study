# 반도체 Physical AI 하네스 엔지니어링 — 11단계

실습 051~055는 공정 통계적 관리(SPC)의 기초와 관리도 경보 규칙을 다룹니다.

## 포함 내용
- baseline 평균·표준편차·σ 구간
- X-bar 관리도
- 개별값 관리도
- 이동범위 관리도
- Western Electric 규칙 4종
- 합성 온도 공정 데이터
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_051_spc_baseline_summary.py
python examples\example_052_xbar_control_chart.py
python examples\example_053_individuals_chart.py
python examples\example_054_moving_range_chart.py
python examples\example_055_western_electric_rules.py

pytest -q
```

관리한계는 규격 한계와 다르며, 실제 공정 적용 전 기준 구간의 안정성과 부분군 구성을 검증해야 합니다.
