# 예제 164 하네스 프롬프트

20년차 Robotics 엔지니어로서 Windows 10, Anaconda, PyMC, ArviZ 기반의 **가속도 바이어스 단일 모수 추정** 실습을 작성한다.

요구사항:
- `common.bayes_utils`를 사용한다.
- 사전분포, 우도, 사후분포를 구분해 설명한다.
- draws=500, tune=500, chains=2, cores=1, random_seed=42를 사용한다.
- 결과는 outputs에 CSV·PNG·JSON으로 저장한다.
- posterior mean, 95% credible interval, R-hat, ESS 중 필요한 값을 출력한다.
- ROS2 `/imu` 공분산과 진단 토픽 연결점을 설명한다.
- 온도, 정지 검출, 장착 축, 시간 동기화의 실차 고려사항을 기록한다.
