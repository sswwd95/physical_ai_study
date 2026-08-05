# 예제 449 — 패킷 손실

```bat
python ex449\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `import numpy as np` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `rng=np.random.default_rng(8); applied=(0,0)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | ` while v.is_running() and d.time<12:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  if rng.random()>.2: applied=(7,9)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `  wheels(d,*applied); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
