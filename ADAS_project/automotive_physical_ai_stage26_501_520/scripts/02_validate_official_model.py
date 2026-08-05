from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from common.tb3_burger_utils import find_repo_root,tb3_dir,scene_path,model_path
print("repository:",find_repo_root())
print("tb3:",tb3_dir())
print("scene:",scene_path())
print("model:",model_path())
assert scene_path().exists()
assert model_path().exists()
try:
    import mujoco
    model=mujoco.MjModel.from_xml_path(str(scene_path()))
    print("loaded model:",model.nbody,"bodies,",model.nu,"actuators")
except ImportError:
    print("MuJoCo is not installed yet. File validation passed.")
