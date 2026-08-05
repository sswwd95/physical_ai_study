# 예제 448 — 명령 지연

```bat
python ex448\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `from common.ops import Delay` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `q=Delay(30)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | ` while v.is_running() and d.time<14:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  desired=(8,8) if d.time<5 else (-5,5) if d.time<10 else (0,0); wheels(d,*q.push(desired)); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
