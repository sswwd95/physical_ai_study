# 자동차 Physical AI 하네스 엔지니어링
## 16단계 | 301~320제 | MuJoCo 기반 자동차 주행 제어·PID 기초

### 주요 내용
- PID 클래스와 오차 항
- P·PI·PID 속도 응답
- 출력 포화·데드존·안티와인드업
- 외란 억제와 계단 목표 추종
- Twist와 바퀴 속도 변환
- 좌우 바퀴 독립 제어
- 각속도·횡방향 오차 제어
- 복합 선속도·각속도 제어
- PID 게인 그리드 탐색
- 샘플링 주기 영향
- MuJoCo 액추에이터 스모크 테스트
- 통합 PID 진단 리포트

### 설치
```bat
conda env create -f environment.yml
conda activate auto_physical_ai
```

### 전체 실행
```bat
00_run_all_examples.bat
```

MuJoCo가 없는 경우 319제를 제외한 수치제어 예제는 실행할 수 있습니다.
