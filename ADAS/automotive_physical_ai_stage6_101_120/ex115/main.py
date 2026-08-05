import mujoco
from common.mujoco_utils import load_model_and_data
_, model, data = load_model_and_data()
data.ctrl[:2] = [7.0, 7.0]
for _ in range(200):
    mujoco.mj_step(model, data)
for sensor_name in ["imu_accel", "imu_gyro"]:
    sid = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SENSOR, sensor_name)
    if sid >= 0:
        adr = int(model.sensor_adr[sid])
        dim = int(model.sensor_dim[sid])
        print(sensor_name, data.sensordata[adr:adr+dim].copy())
    else:
        print(sensor_name, "not found in selected model")
