from common.control_utils import MODEL_PATH
try:
    import mujoco
except ImportError:
    print("MuJoCo is not installed. Install environment.yml first.")
else:
    model=mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data=mujoco.MjData(model)
    data.ctrl[:2]=[6.0,6.0]
    for _ in range(200):
        mujoco.mj_step(model,data)
    print("model:",MODEL_PATH)
    print("time:",data.time)
    print("qpos:",data.qpos[:3])
