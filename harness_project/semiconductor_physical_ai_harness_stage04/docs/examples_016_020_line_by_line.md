# 실습 016~020 라인별 해설

## 016 센서 시계열
센서별 그래프를 분리해 단위 차이 왜곡을 피하고, 시간순 정렬·축 이름·격자·고해상도 저장·메모리 해제를 적용합니다.

## 017 Lot 비교
Lot별 평균은 중심, 표준편차는 내부 변동, min/max는 극단 범위를 뜻합니다. 상자그림은 중앙값·사분위수·이상값 후보를 함께 보여줍니다.

## 018 Recipe 비교
표본 수와 불량률을 함께 보며 평균 품질 막대그래프는 탐색용입니다. 통계적 유의성이나 원인을 확정하지 않습니다.

## 019 분포 분석
히스토그램, 왜도, 첨도, 1%·99% 분위수로 분포 치우침과 극단값 후보를 확인합니다.

## 020 기초 대시보드
전체 행, Lot·Recipe 수, 평균 품질, 불량률과 Lot별 표를 단일 HTML로 제공합니다.

## 실행
```bat
conda env create -f environment.yml
conda activate semi-physical-ai
python examples\example_016_sensor_timeseries_plot.py
python examples\example_017_lot_comparison.py
python examples\example_018_recipe_comparison.py
python examples\example_019_sensor_distribution_analysis.py
python examples\example_020_basic_process_dashboard.py
```
