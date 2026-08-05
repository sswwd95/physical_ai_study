# 자동차 Physical AI 하네스 엔지니어링
## 18단계 | 341~360제 | 자동차 장애물·안전거리·충돌 위험 제어 기초

### 주요 내용
- 상대속도·접근속도
- TTC
- 반응거리·제동거리·안전거리
- 마찰계수 영향
- 안전거리 부족 탐지
- 위험등급
- 감속·비상정지
- 경고 히스테리시스
- 장애물 회피 조향
- 안전거리 기반 속도 제한
- Logistic Regression·Random Forest 위험 예측
- MuJoCo 안전정지
- 통합 안전 제어

### 데이터
180초, 10Hz, 총 1,800행의 합성 충돌 위험 로그입니다.
세 구간의 위험 접근 시나리오를 포함합니다.

### 설치
```bat
conda env create -f environment.yml
conda activate auto_physical_ai
```

### 전체 실행
```bat
00_run_all_examples.bat
```
