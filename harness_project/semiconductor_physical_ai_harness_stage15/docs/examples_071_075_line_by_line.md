# 실습 071~075 라인별 해설

## 실습 071 Cp·Cpk
1. Cp는 규격 폭과 단기 변동 폭을 비교합니다.
2. 부분군 내부 표준편차 평균을 단기 sigma의 교육용 추정치로 사용합니다.
3. Cp는 공정 중심이 규격 중앙에 있다고 가정한 잠재 능력입니다.
4. Cpu와 Cpl은 상한·하한 방향 능력을 각각 봅니다.
5. Cpk는 Cpu와 Cpl 중 작은 값이므로 중심 치우침을 반영합니다.
6. 공정이 불안정하면 Cp와 Cpk 해석은 제한됩니다.

## 실습 072 Pp·Ppk
1. 전체 기간 표준편차는 Lot 간 이동과 장기 변동을 포함합니다.
2. Pp는 장기 전체 변동 대비 규격 폭을 봅니다.
3. Ppk는 장기 변동과 중심 치우침을 함께 반영합니다.
4. 일반적으로 장기 변동이 크면 Ppk가 Cpk보다 낮아질 수 있습니다.
5. 두 지수 차이가 크면 시간에 따른 공정 변화 가능성을 검토합니다.
6. 측정시스템 오차도 지수에 영향을 줍니다.

## 실습 073 규격 이탈률
1. LSL 미만과 USL 초과를 따로 표시합니다.
2. 실제 관측 이탈률은 데이터 안의 규격 외 비율입니다.
3. PPM은 이 비율을 백만 개 기준으로 환산합니다.
4. 표본이 작으면 관측 PPM 변동이 큽니다.
5. 분포 가정 기반 예측 PPM과 실제 관측 PPM은 다를 수 있습니다.
6. Lot과 Recipe별로 분리해 보는 것이 중요합니다.

## 실습 074 Lot별 능력 비교
1. Lot마다 평균과 변동이 다를 수 있습니다.
2. 각 Lot 내부에서 부분군을 다시 구성합니다.
3. Cp/Cpk는 단기 능력, Pp/Ppk는 장기 성능을 봅니다.
4. 규격 이탈률은 실제 결과와 지수를 함께 해석하게 합니다.
5. Cpk가 낮은 Lot은 중심 치우침 또는 큰 변동을 확인합니다.
6. Recipe 차이와 장비 이벤트를 함께 비교합니다.

## 실습 075 공정 능력 대시보드
1. Cp/Cpk와 Pp/Ppk를 같은 화면에서 비교합니다.
2. 규격 이탈률과 PPM은 실제 관측 품질 결과를 보여줍니다.
3. Lot별 표는 문제가 집중된 생산 단위를 찾게 합니다.
4. 최저 Cpk Lot을 우선 조사 대상으로 표시합니다.
5. 공정 능력지수는 공정 안정성과 측정 신뢰성이 전제입니다.
6. HTML과 JSON을 함께 제공해 사람과 시스템이 모두 활용할 수 있습니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_071_cp_cpk.py
python examples\example_072_pp_ppk.py
python examples\example_073_spec_violation_rate.py
python examples\example_074_lot_capability_comparison.py
python examples\example_075_capability_dashboard.py

pytest -q
```
