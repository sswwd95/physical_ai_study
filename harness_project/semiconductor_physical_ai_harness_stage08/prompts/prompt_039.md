# 실습 039 생성 하네스 프롬프트
역할: 반도체 계측 신호 처리 엔지니어.
목표: Savitzky-Golay 필터로 곡선 형태를 보존하며 노이즈를 줄인다.
필수 조건:
- scipy.signal.savgol_filter를 사용한다.
- window_length=15, polyorder=2를 사용한다.
- mode='interp'를 사용한다.
- 센서별 savgol 결과 열을 저장한다.
