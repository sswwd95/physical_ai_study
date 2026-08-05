import csv, json, mujoco
from common.mujoco_utils import load_model_and_data, output_path
path, model, data = load_model_and_data()
commands = [
    (6.0, 6.0, 200, "forward"),
    (3.0, 7.0, 150, "left_turn"),
    (-5.0, 5.0, 120, "spin"),
    (0.0, 0.0, 80, "stop"),
]
log_path = output_path("ex120_tb3_integrated_log.csv")
rows = []
for left, right, steps, mode in commands:
    data.ctrl[:2] = [left, right]
    for step in range(steps):
        mujoco.mj_step(model, data)
        if step % 10 == 0:
            rows.append([data.time, mode, *data.qpos[:3], *data.qvel[:3], left, right])
with log_path.open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["time_s","mode","x","y","z","vx","vy","vz","left_ctrl","right_ctrl"])
    writer.writerows(rows)
summary = {
    "model_path": str(path),
    "nbody": model.nbody,
    "njnt": model.njnt,
    "nu": model.nu,
    "nsensor": model.nsensor,
    "final_time_s": float(data.time),
    "final_position": [float(v) for v in data.qpos[:3]],
    "log_rows": len(rows),
}
summary_path = output_path("ex120_summary.json")
summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(summary)
print("saved:", log_path)
print("saved:", summary_path)
