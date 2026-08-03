# 반도체 Physical AI 하네스 엔지니어링 — 7단계

실습 031~035는 센서 단위, 시간축, 중복 timestamp, 센서 드리프트의 데이터 품질 관리를 다룹니다.

## 포함 내용
- JSON 기반 센서 단위 계약
- 혼합 단위 입력 검증
- 표준 단위 자동 변환
- 1초 샘플링 간격 이상 탐지
- 중복 timestamp 리포트와 통합 처리
- 최근 120초 선형 추세 기반 드리프트 탐지
- Antigravity용 생성·검증 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_031_validate_sensor_units.py
python examples\example_032_convert_sensor_units.py
python examples\example_033_detect_time_interval_anomalies.py
python examples\example_034_resolve_duplicate_timestamps.py
python examples\example_035_detect_sensor_drift.py

pytest -q
```

## 주의
단위 변환식과 드리프트 임계값은 교육용입니다. 실제 장비에서는 센서 사양서, 계측 교정 이력, 공정 Recipe와 장비 이벤트를 함께 검증해야 합니다.
