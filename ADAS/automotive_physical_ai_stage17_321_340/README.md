# 자동차 Physical AI 하네스 엔지니어링
## 17단계 | 321~340제 | MuJoCo 기반 경로 추종·Pure Pursuit·Stanley 제어 기초

### 주요 내용
- 웨이포인트 경로
- 최근접점·진행방향·횡방향 오차
- 룩어헤드 목표점
- Pure Pursuit
- Stanley 제어
- 게인·룩어헤드 영향
- 차선변경·원형 경로
- 곡률 기반 속도 제한
- 경로 이탈 복구
- MuJoCo 액추에이터 연계
- 통합 제어기 비교

### 설치
```bat
conda env create -f environment.yml
conda activate auto_physical_ai
```

### 전체 실행
```bat
00_run_all_examples.bat
```

MuJoCo가 없어도 339제를 제외한 수치 경로추종 예제는 실행할 수 있습니다.
