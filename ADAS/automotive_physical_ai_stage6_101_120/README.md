# 자동차 Physical AI 하네스 엔지니어링
## 6단계 | 101~120제 | MuJoCo TurtleBot3 Burger 모델 로딩·센서·구동 기초

### 핵심 학습 내용
- MuJoCo 3.6.0 설치와 버전 확인
- ROBOTIS `robotis_mujoco_menagerie/robotis_tb3` XML 탐색
- 오프라인 교육용 TurtleBot3 유사 모델 폴백
- 바디·관절·액추에이터·센서 구조 조회
- 헤드리스 물리 시뮬레이션
- 전진·제자리 회전·차동 회전
- 관절 센서·IMU·베이스 자세 읽기
- 제어 포화
- CSV 로그 저장
- 통합 구동·센서 진단

### 설치
```bat
conda env create -f environment.yml
conda activate auto_physical_ai
```

### ROBOTIS 모델 저장소 사용
```bat
set ROBOTIS_MUJOCO_MENAGERIE=C:\work\robotis_mujoco_menagerie
python ex102\main.py
```

공식 저장소를 찾지 못하면 `models/tb3_burger_training.xml` 교육용 모델을 자동 사용합니다.

### 전체 실행
```bat
00_run_all_examples.bat
```

### 주의
공식 ROBOTIS XML의 액추에이터·센서 이름과 순서는 교육용 모델과 다를 수 있습니다.
실무 코드에서는 이름 기반 탐색과 존재 여부 검사가 필요합니다.
