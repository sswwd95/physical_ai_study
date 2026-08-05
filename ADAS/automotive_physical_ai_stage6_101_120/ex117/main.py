import numpy as np, mujoco
from common.mujoco_utils import load_model_and_data
_, model, data = load_model_and_data()
requested = np.array([30.0, -30.0])
low = model.actuator_ctrlrange[:2, 0]
high = model.actuator_ctrlrange[:2, 1]
safe = np.clip(requested, low, high)
data.ctrl[:2] = safe
for _ in range(100):
    mujoco.mj_step(model, data)
print("requested:", requested)
print("applied:", safe)
