from __future__ import annotations
import importlib
import platform
import sys
from pathlib import Path

REQUIRED = ["numpy", "pandas", "matplotlib", "mujoco", "pymc", "arviz"]

def main() -> int:
    print("=== 자동차 Physical AI 환경 진단 ===")
    print("Python:", sys.version.replace("\n", " "))
    print("Executable:", sys.executable)
    print("OS:", platform.platform())
    print("Project:", Path.cwd())
    failures = 0
    for name in REQUIRED:
        try:
            module = importlib.import_module(name)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name:<12} {version}")
        except Exception as exc:
            failures += 1
            print(f"[FAIL] {name:<12} {type(exc).__name__}: {exc}")
    print("RESULT:", "PASS" if failures == 0 else f"FAIL({failures})")
    return 0 if failures == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
