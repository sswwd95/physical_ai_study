# 자동차 Physical AI 하네스 엔지니어링
## 15단계 | 281~300제 | PyMC 기반 차량 부품 고장확률·잔여수명 추정

### 주요 내용
- 검열 수명 데이터
- 부품별 고장확률
- Weibull 수명분포
- 생존확률
- 사후 중앙수명
- 부하·온도 수명 회귀
- 부품별 계층 수명 모델
- RUL 특징 상관관계
- 베이지안 RUL 회귀
- 다중 센서 RUL
- 사후 예측
- 정비 임계시간 초과확률
- R-hat·ESS 진단
- 통합 고장확률·RUL 리포트

### 데이터
- 부품 수명 데이터: 4개 부품 × 120개 = 480행
- RUL 상태 스냅샷: 360행

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
