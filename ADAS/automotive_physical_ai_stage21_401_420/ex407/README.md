# 예제 407 — Free Camera

## 실행
```bat
python ex407\main.py
```

## 핵심
`launch_passive()`에서는 사용자 코드가 `mj_step()`으로 물리를 진행하고 `sync()`로 화면과 입력을 동기화합니다. 공유 상태 변경은 `lock()` 안에서 수행합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.viewer_utils import load,run,wheels` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 2 | `mj,m,d=load()` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 3 | `with mj.viewer.launch_passive(m,d) as v:` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 4 | ` v.cam.type=mj.mjtCamera.mjCAMERA_FREE; v.cam.lookat[:]=[1,0,.2]; v.cam.distance=5; v.cam.azimuth=135; v.cam.elevation=-25` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 5 | ` run(mj,m,d,v,10,lambda m,d:wheels(d,6,7))` | Viewer 또는 물리 상태를 설정·실행합니다. |
