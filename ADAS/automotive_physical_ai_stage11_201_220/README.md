# 자동차 Physical AI 하네스 엔지니어링
## 11단계 | 201~220제 | 자동차 주행 상태·이상 주행 탐지 기초

### 주요 내용
- 규칙 기반 주행 상태 분류
- 급가속·급감속·급조향
- 전방 위험 접근과 TTC 등급
- 모터 과전류
- Z-score·IQR·이동 통계
- 복합 위험 점수
- 이상 이벤트 구간 병합
- 혼동행렬·precision·recall
- Isolation Forest
- 규칙 기반과 비지도 탐지 비교
- 통합 이상 탐지 파이프라인

### 데이터
180초, 10Hz, 총 1,800행의 합성 주행 로그를 포함합니다.
급가속, 급감속, 급조향, 위험 접근, 모터 과부하 이벤트를 삽입했습니다.

### 설치
```bat
conda env create -f environment.yml
conda activate auto_physical_ai
```

### 전체 실행
```bat
00_run_all_examples.bat
```
