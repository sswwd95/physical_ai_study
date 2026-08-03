# 검증 보고서

- Python 예제: 20개
- 라인별 해설 가이드: 20개
- Python 문법 검사: 전체 통과
- 센서 데이터: 420행 × 10열
- 교육용 실제 이상 라벨 수: 40건
- 단변량·문맥·다변량 이상 탐지 포함
- Isolation Forest, LOF, One-Class SVM 포함
- Robust Covariance, PCA 재구성 오차 포함
- 모델 평가, 임계값 최적화, 앙상블 포함
- Excel 자동 이상 탐지 보고서 포함

## 권장 실행
```bat
conda env create -f environment.yml
conda activate semi-physical-ai-stage05
run_all_windows.bat
```

## 주의
true_anomaly는 교육과 평가를 위한 합성 라벨입니다. 실제 공정에서는 정비 이력,
불량 검사 결과, 엔지니어 판정 등 신뢰 가능한 기준과 함께 모델을 검증해야 합니다.
