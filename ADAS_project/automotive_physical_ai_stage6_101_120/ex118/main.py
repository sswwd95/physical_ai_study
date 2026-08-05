import csv, mujoco
from common.mujoco_utils import load_model_and_data, output_path
_, model, data = load_model_and_data()
path = output_path("ex118_simulation_log.csv")
with path.open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["time_s","x","y","z","left_ctrl","right_ctrl"])
    data.ctrl[:2] = [6.0, 6.0]
    for step in range(500):
        mujoco.mj_step(model, data)
        if step % 10 == 0:
            writer.writerow([data.time, *data.qpos[:3], *data.ctrl[:2]])
print("saved:", path)
