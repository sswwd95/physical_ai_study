from common.safety_utils import MODEL_PATH
try:
    import mujoco
except ImportError:
    print("MuJoCo is not installed. Install environment.yml first.")
else:
    model=mujoco.MjModel.from_xml_path(str(MODEL_PATH))
    data=mujoco.MjData(model)
    data.ctrl[:2]=[8.0,8.0]
    for _ in range(100): mujoco.mj_step(model,data)
    data.ctrl[:2]=[0.0,0.0]
    for _ in range(100): mujoco.mj_step(model,data)
    print("time:",data.time)
    print("control:",data.ctrl[:2])
