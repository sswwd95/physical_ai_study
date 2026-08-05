import mujoco
from common.mujoco_utils import load_model_and_data

def run_command(model, data, left, right, steps):
    data.ctrl[:2] = [left, right]
    for _ in range(steps):
        mujoco.mj_step(model, data)

_, model, data = load_model_and_data()
run_command(model, data, 6.0, 6.0, 200)
run_command(model, data, -5.0, 5.0, 150)
run_command(model, data, 6.0, 6.0, 200)
print("final time:", data.time)
print("final position:", data.qpos[:3].copy())
