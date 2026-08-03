# 반도체 Physical AI 하네스 엔지니어링 — 3단계

실습 011~015는 반도체 장비 센서 로그의 기초 분석을 다룹니다.

## 포함 내용
- 센서 CSV 로딩과 데이터 구조 검사
- 센서별 기술통계와 변동계수
- 30초 이동평균·이동표준편차
- 센서 간 상관관계
- Lot별 설비 상태 요약 리포트
- 실행용 합성 데이터 600행
- Antigravity용 생성·검증 하네스 프롬프트
- 라인별 해설과 pytest 검사

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_011_load_and_inspect_sensor_log.py
python examples\example_012_sensor_descriptive_statistics.py
python examples\example_013_rolling_statistics.py
python examples\example_014_sensor_correlation_analysis.py
python examples\example_015_equipment_health_summary.py

pytest -q
```

모든 임계값과 상태 등급은 교육용입니다.
