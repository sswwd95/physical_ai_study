# 자동차 Physical AI 하네스 엔지니어링
## 9단계 | 161~180제 | PyMC 기반 IMU 바이어스·센서 오차 베이즈 추정

가속도·자이로 바이어스, 센서 노이즈, 신용구간, 기준 초과 사후확률,
두 센서 비교, 온도 회귀, 계층 모델, Student-t 강건 모델, R-hat·ESS 진단을 다룹니다.

```bat
conda env create -f environment.yml
conda activate auto_physical_ai
00_run_quick_examples.bat
```

전체 샘플링:
```bat
00_run_all_examples.bat
```

Windows 안정성을 위해 `cores=1`을 사용합니다.
