# 설계 기준

프로젝트 통합 흐름:
센서 → 상태추정 → 경로추종 → 위험판단 → 안전제어 → 상태진단 → Viewer 시각화

Viewer API:
- launch_passive
- is_running
- sync
- lock
- cam
- opt

실차 적용 시 Viewer 색상·마커는 진단용이며,
긴급정지와 액추에이터 제한은 별도의 독립 안전계층으로 구현해야 합니다.
