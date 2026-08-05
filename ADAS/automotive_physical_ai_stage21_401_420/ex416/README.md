# 예제 416 — 키보드 주행

## 실행
```bat
python ex416\main.py
```

## 핵심
`launch_passive()`에서는 사용자 코드가 `mj_step()`으로 물리를 진행하고 `sync()`로 화면과 입력을 동기화합니다. 공유 상태 변경은 `lock()` 안에서 수행합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 2 | `from common.viewer_utils import load,wheels` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 3 | `mj,m,d=load(); cmd=[0,0]` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 4 | `def key(k):` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 5 | ` if k in (87,119): cmd[:]=[7,7]` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 6 | ` elif k in (65,97): cmd[:]=[-4,4]` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 7 | ` elif k in (68,100): cmd[:]=[4,-4]` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 8 | ` elif k in (83,115): cmd[:]=[0,0]` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 9 | `with mj.viewer.launch_passive(m,d,key_callback=key) as v:` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 10 | ` while v.is_running(): wheels(d,*cmd); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | Viewer 또는 물리 상태를 설정·실행합니다. |
