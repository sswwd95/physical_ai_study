from pathlib import Path
import json
import math
import os
import shutil

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
EXTENSIONS = ROOT / "extensions"


def repo() -> Path:
    candidates = []

    env_path = os.environ.get("ROBOTIS_MENAGERIE_ROOT")
    if env_path:
        candidates.append(Path(env_path))

    candidates.extend(
        [
            ROOT / "vendor" / "robotis_mujoco_menagerie",
            Path("C:/work/robotis_mujoco_menagerie"),
            Path.home() / "robotis_mujoco_menagerie",
        ]
    )

    for candidate in candidates:
        model_path = (
            candidate
            / "robotis_tb3"
            / "turtlebot3_burger.xml"
        )

        if model_path.exists():
            return candidate.resolve()

    raise FileNotFoundError(
        "ROBOTIS MuJoCo Menagerie를 찾을 수 없습니다.\n"
        "vendor/robotis_mujoco_menagerie 폴더를 확인하세요."
    )


def burger_directory() -> Path:
    return repo() / "robotis_tb3"


def burger_model() -> Path:
    return burger_directory() / "turtlebot3_burger.xml"


def find_assets_directory() -> Path:
    tb3_directory = burger_directory()

    candidates = [
        tb3_directory / "assets",
        tb3_directory / "meshes",
        tb3_directory,
    ]

    for candidate in candidates:
        if (candidate / "burger_base.stl").exists():
            return candidate.resolve()

    matches = list(tb3_directory.rglob("burger_base.stl"))

    if matches:
        return matches[0].parent.resolve()

    raise FileNotFoundError(
        "burger_base.stl 파일을 찾을 수 없습니다.\n"
        "ROBOTIS 저장소가 불완전하게 복제됐습니다."
    )


def prepare_assets() -> Path:
    EXTENSIONS.mkdir(parents=True, exist_ok=True)

    source_assets = find_assets_directory()
    target_assets = EXTENSIONS / "assets"

    if target_assets.exists() or target_assets.is_symlink():
        if target_assets.is_symlink():
            target_assets.unlink()
        elif target_assets.resolve() != source_assets.resolve():
            shutil.rmtree(target_assets)

    if not target_assets.exists():
        try:
            target_assets.symlink_to(
                source_assets,
                target_is_directory=True,
            )
        except OSError:
            shutil.copytree(
                source_assets,
                target_assets,
                dirs_exist_ok=True,
            )

    return target_assets


def scene(name: str, world: str = "") -> Path:
    EXTENSIONS.mkdir(parents=True, exist_ok=True)
    prepare_assets()

    scene_path = EXTENSIONS / name
    model_path = burger_model()

    scene_path.write_text(
        f"""<mujoco model="{name}">
 <compiler angle="radian" meshdir="assets"/>
 <include file="{model_path.as_posix()}"/>

 <statistic center="1 0 .4" extent="5"/>

 <visual>
  <headlight
   diffuse=".7 .7 .7"
   ambient=".25 .25 .25"
  />
  <global
   azimuth="120"
   elevation="-22"
  />
 </visual>

 <asset>
  <texture
   type="2d"
   name="road"
   builtin="checker"
   rgb1=".12 .12 .12"
   rgb2=".18 .18 .18"
   width="512"
   height="512"
  />
  <material
   name="roadmat"
   texture="road"
   texrepeat="16 16"
  />
 </asset>

 <worldbody>
  <light
   pos="0 0 5"
   dir="0 0 -1"
  />
  <geom
   type="plane"
   size="20 10 .05"
   material="roadmat"
  />
  {world}
 </worldbody>
</mujoco>
""",
        encoding="utf-8",
    )

    return scene_path


def load(path: Path):
    import mujoco
    import mujoco.viewer

    model = mujoco.MjModel.from_xml_path(str(path))
    data = mujoco.MjData(model)

    return mujoco, model, data


def wheels(data, left: float, right: float) -> None:
    data.ctrl[0] = float(
        np.clip(left, -6.67, 6.67)
    )
    data.ctrl[1] = float(
        np.clip(right, -6.67, 6.67)
    )


def pose(data) -> tuple[float, float, float]:
    qw, qx, qy, qz = data.qpos[3:7]

    yaw = math.atan2(
        2 * (qw * qz + qx * qy),
        1 - 2 * (qy * qy + qz * qz),
    )

    return (
        float(data.qpos[0]),
        float(data.qpos[1]),
        float(yaw),
    )


def out(name: str) -> Path:
    OUTPUTS.mkdir(
        parents=True,
        exist_ok=True,
    )

    return OUTPUTS / name


def save_json(data, name: str) -> Path:
    output_path = out(name)

    output_path.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    return output_path