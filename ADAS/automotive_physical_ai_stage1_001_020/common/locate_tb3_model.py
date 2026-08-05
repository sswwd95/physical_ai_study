from __future__ import annotations
import os
from pathlib import Path

CANDIDATE_FILES = ("scene.xml", "robot.xml", "model.xml", "tb3.xml")

def candidate_roots() -> list[Path]:
    roots = []
    env = os.getenv("ROBOTIS_MUJOCO_MENAGERIE")
    if env:
        roots.append(Path(env))
    roots.extend([
        Path.cwd() / "robotis_mujoco_menagerie",
        Path.cwd().parent / "robotis_mujoco_menagerie",
        Path.home() / "robotis_mujoco_menagerie",
        Path.home() / "Documents" / "robotis_mujoco_menagerie",
    ])
    return roots

def find_tb3_model() -> Path | None:
    for root in candidate_roots():
        tb3 = root / "robotis_tb3"
        if not tb3.exists():
            continue
        for name in CANDIDATE_FILES:
            direct = tb3 / name
            if direct.exists():
                return direct.resolve()
        for file in tb3.rglob("*.xml"):
            if "scene" in file.name.lower() or "burger" in str(file).lower():
                return file.resolve()
    return None

def main() -> int:
    model = find_tb3_model()
    if model:
        print("[OK] TurtleBot3 모델:", model)
        return 0
    print("[WARN] robotis_tb3 모델을 찾지 못했습니다.")
    print("ROBOTIS_MUJOCO_MENAGERIE 환경변수에 저장소 루트를 지정하세요.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
