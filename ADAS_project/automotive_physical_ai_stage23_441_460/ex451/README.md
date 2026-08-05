# 예제 451 — 영점 캘리브레이션

```bat
python ex451\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `import numpy as np` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `bias=np.array([.08,-.04,.02]); samples=[]` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | ` while v.is_running() and d.time<10:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  mj.mj_step(m,d); measured=d.sensordata[7:10]+bias` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `  if d.time<3:samples.append(measured.copy())` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 10 | `  est=np.mean(samples,axis=0) if samples else np.zeros(3); print(measured-est); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
