from pathlib import Path
import mujoco

xml = Path(__file__).resolve().parents[2] / "common" / "minimal_car.xml"
model = mujoco.MjModel.from_xml_path(str(xml))
data = mujoco.MjData(model)
for _ in range(100):
    mujoco.mj_step(model, data)
print("time:", data.time)
print("qpos:", data.qpos.copy())
print("sensordata:", data.sensordata.copy())
