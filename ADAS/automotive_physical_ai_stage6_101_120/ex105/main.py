import mujoco
from common.mujoco_utils import load_model_and_data, name_list
_, model, _ = load_model_and_data()
for idx, name in enumerate(name_list(model, mujoco.mjtObj.mjOBJ_BODY)):
    print(idx, name)
