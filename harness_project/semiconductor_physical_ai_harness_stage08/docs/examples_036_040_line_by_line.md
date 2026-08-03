# 실습 036~040 라인별 해설

## 실습 036 센서 노이즈 수준 분석
1. 기준 신호와 노이즈 신호의 차이를 실제 노이즈로 정의합니다.
2. 노이즈 평균은 편향 여부를 보여줍니다.
3. 노이즈 표준편차는 흔들림 크기를 나타냅니다.
4. RMS는 노이즈의 전체 에너지 크기입니다.
5. SNR은 신호 전력과 노이즈 전력의 비율을 dB로 표현합니다.
6. SNR이 낮은 센서는 상대적으로 노이즈 영향이 큽니다.

## 실습 037 이동평균 필터
1. 이동창 안의 평균값으로 현재 값을 대체합니다.
2. 중심 이동창은 앞뒤 데이터를 함께 사용합니다.
3. 노이즈를 줄이지만 빠른 피크를 낮출 수 있습니다.
4. 창이 커질수록 더 부드럽지만 반응이 느려집니다.
5. 실시간 시스템에서는 중심창 대신 과거창을 사용해야 합니다.
6. 필터값과 원시값을 모두 보존해야 비교할 수 있습니다.

## 실습 038 지수평활
1. 최근 값에 더 큰 가중치를 주는 재귀형 필터입니다.
2. alpha가 클수록 새로운 변화에 빠르게 반응합니다.
3. alpha가 작을수록 더 부드럽지만 지연이 커집니다.
4. 과거 전체 데이터를 저장하지 않아도 계산할 수 있습니다.
5. 실시간 공정 모니터링에 적합한 단순 필터입니다.
6. 공정 전환에서는 지연 특성을 반드시 검토해야 합니다.

## 실습 039 Savitzky-Golay 필터
1. 이동창 안에서 저차 다항식을 적합합니다.
2. 단순 평균보다 곡선의 모양과 피크를 잘 보존할 수 있습니다.
3. window_length는 반드시 홀수여야 합니다.
4. polyorder는 window_length보다 작아야 합니다.
5. 창이 너무 크면 급격한 공정 변화를 과도하게 평활화합니다.
6. 계측 곡선의 미분·추세 분석 전처리에 자주 사용됩니다.

## 실습 040 필터 성능 비교
1. 깨끗한 기준 신호와 필터 결과를 직접 비교합니다.
2. MAE는 평균 절대 복원 오차입니다.
3. RMSE는 큰 오차에 더 민감합니다.
4. roughness는 필터 결과의 잔여 흔들림 정도입니다.
5. 낮은 roughness만 추구하면 실제 변화까지 제거할 수 있습니다.
6. 센서별로 정확도와 반응성을 함께 고려해 필터를 선택합니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_036_noise_level_analysis.py
python examples\example_037_moving_average_filter.py
python examples\example_038_exponential_smoothing.py
python examples\example_039_savgol_filter.py
python examples\example_040_compare_filter_performance.py

pytest -q
```
