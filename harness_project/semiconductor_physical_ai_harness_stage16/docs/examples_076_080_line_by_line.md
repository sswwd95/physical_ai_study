# 실습 076~080 라인별 해설

## 실습 076 정규성 검정
1. 정규성은 공정 능력지수 해석의 중요한 가정입니다.
2. Shapiro-Wilk는 표본 분포가 정규분포와 유사한지 평가합니다.
3. D'Agostino K²는 왜도와 첨도를 함께 사용합니다.
4. p-value가 작으면 정규성 가정을 의심합니다.
5. 표본이 크면 작은 차이도 유의하게 나올 수 있습니다.
6. 검정 결과와 히스토그램·Q-Q plot을 함께 보는 것이 좋습니다.

## 실습 077 비정규 공정 능력
1. 정규 가정 Ppk는 평균과 표준편차를 사용합니다.
2. 비대칭 분포에서는 상·하한 꼬리 길이가 다를 수 있습니다.
3. 분위수 방식은 양쪽 꼬리를 따로 반영합니다.
4. 0.135%와 99.865%는 정규분포의 약 ±3σ에 대응합니다.
5. 분위수 추정에는 충분한 표본 수가 필요합니다.
6. 분포 변환이나 적합 분포 모델도 대안이 될 수 있습니다.

## 실습 078 Bootstrap Cpk
1. 원본 표본에서 복원추출해 새로운 표본을 만듭니다.
2. 각 표본에서 Cpk를 다시 계산합니다.
3. 반복된 Cpk 분포로 불확실성을 추정합니다.
4. 2.5%와 97.5% 분위수를 95% 신뢰구간으로 사용합니다.
5. 표본이 작거나 이상값이 많으면 구간이 넓어질 수 있습니다.
6. 점추정치만 보는 것보다 보수적 판단이 가능합니다.

## 실습 079 불확실성 비교
1. 정규성 검정으로 지수 계산 방법을 선택합니다.
2. 정규성이 기각되면 분위수 기반 지수를 권장합니다.
3. Bootstrap 구간은 지수 추정의 안정성을 보여줍니다.
4. 하한이 1보다 낮으면 실제 능력이 부족할 가능성을 고려합니다.
5. 권장값과 관측 Cpk가 크게 다르면 분포 가정을 재검토합니다.
6. 자동 권장은 전문가 검토를 대체하지 않습니다.

## 실습 080 종합 판정
1. 권장 지수와 Bootstrap 하한을 함께 사용합니다.
2. CAPABLE은 점추정치와 보수적 하한이 모두 양호한 경우입니다.
3. MARGINAL은 평균적으론 가능하지만 여유가 부족한 경우입니다.
4. NOT_CAPABLE은 규격 대비 능력이 부족한 경우입니다.
5. 정규성 기각 또는 낮은 신뢰구간 하한은 추가 검토 대상으로 표시합니다.
6. 실제 Fab 승인 기준은 고객·제품·공정별로 다릅니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_076_normality_tests.py
python examples\example_077_nonnormal_capability.py
python examples\example_078_bootstrap_cpk_interval.py
python examples\example_079_capability_uncertainty_comparison.py
python examples\example_080_capability_decision_report.py

pytest -q
```
