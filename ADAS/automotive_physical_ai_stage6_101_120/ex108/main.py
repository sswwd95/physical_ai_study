import mujoco
from common.mujoco_utils import load_model_and_data, name_list
_, model, _ = load_model_and_data()
names = name_list(model, mujoco.mjtObj.mjOBJ_SENSOR)
for idx, name in enumerate(names):
    print(idx, name, "dim=", int(model.sensor_dim[idx]), "adr=", int(model.sensor_adr[idx]))
