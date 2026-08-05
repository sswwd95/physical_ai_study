# 예제 413 — Geom 색상 변경

## 실행
```bat
python ex413\main.py
```

## 핵심
`launch_passive()`에서는 사용자 코드가 `mj_step()`으로 물리를 진행하고 `sync()`로 화면과 입력을 동기화합니다. 공유 상태 변경은 `lock()` 안에서 수행합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,math` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 2 | `from common.viewer_utils import load` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 3 | `mj,m,d=load(); gid=mj.mj_name2id(m,mj.mjtObj.mjOBJ_GEOM,"chassis")` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 4 | `with mj.viewer.launch_passive(m,d) as v:` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 5 | ` while v.is_running() and d.time<10:` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 6 | `  mj.mj_step(m,d); x=.5+.5*math.sin(d.time*2)` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 7 | `  with v.lock(): m.geom_rgba[gid]=[x,.2,1-x,1]` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 8 | `  v.sync(); time.sleep(m.opt.timestep)` | Viewer 또는 물리 상태를 설정·실행합니다. |
