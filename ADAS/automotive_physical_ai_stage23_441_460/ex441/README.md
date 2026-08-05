# 예제 441 — 파라미터 인벤토리

```bat
python ex441\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `print("mass",m.body_mass.sum(),"timestep",m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `mj.viewer.launch(m,d)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
