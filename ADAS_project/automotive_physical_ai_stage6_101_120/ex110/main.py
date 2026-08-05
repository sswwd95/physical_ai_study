import mujoco
from common.mujoco_utils import load_model_and_data
_, model, data = load_model_and_data()
for _ in range(100):
    mujoco.mj_step(model, data)
print("time:", round(data.time, 3))
print("qpos:", data.qpos.copy())
