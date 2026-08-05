# 예제 446 — 센서 드롭아웃

```bat
python ex446\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `import numpy as np` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `rng=np.random.default_rng(21); last=np.zeros(m.nsensordata)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | ` while v.is_running() and d.time<10:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  wheels(d,6,6); mj.mj_step(m,d)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `  if rng.random()>.25:last=d.sensordata.copy()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 10 | `  print(last); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
