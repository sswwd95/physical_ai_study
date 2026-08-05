from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
FALLBACK_MODEL = ROOT / "models" / "tb3_burger_training.xml"
OUTPUTS = ROOT / "outputs"

def output_path(name: str) -> Path:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def find_tb3_xml() -> Path:
    """ROBOTIS 저장소가 있으면 우선 사용하고, 없으면 교육용 모델을 반환한다."""
    candidates = []
    env_root = os.environ.get("ROBOTIS_MUJOCO_MENAGERIE")
    if env_root:
        candidates.append(Path(env_root))
    candidates.extend([
        ROOT.parent / "robotis_mujoco_menagerie",
        Path.cwd() / "robotis_mujoco_menagerie",
        Path.home() / "robotis_mujoco_menagerie",
    ])
    for base in candidates:
        if not base.exists():
            continue
        xmls = sorted(base.rglob("*.xml"))
        preferred = [p for p in xmls if "robotis_tb3" in str(p).lower() or "burger" in p.name.lower()]
        if preferred:
            return preferred[0]
    return FALLBACK_MODEL

def load_model_and_data():
    import mujoco
    path = find_tb3_xml()
    model = mujoco.MjModel.from_xml_path(str(path))
    data = mujoco.MjData(model)
    return path, model, data

def name_list(model, object_type):
    import mujoco
    count_map = {
        mujoco.mjtObj.mjOBJ_BODY: model.nbody,
        mujoco.mjtObj.mjOBJ_JOINT: model.njnt,
        mujoco.mjtObj.mjOBJ_ACTUATOR: model.nu,
        mujoco.mjtObj.mjOBJ_SENSOR: model.nsensor,
        mujoco.mjtObj.mjOBJ_GEOM: model.ngeom,
        mujoco.mjtObj.mjOBJ_SITE: model.nsite,
    }
    names = []
    for idx in range(count_map[object_type]):
        name = mujoco.mj_id2name(model, object_type, idx)
        names.append(name if name is not None else f"<unnamed_{idx}>")
    return names
