# 자동차 Physical AI 하네스 엔지니어링
## 10단계 | 181~200제 | PyMC 기반 휠 슬립·오도메트리 불확실성 추정

### 주요 내용
- 슬립률 기술통계와 사전분포
- 전체·노면별 슬립률 사후추정
- 슬립 기준 초과 확률
- 거리·회전각 오도메트리 오차 추정
- 슬립률과 거리오차 베이지안 회귀
- IMU 변동·휠 속도차 기반 슬립 예측
- 슬립 위험 로지스틱 회귀
- 노면별 계층 모델
- Student-t 강건 모델
- 사후 예측 분포
- R-hat·ESS 진단
- 통합 불확실성 리포트

### 설치
```bat
conda env create -f environment.yml
conda activate auto_physical_ai
```

### 빠른 확인
```bat
00_run_quick_examples.bat
```

### 전체 실행
```bat
00_run_all_examples.bat
```

Windows 안정성을 위해 PyMC 샘플링은 `cores=1`을 사용합니다.
