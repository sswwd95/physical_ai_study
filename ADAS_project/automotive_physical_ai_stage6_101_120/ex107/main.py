import mujoco
from common.mujoco_utils import load_model_and_data, name_list
_, model, _ = load_model_and_data()
names = name_list(model, mujoco.mjtObj.mjOBJ_ACTUATOR)
for idx, name in enumerate(names):
    print(idx, name, "ctrlrange=", model.actuator_ctrlrange[idx].tolist())
