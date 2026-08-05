# 예제 447 — 엔코더 고착

```bat
python ex447\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `frozen=None` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | ` while v.is_running() and d.time<10:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | `  wheels(d,6,9); mj.mj_step(m,d); value=float(d.sensordata[-2])` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  if d.time>5 and frozen is None:frozen=value` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `  print("used",frozen if frozen is not None else value); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
