"""
반도체 Physical AI 하네스 엔지니어링 실습 006~010
Windows 10 / Anaconda / PyMC / Antigravity
"""

from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = PROJECT_ROOT / "examples"

# 1. 실행할 작업을 순서대로 정의한다.
PIPELINE = [
    "example_006_yaml_config_loader.py",
    "example_007_structured_logging.py",
]

# 2. 각 작업을 현재 Python 인터프리터로 실행한다.
for script_name in PIPELINE:
    script_path = EXAMPLES_DIR / script_name
    print(f"\n[실행 시작] {script_name}")

    completed = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    # 3. 표준 출력을 그대로 보여준다.
    if completed.stdout:
        print(completed.stdout)

    # 4. 오류 출력이 있으면 함께 보여준다.
    if completed.stderr:
        print("[표준 오류]")
        print(completed.stderr)

    # 5. 하나라도 실패하면 즉시 파이프라인을 중단한다.
    if completed.returncode != 0:
        raise RuntimeError(
            f"{script_name} 실행 실패, 종료 코드={completed.returncode}"
        )

    print(f"[실행 성공] {script_name}")

print("\n[전체 성공] 실행 하네스가 모든 단계를 완료했습니다.")
