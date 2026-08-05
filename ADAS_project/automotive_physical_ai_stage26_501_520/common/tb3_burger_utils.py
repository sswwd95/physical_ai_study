from pathlib import Path
import os
import time
import math
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
REPO_NAME = "robotis_mujoco_menagerie"
TB3_DIR_NAME = "robotis_tb3"
SCENE_NAME = "scene_turtlebot3_burger.xml"
MODEL_NAME = "turtlebot3_burger.xml"

def candidate_repo_roots():
    candidates = []
    env_root = os.environ.get("ROBOTIS_MENAGERIE_ROOT")
    if env_root:
        candidates.append(Path(env_root))
    candidates.extend([
        ROOT / "vendor" / REPO_NAME,
        ROOT.parent / REPO_NAME,
        Path.cwd() / REPO_NAME,
        Path.home() / REPO_NAME,
        Path("C:/work") / REPO_NAME,
    ])
    return candidates

def find_repo_root():
    for candidate in candidate_repo_roots():
        scene = candidate / TB3_DIR_NAME / SCENE_NAME
        if scene.exists():
            return candidate.resolve()
    checked = "\n".join(str(p) for p in candidate_repo_roots())
    raise FileNotFoundError(
        "공식 robotis_mujoco_menagerie를 찾지 못했습니다.\n"
        "scripts/01_clone_robotis_menagerie.bat를 실행하거나 "
        "ROBOTIS_MENAGERIE_ROOT 환경변수를 설정하세요.\n"
        f"확인한 경로:\n{checked}"
    )

def tb3_dir():
    return find_repo_root() / TB3_DIR_NAME

def scene_path():
    return tb3_dir() / SCENE_NAME

def model_path():
    return tb3_dir() / MODEL_NAME

def output_path(name):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def load_tb3():
    import mujoco
    import mujoco.viewer
    model = mujoco.MjModel.from_xml_path(str(scene_path()))
    data = mujoco.MjData(model)
    ids = {
        "base_body": mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "base"),
        "base_joint": mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "base_joint"),
        "wheel_left_joint": mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "wheel_left"),
        "wheel_right_joint": mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "wheel_right"),
        "wheel_left_actuator": mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_ACTUATOR, "wheel_left"),
        "wheel_right_actuator": mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_ACTUATOR, "wheel_right"),
    }
    return mujoco, model, data, ids

def set_wheels(data, left, right):
    data.ctrl[0] = float(np.clip(left, -6.67, 6.67))
    data.ctrl[1] = float(np.clip(right, -6.67, 6.67))

def yaw_from_quat(q):
    qw, qx, qy, qz = q
    return math.atan2(2*(qw*qz + qx*qy), 1 - 2*(qy*qy + qz*qz))

def base_pose(data):
    return {
        "x_m": float(data.qpos[0]),
        "y_m": float(data.qpos[1]),
        "z_m": float(data.qpos[2]),
        "yaw_rad": float(yaw_from_quat(data.qpos[3:7])),
    }

def realtime_loop(mujoco, model, data, viewer, duration_s, control=None, logger=None):
    start = time.time()
    while viewer.is_running() and time.time() - start < duration_s:
        tick = time.time()
        if control:
            control(model, data)
        mujoco.mj_step(model, data)
        if logger:
            logger(model, data)
        viewer.sync()
        delay = model.opt.timestep - (time.time() - tick)
        if delay > 0:
            time.sleep(delay)

def make_extension_scene(name, extra_worldbody="", extra_sensor="", extra_actuator=""):
    """Create a temporary MJCF scene that includes the official Burger model."""
    path = ROOT / "extensions" / name
    include_path = model_path().as_posix()
    xml = f"""<mujoco model="{name}">
  <include file="{include_path}"/>
  <statistic center="0.3 0 0.4" extent="3"/>
  <visual>
    <headlight diffuse="0.6 0.6 0.6" ambient="0.3 0.3 0.3" specular="0 0 0"/>
    <global azimuth="120" elevation="-20"/>
  </visual>
  <asset>
    <texture type="skybox" builtin="gradient" rgb1="0.3 0.5 0.7" rgb2="0 0 0" width="512" height="3072"/>
    <texture type="2d" name="groundplane_ext" builtin="checker" mark="edge"
             rgb1="0.2 0.3 0.4" rgb2="0.1 0.2 0.3" markrgb="0.8 0.8 0.8"
             width="300" height="300"/>
    <material name="groundplane_ext" texture="groundplane_ext" texuniform="true"
              texrepeat="8 8" reflectance="0.2"/>
  </asset>
  <worldbody>
    <light pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor_ext" size="0 0 0.05" type="plane" material="groundplane_ext"/>
    {extra_worldbody}
  </worldbody>
  <sensor>{extra_sensor}</sensor>
  <actuator>{extra_actuator}</actuator>
</mujoco>"""
    path.write_text(xml, encoding="utf-8")
    return path

def save_json(obj, name):
    p = output_path(name)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    return p
