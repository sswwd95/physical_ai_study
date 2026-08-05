# 예제 457 — 운영 상태기계

```bat
python ex457\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | ` while v.is_running() and d.time<18:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `  t=d.time; cmd=(0,0) if t<3 else (7,7) if t<9 else (-4,4) if t<13 else (5,6) if t<17 else (0,0); wheels(d,*cmd); print(t,cmd); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
