# 반도체 Physical AI 하네스 엔지니어링 — 12단계

실습 056~060은 작은 공정 평균 이동 탐지와 통합 경보 설계를 다룹니다.

## 포함 내용
- EWMA 관리도
- 양·음 CUSUM 관리도
- 작은 평균 이동 탐지 지연 계산
- 기준 구간 오경보율과 이동별 탐지 성능 비교
- 개별값·EWMA·CUSUM 투표형 통합 경보
- 합성 평균 이동 데이터
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_056_ewma_control_chart.py
python examples\example_057_cusum_control_chart.py
python examples\example_058_small_shift_detection.py
python examples\example_059_compare_control_chart_performance.py
python examples\example_060_integrated_process_alerts.py

pytest -q
```

모든 경보 기준은 교육용이며 실제 장비 정지, 인터록, Recipe 변경 명령에는 사용할 수 없습니다.
