import mujoco
from common.mujoco_utils import load_model_and_data, name_list
_, model, _ = load_model_and_data()
names = name_list(model, mujoco.mjtObj.mjOBJ_JOINT)
for idx, name in enumerate(names):
    print(idx, name, "type=", int(model.jnt_type[idx]), "qposadr=", int(model.jnt_qposadr[idx]))
