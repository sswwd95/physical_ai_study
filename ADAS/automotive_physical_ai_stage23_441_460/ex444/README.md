# 예제 444 — 조명·외관 랜덤화

```bat
python ex444\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `import numpy as np` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `g=mj.mj_name2id(m,mj.mjtObj.mjOBJ_GEOM,"chassis"); rng=np.random.default_rng(7)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | ` while v.is_running() and d.time<12:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  if int(d.time)%3==0 and d.time-int(d.time)<.02:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `   with v.lock(): m.geom_rgba[g]=[rng.random(),rng.random(),rng.random(),1]` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 10 | `  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
