import mujoco
from common.mujoco_utils import load_model_and_data
_, model, data = load_model_and_data()
data.ctrl[:2] = [5.0, 7.0]
for _ in range(100):
    mujoco.mj_step(model, data)
for sid in range(model.nsensor):
    adr = int(model.sensor_adr[sid])
    dim = int(model.sensor_dim[sid])
    name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_SENSOR, sid)
    print(name, data.sensordata[adr:adr+dim].copy())
