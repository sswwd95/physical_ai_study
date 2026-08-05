# 예제 415 — 일시정지 키

## 실행
```bat
python ex415\main.py
```

## 핵심
`launch_passive()`에서는 사용자 코드가 `mj_step()`으로 물리를 진행하고 `sync()`로 화면과 입력을 동기화합니다. 공유 상태 변경은 `lock()` 안에서 수행합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 2 | `from common.viewer_utils import load,wheels` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 3 | `mj,m,d=load(); paused=False` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 4 | `def key(k):` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 5 | ` global paused` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 6 | ` if k==32: paused=not paused` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 7 | `with mj.viewer.launch_passive(m,d,key_callback=key) as v:` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 8 | ` while v.is_running():` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 9 | `  if not paused: wheels(d,6,7); mj.mj_step(m,d)` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 10 | `  v.sync(); time.sleep(m.opt.timestep)` | Viewer 또는 물리 상태를 설정·실행합니다. |
