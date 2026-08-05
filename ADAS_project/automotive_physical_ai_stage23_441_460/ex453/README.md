# 예제 453 — 재현 리플레이

```bat
python ex453\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `cmds=[(6,6)]*250+[(3,8)]*250+[(0,0)]*150` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | ` for c in cmds:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | `  if not v.is_running():break` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  wheels(d,*c); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `print(d.qpos.copy())` | 디지털 트윈 운영 검증 코드를 실행합니다. |
