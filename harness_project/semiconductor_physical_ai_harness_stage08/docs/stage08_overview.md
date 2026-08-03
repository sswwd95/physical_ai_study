# 8단계 개요: 센서 노이즈와 필터링

| 실습 | 주제 | 주요 출력 |
|---:|---|---|
|036|센서 노이즈 수준 분석|`sensor_noise_summary.csv`|
|037|이동평균 필터|`sensor_moving_average.csv`|
|038|지수평활|`sensor_exponential_smoothing.csv`|
|039|Savitzky-Golay 필터|`sensor_savgol_filtered.csv`|
|040|필터 성능 비교|`filter_performance_comparison.csv`|

## 실무 핵심
필터는 노이즈를 줄이는 동시에 실제 공정 변화도 약화시킬 수 있습니다. 따라서 정확도, 반응속도, 피크 보존, 실시간 적용 가능성을 함께 비교해야 합니다.
