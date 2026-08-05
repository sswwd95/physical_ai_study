# 예제 401 — Viewer 기본 실행

## 실행
```bat
python ex401\main.py
```

## 핵심
`launch_passive()`에서는 사용자 코드가 `mj_step()`으로 물리를 진행하고 `sync()`로 화면과 입력을 동기화합니다. 공유 상태 변경은 `lock()` 안에서 수행합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `from common.viewer_utils import load` | Viewer 또는 물리 상태를 설정·실행합니다. |
| 2 | `mj,m,d=load(); mj.viewer.launch(m,d)` | Viewer 또는 물리 상태를 설정·실행합니다. |
