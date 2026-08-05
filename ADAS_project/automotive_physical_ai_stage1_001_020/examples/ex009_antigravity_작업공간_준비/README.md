# 예제 009 — Antigravity 작업공간 준비

## 핵심 주제
에이전트가 안전하게 작업할 프로젝트 규칙 파일을 만든다.

## 실행 절차

```bat
conda activate auto_physical_ai
cd /d <압축을_푼_폴더>
python examples\ex009_antigravity_작업공간_준비\main.py
```

## 기대 결과
오류 없이 진단 정보 또는 계산 결과가 출력됩니다. 외부 모델이 필요한 예제는 모델 경로가 없을 때 안전하게 `SKIP` 또는 안내 문구를 출력합니다.

## 초보자 체크포인트
- `python` 실행 경로가 `auto_physical_ai` 환경인지 확인합니다.
- 패키지 오류가 나면 `conda env update -f environment.yml --prune`을 실행합니다.
- 경로 문제를 줄이기 위해 압축 해제 위치에 한글과 공백을 사용하지 않는 것을 권장합니다.

## 라인별 해설
| 줄 | 코드 | 설명 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 표준/외부 모듈을 불러옵니다. |
| 2 | `` | 가독성을 위한 빈 줄입니다. |
| 3 | `root = Path.cwd()` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 4 | `rules = root / "AGENTS.md"` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 5 | `rules.write_text("""# Project rules` | 해당 기능을 실행하는 문장입니다. |
| 6 | `- Never delete files outside this project.` | 해당 기능을 실행하는 문장입니다. |
| 7 | `- Ask before running destructive commands.` | 해당 기능을 실행하는 문장입니다. |
| 8 | `- Use the auto_physical_ai conda environment.` | 해당 기능을 실행하는 문장입니다. |
| 9 | `- Run smoke tests after code changes.` | 해당 기능을 실행하는 문장입니다. |
| 10 | `- Keep MuJoCo pinned to 3.6.0.` | 해당 기능을 실행하는 문장입니다. |
| 11 | `""", encoding="utf-8")` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 12 | `print("written:", rules.resolve())` | 실행 결과나 진단 정보를 화면에 출력합니다. |
