# 예제 458 — 파라미터 스윕

```bat
python ex458\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `speeds=[4,7,10]; idx=0` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | ` while v.is_running() and d.time<15:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | `  idx=min(int(d.time//5),2); wheels(d,speeds[idx],speeds[idx]); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
