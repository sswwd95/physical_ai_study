# 핵심 소스 라인별 해설

- `scene.py`: 교육용 드론, 전방 카메라, 이동 표적을 정의한다.
- `vision.py`: HSV 빨간색 마스크, contour, 바운딩 박스, 중심 좌표를 계산한다.
- `AlphaBetaTracker`: 짧은 검출 누락 동안 위치를 예측한다.
- `controller.py`: 화면 오차를 yaw·roll로, 객체 크기를 pitch로, 고도 오차를 vz로 바꾼다.
- `SAFETY_BACKOFF`: 객체가 너무 가까우면 후진한다.
- `SEARCH`: 객체가 사라지면 yaw 회전으로 재탐색한다.
- `main.py`: 렌더링→탐지→추적→제어→로그 순서로 실행한다. 18~23초에 표적을 숨겨 이탈을 재현한다.
- `analysis.py`: 지연시간과 추적 성공률의 사후분포 및 94% HDI를 계산한다.
- `rl_env.py`: PPO가 직접 비행하지 않고 제어 이득을 조정하도록 설계한다.
