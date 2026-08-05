import mujoco
from common.mujoco_utils import load_model_and_data
_, model, data = load_model_and_data()
data.ctrl[0] = 4.0
data.ctrl[1] = 8.0
for _ in range(400):
    mujoco.mj_step(model, data)
print("base position:", data.qpos[:3].copy())
print("base quaternion:", data.qpos[3:7].copy())
