import sys
from pathlib import Path
import mujoco

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "common"))
from locate_tb3_model import find_tb3_model

path = find_tb3_model()
if path is None:
    print("SKIP: robotis_tb3 모델 경로 미설정")
else:
    model = mujoco.MjModel.from_xml_path(str(path))
    print("loaded:", path)
    print("nbody/njnt/nu/nsensor:", model.nbody, model.njnt, model.nu, model.nsensor)
