from common.path_tracking import MODEL_PATH
try:
    import mujoco
except ImportError:
    print("MuJoCo is not installed. Install environment.yml first.")
else:
    model=mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data=mujoco.MjData(model)
    data.ctrl[:2]=[5.0,7.0]
    for _ in range(200):
        mujoco.mj_step(model,data)
    print("model:",MODEL_PATH)
    print("time:",data.time)
    print("base qpos:",data.qpos[:7])
