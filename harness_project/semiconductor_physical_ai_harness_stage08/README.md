# 반도체 Physical AI 하네스 엔지니어링 — 8단계

실습 036~040은 센서 노이즈 수준 분석과 필터 성능 비교를 다룹니다.

## 포함 내용
- 센서별 노이즈 평균·표준편차·RMS·SNR
- 중심 이동평균 필터
- 지수평활 필터
- Savitzky-Golay 필터
- 필터별 MAE·RMSE·roughness 비교
- 깨끗한 기준 신호와 노이즈 신호
- Antigravity 생성·검증 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

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

필터 파라미터는 교육용이며 실제 장비 적용 전 센서 응답속도와 공정 변화 특성을 검증해야 합니다.
