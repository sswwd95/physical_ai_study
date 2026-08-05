# 검증 보고서

- Python 예제: 20개
- 라인별 해설 가이드: 20개
- Python 문법 검사: 전체 통과
- 센서 데이터: 360행 × 9열
- 점진 드리프트 구간 포함
- 급격한 다중 센서 변화 구간 포함
- CUSUM, EWMA, 분산비, PCA 거리, Mahalanobis 거리 예제 포함
- Excel 자동 변화 감지 보고서 예제 포함

## 권장 실행
```bat
conda env create -f environment.yml
conda activate semi-physical-ai-stage04
run_all_windows.bat
```

## 주의
본 단계의 임계값은 교육용입니다. 실제 반도체 장비에서는 장비·챔버·레시피별
정상 기준 구간과 경보 정책을 별도로 승인해야 합니다.
