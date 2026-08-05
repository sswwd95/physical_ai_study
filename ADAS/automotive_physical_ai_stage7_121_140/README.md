# 자동차 Physical AI 하네스 엔지니어링
## 7단계 | 121~140제 | TurtleBot3 차동구동 운동학·오도메트리·궤적 분석

### 주요 내용
- TurtleBot3 Burger 차동구동 파라미터
- 좌우 바퀴 각속도와 Twist 변환
- 직진·제자리 회전·원호 운동
- 오도메트리 수치 적분
- 복합 명령 궤적 생성
- XY 궤적 시각화
- 누적 이동거리와 최종 변위
- 적분 주기 영향
- 바퀴 반지름·차축 간격 오차
- 휠 슬립과 궤적 오차
- 통합 궤적·바퀴 명령·진단 리포트

### 설치
```bat
conda env create -f environment.yml
conda activate auto_physical_ai
```

### 개별 실행
```bat
python ex121\main.py
```

### 전체 실행
```bat
00_run_all_examples.bat
```

### 실무 주의사항
교육용 오도메트리는 평면 운동과 이상적인 바퀴 접촉을 가정합니다.
실차에서는 엔코더 분해능, 타이어 변형, 휠 슬립, 바닥 마찰, 시간 지연, IMU 바이어스를 함께 고려해야 합니다.
