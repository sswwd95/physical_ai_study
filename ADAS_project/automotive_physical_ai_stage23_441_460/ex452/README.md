# 예제 452 — 체크포인트 복원

```bat
python ex452\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `checkpoint=None; restored=False` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | ` while v.is_running() and d.time<14:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | `  wheels(d,7,8); mj.mj_step(m,d)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  if d.time>4 and checkpoint is None: checkpoint=(d.qpos.copy(),d.qvel.copy(),d.time)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `  if d.time>9 and not restored:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 10 | `   with v.lock(): d.qpos[:]=checkpoint[0]; d.qvel[:]=checkpoint[1]; d.time=checkpoint[2]; mj.mj_forward(m,d)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 11 | `   restored=True` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 12 | `  v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
