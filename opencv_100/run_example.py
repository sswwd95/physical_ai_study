from __future__ import annotations

import argparse
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def example_path(number: int) -> Path:
    if not 1 <= number <= 100:
        raise ValueError("예제 번호는 1~100이어야 합니다.")
    stage = (number - 1) // 10 + 1
    return ROOT / f"stage{stage:02d}" / f"ex{number:03d}.py"


def main() -> None:
    parser = argparse.ArgumentParser(description="OpenCV 100제 예제 실행기")
    parser.add_argument("number", type=int, help="실행할 예제 번호(1~100)")
    args = parser.parse_args()
    path = example_path(args.number)
    print(f"실행: {path.relative_to(ROOT)}")
    runpy.run_path(str(path), run_name="__main__")


if __name__ == "__main__":
    main()
