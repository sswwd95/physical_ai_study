import mujoco
from common.mujoco_utils import load_model_and_data
_, model, data = load_model_and_data()
mujoco.mj_forward(model, data)
print("qpos:", data.qpos.copy())
print("qvel:", data.qvel.copy())
print("sensordata:", data.sensordata.copy())
