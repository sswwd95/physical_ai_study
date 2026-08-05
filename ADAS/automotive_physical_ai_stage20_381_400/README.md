# 자동차 Physical AI 하네스 엔지니어링
## 20단계 | 381~400제 | Stable-Baselines3 PPO 학습·평가·안전 적용 기초

### 주요 내용
- PPO 설치·모델 생성
- 하이퍼파라미터
- 짧은 학습
- 모델 저장·로드
- 결정론적·확률적 평가
- Monitor
- EvalCallback
- CheckpointCallback
- Vector 환경
- VecNormalize
- learning rate·gamma 비교
- 안전 행동 필터
- 안전 필터 전후 성능
- 행동 분포·학습곡선
- 통합 PPO 리포트

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

교육용 학습 스텝은 짧게 설정했습니다. 실제 성능 비교에서는 충분한 학습 스텝과 여러 random seed가 필요합니다.
