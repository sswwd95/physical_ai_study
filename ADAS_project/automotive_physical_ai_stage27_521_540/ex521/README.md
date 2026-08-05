# 예제 521 — ADAS 확장 scene 점검

## 실행
```bat
python ex521\main.py
```

## 주의
이 예제의 ADAS 임계값은 교육용이며 실제 차량 안전 인증값이 아닙니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.adas_tb3_utils import *` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 2 | `p=scene("ex521.xml",'<geom type="box" pos="3 .6 .01" size="8 .025 .01" rgba="1 1 1 1"/><geom type="box" pos="3 -.6 .01" size="8 .025 .01" rgba="1 1 1 1"/>'); mj,m,d=load(p); print(p,m.nbody,m.nu); mj.viewer.launch(m,d)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
