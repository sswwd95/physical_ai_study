import mujoco
from common.mujoco_utils import load_model_and_data
_, model, data = load_model_and_data()
if model.nu < 2:
    raise RuntimeError("두 개 이상의 바퀴 액추에이터가 필요합니다.")
data.ctrl[0] = -6.0
data.ctrl[1] = 6.0
for _ in range(300):
    mujoco.mj_step(model, data)
print("base quaternion:", data.qpos[3:7].copy())
print("controls:", data.ctrl.copy())
