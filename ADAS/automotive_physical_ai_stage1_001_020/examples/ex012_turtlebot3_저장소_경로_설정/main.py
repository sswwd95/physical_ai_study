import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "common"))
from locate_tb3_model import find_tb3_model

model = find_tb3_model()
print("model:", model)
if model is None:
    print("ROBOTIS_MUJOCO_MENAGERIE를 저장소 루트로 지정하세요.")
