# 예제 420 — 통합 안전정지

## 실행
```bat
python ex420\main.py
```

## 핵심
`launch_passive()`에서는 사용자 코드가 `mj_step()`으로 물리를 진행하고 `sync()`로 화면과 입력을 동기화합니다. 공유 상태 변경은 `lock()` 안에서 수행합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,json` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 2 | `from common.viewer_utils import load,wheels,out` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 3 | `mj,m,d=load(); b=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base"); o=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"obstacle"); rows=[]` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 4 | `with mj.viewer.launch_passive(m,d) as v:` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 5 | ` v.cam.type=mj.mjtCamera.mjCAMERA_TRACKING; v.cam.trackbodyid=b; v.cam.distance=3` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 6 | ` while v.is_running() and d.time<15:` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 7 | `  dist=float(((d.xpos[b]-d.xpos[o])**2).sum()**.5); wheels(d,0,0) if dist<.8 else wheels(d,7,7)` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 8 | `  mj.mj_step(m,d); rows.append(dist); v.sync(); time.sleep(m.opt.timestep)` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 9 | `r={"samples":len(rows),"min_distance":min(rows) if rows else None}; p=out("ex420_report.json"); p.write_text(json.dumps(r,indent=2)); print(r,p)` | Viewer 또는 물리 상태를 설정·실행합니다. |
