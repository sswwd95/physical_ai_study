# 실습 041~045 라인별 해설

## 실습 041 표준화
1. StandardScaler는 센서별 평균과 표준편차를 학습합니다.
2. 각 값에서 평균을 빼고 표준편차로 나눕니다.
3. 단위가 다른 센서를 같은 규모로 비교할 수 있습니다.
4. 평균과 scale은 추론 데이터에도 동일하게 적용해야 합니다.
5. 이상값이 평균과 표준편차에 영향을 줄 수 있습니다.
6. 파라미터 저장은 학습·배포 일관성에 필요합니다.

## 실습 042 Min-Max 정규화
1. 센서 최솟값을 0, 최댓값을 1로 변환합니다.
2. 신경망이나 거리 기반 알고리즘에서 자주 사용합니다.
3. 값의 순서와 상대 간격은 유지됩니다.
4. 극단값이 존재하면 일반 데이터가 좁은 범위에 모일 수 있습니다.
5. 새 데이터가 학습 범위를 벗어나면 0~1 밖 값이 생길 수 있습니다.
6. data_min과 data_max를 반드시 저장합니다.

## 실습 043 Robust Scaling
1. 평균 대신 중앙값을 사용합니다.
2. 표준편차 대신 IQR을 사용합니다.
3. 이상값이 있는 센서에서 더 안정적일 수 있습니다.
4. 결과 중앙값은 대체로 0 근처가 됩니다.
5. IQR이 매우 작은 센서는 스케일 안정성을 확인해야 합니다.
6. 실제 모델 성능으로 StandardScaler와 비교해야 합니다.

## 실습 044 파생 변수
1. diff는 현재값과 직전값의 변화량입니다.
2. 이동평균은 단기 추세를 나타냅니다.
3. 이동표준편차는 최근 변동성을 나타냅니다.
4. 진동×전류는 기계적 부하를 표현하는 교육용 복합 지표입니다.
5. 기준값 이탈은 정상점에서 얼마나 벗어났는지 보여줍니다.
6. 시간 특징은 교대·시간대 패턴을 분석할 때 활용할 수 있습니다.

## 실습 045 통합 전처리 파이프라인
1. 특징 생성은 원시 데이터를 모델 입력으로 바꾸는 첫 단계입니다.
2. rolling과 diff 때문에 초기 결측값이 생길 수 있습니다.
3. SimpleImputer가 중앙값으로 결측을 채웁니다.
4. RobustScaler가 이상값 영향을 줄이며 스케일을 맞춥니다.
5. Pipeline은 같은 순서의 처리를 학습과 추론에 재사용합니다.
6. 메타데이터는 입력 열·출력 열·처리 단계를 추적하게 합니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_041_standard_scaling.py
python examples\example_042_minmax_normalization.py
python examples\example_043_robust_scaling.py
python examples\example_044_feature_engineering.py
python examples\example_045_integrated_preprocessing_pipeline.py

pytest -q
```
