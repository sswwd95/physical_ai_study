# 예제 460 — 통합 운영 검증

```bat
python ex460\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `import numpy as np` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `from common.ops import xy,dist,Delay,save` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `b=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base"); dock=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"dock"); q=Delay(20); rng=np.random.default_rng(42); rows=[]` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | ` while v.is_running() and d.time<22:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `  p=xy(d,b); dd=dist(p,xy(d,dock)); gd=dist(p,(2,2)); des=(7,7)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 10 | `  if gd<1.3:des=(-5,5)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 11 | `  if dd<1.8:des=(3,3)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 12 | `  if dd<.6:des=(0,0)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 13 | `  app=q.push(des)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 14 | `  if rng.random()<.1: app=(float(d.ctrl[0]),float(d.ctrl[1]))` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 15 | `  wheels(d,*app); mj.mj_step(m,d); rows.append([dd,gd,*d.ctrl[:2]]); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 16 | `r={"samples":len(rows),"min_dock":min(x[0] for x in rows) if rows else None}; print(r,save(r,"ex460.json"))` | 디지털 트윈 운영 검증 코드를 실행합니다. |
