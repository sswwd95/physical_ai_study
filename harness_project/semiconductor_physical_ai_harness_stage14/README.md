# 반도체 Physical AI 하네스 엔지니어링 — 14단계

실습 066~070은 PCA 기반 다변량 공정 모니터링과 이상 센서 기여도 분석을 다룹니다.

## 포함 내용
- StandardScaler와 PCA 정상 기준 모델
- 누적 설명분산 95% 주성분 선택
- 주성분 점수 관리한계
- SPE/Q 잔차 통계량
- 센서별 SPE 기여도
- Lot별 PCA 경보 HTML 대시보드
- 합성 다중 센서 데이터
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_066_train_pca_baseline.py
python examples\example_067_pca_score_monitoring.py
python examples\example_068_spe_q_statistic.py
python examples\example_069_pca_sensor_contributions.py
python examples\example_070_pca_monitoring_dashboard.py

pytest -q
```

PCA 기준 구간과 임계값은 교육용입니다. 실제 Fab에서는 장비·제품·Recipe별 모델 분리와 재검증이 필요합니다.
