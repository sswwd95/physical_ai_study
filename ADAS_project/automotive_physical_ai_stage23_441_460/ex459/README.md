# 예제 459 — 트윈 오차 로그

```bat
python ex459\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `import pandas as pd` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `from common.ops import out` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `rows=[]` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | ` while v.is_running() and d.time<10:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `  wheels(d,7,8); mj.mj_step(m,d); pred=.35*d.time; actual=float(d.qpos[0]); rows.append([d.time,pred,actual,actual-pred]); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 10 | `p=out("ex459.csv"); pd.DataFrame(rows,columns=["time","pred","actual","error"]).to_csv(p,index=False); print(p)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
