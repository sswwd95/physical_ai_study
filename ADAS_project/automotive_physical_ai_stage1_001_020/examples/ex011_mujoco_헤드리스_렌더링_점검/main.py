from pathlib import Path
import mujoco

xml = Path(__file__).resolve().parents[2] / "common" / "minimal_car.xml"
model = mujoco.MjModel.from_xml_path(str(xml))
data = mujoco.MjData(model)
for _ in range(10):
    mujoco.mj_step(model, data)
print("headless simulation OK; time=", data.time)
print("GUI는 별도 예제에서 mujoco.viewer를 사용합니다.")
