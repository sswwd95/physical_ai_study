# 자동차 Physical AI 하네스 엔지니어링
## 5단계 | 081~100제 | 센서 동기화·리샘플링·센서 융합 기초

### 주요 내용
- 센서 주기 측정과 시간 정렬
- 공통 시간축 생성
- 다운샘플링과 업샘플링
- 선형 보간과 최근접 결합
- 결합 허용 오차 비교
- 오프셋과 지연 추정
- 휠·GPS 가중 평균 융합
- IMU 적분과 바이어스 보정
- 상보 필터
- 1차원 칼만 필터
- 통합 센서 데이터셋과 품질 리포트

### 데이터
- IMU 50Hz
- 휠 속도 20Hz
- 전방 거리 10Hz
- GPS 속도 2Hz

### 설치
```bat
conda env create -f environment.yml
conda activate auto_physical_ai
```

### 전체 실행
```bat
00_run_all_examples.bat
```
