# 반도체 Physical AI 하네스 엔지니어링 — 13단계

실습 061~065는 센서 간 상관관계를 반영하는 다변량 공정 모니터링을 다룹니다.

## 포함 내용
- 5개 센서 Z-score와 개별 경보
- Hotelling T² 다변량 거리
- 단변량·다변량 경보 결합
- 0~100 공정 상태 점수
- Lot별 다변량 모니터링 HTML 대시보드
- 합성 다중 센서 공정 데이터
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_061_multisensor_zscore_monitoring.py
python examples\example_062_hotelling_t2.py
python examples\example_063_combine_sensor_alerts.py
python examples\example_064_process_health_score.py
python examples\example_065_multivariate_dashboard.py

pytest -q
```

Hotelling T² 임계값, 상태 점수와 경보 등급은 교육용입니다. 실제 Fab 적용 전 공정 조건별 검증이 필요합니다.
