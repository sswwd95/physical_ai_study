"""
TurtleBot3 Burger MuJoCo 예제에서 공통으로 사용하는 함수 모음입니다.

전체 흐름
1. 프로젝트 위치를 확인합니다.
2. robotis_mujoco_menagerie 저장소를 찾습니다.
3. TurtleBot3 XML을 MuJoCo로 불러옵니다.
4. 바퀴 속도를 설정합니다.
5. 로봇의 위치와 방향을 계산합니다.
6. 시뮬레이션을 실제 시간과 비슷한 속도로 반복 실행합니다.
7. 필요한 추가 장면 XML을 만듭니다.
8. 결과를 JSON 파일로 저장합니다.
"""

# 파일과 폴더 경로를 운영체제에 맞게 안전하게 다루기 위해 사용합니다.
from pathlib import Path

# 환경 변수를 읽기 위해 사용합니다.
import os

# 현재 시각 확인과 잠시 기다리는 기능에 사용합니다.
import time

# 각도 계산에 필요한 atan2 함수를 사용하기 위해 불러옵니다.
import math

# 파이썬 데이터를 JSON 문자열과 파일로 바꾸기 위해 사용합니다.
import json

# 숫자 계산과 바퀴 속도 제한에 사용합니다.
import numpy as np

# 표 형태 데이터를 다루기 위해 불러옵니다.
# 현재 파일에서는 직접 사용하지 않지만 다른 예제에서 사용할 수 있습니다.
import pandas as pd


# ============================================================
# 1. 프로젝트 경로와 파일 이름 설정
# ============================================================

# __file__은 현재 실행 중인 이 파이썬 파일의 경로입니다.
#
# 예:
# C:/work/project/common/adas_tb3_utils.py
#
# Path(__file__).resolve() : 위 경로를 절대 경로로 바꿉니다.
# parents[0]               : common 폴더입니다.
# parents[1]               : project 폴더입니다.
#
# 따라서 ROOT에는 프로젝트 최상위 폴더 경로가 저장됩니다.
ROOT = Path(__file__).resolve().parents[1]

# 실행 결과를 저장할 outputs 폴더 경로입니다.
OUTPUTS = ROOT / "outputs"

# ROBOTIS에서 제공하는 MuJoCo 모델 저장소 폴더 이름입니다.
REPO_NAME = "robotis_mujoco_menagerie"

# 저장소 안에서 TurtleBot3 모델이 들어 있는 폴더 이름입니다.
TB3_DIR_NAME = "robotis_tb3"

# 바닥과 조명까지 포함된 기본 시뮬레이션 장면 XML 이름입니다.
SCENE_NAME = "scene_turtlebot3_burger.xml"

# TurtleBot3 Burger 로봇 자체를 정의한 XML 이름입니다.
MODEL_NAME = "turtlebot3_burger.xml"


# ============================================================
# 2. ROBOTIS 모델 저장소 찾기
# ============================================================

def candidate_repo_roots() -> list[Path]:
    """
    robotis_mujoco_menagerie 저장소가 있을 가능성이 있는 경로를 모읍니다.

    이 함수는 실제 저장소가 있는지 확정하지 않습니다.
    확인해 볼 후보 경로 목록만 만듭니다.
    """

    # 후보 경로를 순서대로 담을 빈 리스트를 만듭니다.
    candidates: list[Path] = []

    # Windows 환경 변수 ROBOTIS_MENAGERIE_ROOT의 값을 읽습니다.
    #
    # 사용 예:
    # set ROBOTIS_MENAGERIE_ROOT=C:\\work\\robotis_mujoco_menagerie
    #
    # 환경 변수가 없으면 env_root에는 None이 들어갑니다.
    env_root = os.environ.get("ROBOTIS_MENAGERIE_ROOT")

    # 환경 변수가 설정되어 있을 때만 후보 목록에 추가합니다.
    # 사용자가 직접 지정한 경로이므로 가장 먼저 확인합니다.
    if env_root:
        candidates.append(Path(env_root))

    # 자주 사용하는 기본 경로들을 후보 목록 뒤에 추가합니다.
    candidates.extend([
        # 현재 프로젝트 안의 vendor 폴더입니다.
        ROOT / "vendor" / REPO_NAME,

        # 현재 프로젝트의 바로 위 폴더입니다.
        ROOT.parent / REPO_NAME,

        # 명령 프롬프트의 현재 작업 폴더입니다.
        Path.cwd() / REPO_NAME,

        # 현재 Windows 사용자의 홈 폴더입니다.
        Path.home() / REPO_NAME,

        # 사용자가 자주 사용하는 C:/work 폴더입니다.
        Path("C:/work") / REPO_NAME,
    ])

    # 완성된 후보 경로 목록을 돌려줍니다.
    return candidates


def find_repo_root() -> Path:
    """
    후보 경로를 차례대로 확인해 실제 ROBOTIS 저장소를 찾습니다.

    robotis_tb3/scene_turtlebot3_burger.xml 파일이 있으면
    정상 저장소로 판단합니다.
    """

    # candidate_repo_roots()가 만든 후보 경로를 하나씩 확인합니다.
    for candidate in candidate_repo_roots():

        # 현재 후보 경로 안의 기본 Scene XML 전체 경로를 만듭니다.
        scene = candidate / TB3_DIR_NAME / SCENE_NAME

        # 해당 XML 파일이 실제로 있으면 저장소를 찾은 것입니다.
        if scene.exists():

            # resolve()로 절대 경로를 만들어 반환합니다.
            return candidate.resolve()

    # 여기까지 왔다면 어느 후보에서도 저장소를 찾지 못한 것입니다.
    # 확인한 모든 경로를 줄바꿈으로 연결합니다.
    checked = "\n".join(str(path) for path in candidate_repo_roots())

    # 문제 원인과 확인한 경로를 포함한 오류를 발생시킵니다.
    raise FileNotFoundError(
        "공식 robotis_mujoco_menagerie를 찾지 못했습니다.\n"
        "scripts/01_clone_robotis_menagerie.bat를 실행하거나 "
        "ROBOTIS_MENAGERIE_ROOT 환경변수를 설정하세요.\n"
        f"확인한 경로:\n{checked}"
    )


def tb3_dir() -> Path:
    """ROBOTIS 저장소 안의 robotis_tb3 폴더 경로를 반환합니다."""

    # 저장소 최상위 경로 뒤에 robotis_tb3 폴더 이름을 붙입니다.
    return find_repo_root() / TB3_DIR_NAME


def scene_path() -> Path:
    """기본 TurtleBot3 시뮬레이션 장면 XML 경로를 반환합니다."""

    # robotis_tb3 폴더 뒤에 Scene XML 파일 이름을 붙입니다.
    return tb3_dir() / SCENE_NAME


def model_path() -> Path:
    """TurtleBot3 Burger 로봇 모델 XML 경로를 반환합니다."""

    # robotis_tb3 폴더 뒤에 로봇 모델 XML 이름을 붙입니다.
    return tb3_dir() / MODEL_NAME


# ============================================================
# 3. 결과 파일 저장 경로 만들기
# ============================================================

def output_path(name: str) -> Path:
    """
    outputs 폴더를 준비하고 그 안의 결과 파일 경로를 반환합니다.

    예:
    output_path("result.json")
    -> 프로젝트폴더/outputs/result.json
    """

    # outputs 폴더가 없으면 새로 만듭니다.
    # parents=True  : 상위 폴더도 필요하면 함께 만듭니다.
    # exist_ok=True : 이미 폴더가 있어도 오류를 내지 않습니다.
    OUTPUTS.mkdir(parents=True, exist_ok=True)

    # outputs 폴더 경로와 파일 이름을 합쳐 반환합니다.
    return OUTPUTS / name


# ============================================================
# 4. TurtleBot3 MuJoCo 모델 불러오기
# ============================================================

def load_tb3():
    """
    기본 TurtleBot3 장면 XML을 읽어 MuJoCo 시뮬레이션을 준비합니다.

    반환값
    - mujoco : MuJoCo 파이썬 모듈
    - model  : 로봇 구조와 물리 설정을 가진 MjModel
    - data   : 위치, 속도, 제어값 등 현재 상태를 가진 MjData
    - ids    : 주요 몸체, 관절, 액추에이터 ID 모음
    """

    # MuJoCo의 모델 생성 및 물리 계산 기능을 불러옵니다.
    import mujoco

    # MuJoCo 화면 창을 열기 위한 viewer 모듈을 불러옵니다.
    import mujoco.viewer

    # scene_path()가 반환한 XML을 읽어 MuJoCo 모델을 만듭니다.
    # str()은 Path 경로를 일반 문자열로 바꿉니다.
    model = mujoco.MjModel.from_xml_path(str(scene_path()))

    # model을 기준으로 현재 시뮬레이션 상태를 저장할 data를 만듭니다.
    # data에는 위치, 속도, 제어값, 시뮬레이션 시간 등이 들어갑니다.
    data = mujoco.MjData(model)

    # XML 안의 이름을 MuJoCo 내부 번호(ID)로 바꿉니다.
    # MuJoCo 계산에서는 문자열 이름보다 숫자 ID를 자주 사용합니다.
    ids = {
        # 이름이 base인 로봇 몸체의 ID입니다.
        "base_body": mujoco.mj_name2id(
            model, mujoco.mjtObj.mjOBJ_BODY, "base"
        ),

        # 이름이 base_joint인 기본 관절의 ID입니다.
        "base_joint": mujoco.mj_name2id(
            model, mujoco.mjtObj.mjOBJ_JOINT, "base_joint"
        ),

        # 왼쪽 바퀴 관절의 ID입니다.
        "wheel_left_joint": mujoco.mj_name2id(
            model, mujoco.mjtObj.mjOBJ_JOINT, "wheel_left"
        ),

        # 오른쪽 바퀴 관절의 ID입니다.
        "wheel_right_joint": mujoco.mj_name2id(
            model, mujoco.mjtObj.mjOBJ_JOINT, "wheel_right"
        ),

        # 왼쪽 바퀴를 움직이는 액추에이터의 ID입니다.
        "wheel_left_actuator": mujoco.mj_name2id(
            model, mujoco.mjtObj.mjOBJ_ACTUATOR, "wheel_left"
        ),

        # 오른쪽 바퀴를 움직이는 액추에이터의 ID입니다.
        "wheel_right_actuator": mujoco.mj_name2id(
            model, mujoco.mjtObj.mjOBJ_ACTUATOR, "wheel_right"
        ),
    }

    # 준비한 네 가지 값을 호출한 코드로 돌려줍니다.
    return mujoco, model, data, ids


# ============================================================
# 5. 바퀴 속도 제어
# ============================================================

def set_wheels(data, left: float, right: float) -> None:
    """
    왼쪽 바퀴와 오른쪽 바퀴 속도를 설정합니다.

    두 값이 같고 양수  : 앞으로 직진
    두 값이 같고 음수  : 뒤로 직진
    왼쪽이 작고 오른쪽이 큼 : 왼쪽으로 회전
    왼쪽이 크고 오른쪽이 작음 : 오른쪽으로 회전
    """

    # np.clip은 값을 -6.67~6.67 범위 안으로 제한합니다.
    # data.ctrl[0]은 왼쪽 바퀴 제어값입니다.
    data.ctrl[0] = float(np.clip(left, -6.67, 6.67))

    # data.ctrl[1]은 오른쪽 바퀴 제어값입니다.
    data.ctrl[1] = float(np.clip(right, -6.67, 6.67))


# ============================================================
# 6. 로봇 방향과 위치 계산
# ============================================================

def yaw_from_quat(q) -> float:
    """
    쿼터니언 회전값을 Yaw 각도로 바꿉니다.

    Yaw는 로봇을 위에서 봤을 때 왼쪽 또는 오른쪽으로
    얼마나 돌아갔는지를 나타내는 각도입니다.

    반환 단위는 라디안(rad)입니다.
    """

    # q에 들어 있는 네 개의 회전값을 각각 변수에 나눠 담습니다.
    qw, qx, qy, qz = q

    # 쿼터니언을 Yaw 각도로 바꾸는 공식입니다.
    return math.atan2(
        2 * (qw * qz + qx * qy),
        1 - 2 * (qy * qy + qz * qz),
    )


def base_pose(data) -> dict[str, float]:
    """
    로봇 몸체의 현재 위치와 방향을 딕셔너리로 반환합니다.

    반환값
    - x_m     : X축 위치(m)
    - y_m     : Y축 위치(m)
    - z_m     : 높이(m)
    - yaw_rad : 수평 회전각(rad)
    """

    # data.qpos의 앞부분은 일반적으로 다음 뜻입니다.
    # qpos[0]   : X축 위치
    # qpos[1]   : Y축 위치
    # qpos[2]   : Z축 위치
    # qpos[3:7] : 로봇 회전을 나타내는 쿼터니언
    return {
        "x_m": float(data.qpos[0]),
        "y_m": float(data.qpos[1]),
        "z_m": float(data.qpos[2]),
        "yaw_rad": float(yaw_from_quat(data.qpos[3:7])),
    }


# ============================================================
# 7. 실시간 시뮬레이션 반복 실행
# ============================================================

def realtime_loop(
    mujoco,
    model,
    data,
    viewer,
    duration_s: float,
    control=None,
    logger=None,
) -> None:
    """
    지정한 시간 동안 MuJoCo 시뮬레이션을 반복 실행합니다.

    한 번 반복할 때 순서
    1. control 함수 실행
    2. 물리 계산 한 단계 진행
    3. logger 함수 실행
    4. 화면 갱신
    5. 남은 시간만큼 잠시 대기
    """

    # 반복을 시작한 실제 시각을 저장합니다.
    start = time.time()

    # 뷰어가 열려 있고 duration_s초가 지나지 않은 동안 반복합니다.
    while viewer.is_running() and time.time() - start < duration_s:

        # 이번 반복이 시작된 실제 시각입니다.
        tick = time.time()

        # control 함수가 전달되었다면 실행합니다.
        # 예: 현재 위치에 따라 바퀴 속도를 설정하는 함수
        if control:
            control(model, data)

        # MuJoCo 물리 시뮬레이션을 한 단계 진행합니다.
        mujoco.mj_step(model, data)

        # logger 함수가 전달되었다면 실행합니다.
        # 예: 현재 시간과 위치를 리스트에 기록하는 함수
        if logger:
            logger(model, data)

        # 계산 결과를 MuJoCo 화면에 반영합니다.
        viewer.sync()

        # 한 단계 계산 시간보다 빨리 끝났다면 남은 시간을 계산합니다.
        delay = model.opt.timestep - (time.time() - tick)

        # 남은 시간만큼 기다려 실제 시간과 비슷한 속도로 맞춥니다.
        if delay > 0:
            time.sleep(delay)


# ============================================================
# 8. 추가 장면 XML 만들기
# ============================================================

def make_extension_scene(
    name: str,
    extra_worldbody: str = "",
    extra_sensor: str = "",
    extra_actuator: str = "",
) -> Path:
    """
    공식 TurtleBot3 모델을 포함하면서 추가 요소가 들어간
    새로운 MuJoCo XML 파일을 만듭니다.

    extra_worldbody : 장애물, 차선, 표지판 등
    extra_sensor    : 카메라, 거리 센서 등
    extra_actuator  : 모터 등 추가 액추에이터
    """

    # 새 XML 파일을 저장할 extensions 폴더 경로입니다.
    extensions_dir = ROOT / "extensions"

    # extensions 폴더가 없으면 자동으로 만듭니다.
    # 이 줄이 없으면 FileNotFoundError가 발생할 수 있습니다.
    extensions_dir.mkdir(parents=True, exist_ok=True)

    # 실제로 만들 XML 파일의 전체 경로입니다.
    path = extensions_dir / name

    # 공식 TurtleBot3 Burger 모델 XML 경로를 가져옵니다.
    # as_posix()는 Windows의 역슬래시를 슬래시로 바꿉니다.
    include_path = model_path().as_posix()

    # f-string을 사용해 MuJoCo XML 내용을 만듭니다.
    xml = f"""<mujoco model="{name}">
  <!-- 공식 TurtleBot3 Burger 로봇 모델을 현재 장면에 포함합니다. -->
  <include file="{include_path}"/>

  <!-- 뷰어가 처음 열릴 때 화면 중심과 표시 범위를 설정합니다. -->
  <statistic center="0.3 0 0.4" extent="3"/>

  <!-- 기본 조명과 카메라 각도를 설정합니다. -->
  <visual>
    <headlight diffuse="0.6 0.6 0.6"
               ambient="0.3 0.3 0.3"
               specular="0 0 0"/>
    <global azimuth="120" elevation="-20"/>
  </visual>

  <!-- 장면에서 사용할 텍스처와 재질을 정의합니다. -->
  <asset>
    <!-- 하늘 배경용 그라데이션 텍스처입니다. -->
    <texture type="skybox" builtin="gradient"
             rgb1="0.3 0.5 0.7" rgb2="0 0 0"
             width="512" height="3072"/>

    <!-- 바닥에 사용할 체크무늬 텍스처입니다. -->
    <texture type="2d" name="groundplane_ext"
             builtin="checker" mark="edge"
             rgb1="0.2 0.3 0.4" rgb2="0.1 0.2 0.3"
             markrgb="0.8 0.8 0.8"
             width="300" height="300"/>

    <!-- 위 텍스처를 바닥에 적용하기 위한 재질입니다. -->
    <material name="groundplane_ext"
              texture="groundplane_ext"
              texuniform="true"
              texrepeat="8 8"
              reflectance="0.2"/>
  </asset>

  <!-- 실제 시뮬레이션 공간에 놓일 물체를 정의합니다. -->
  <worldbody>
    <!-- 위에서 아래로 비추는 조명입니다. -->
    <light pos="0 0 3" dir="0 0 -1" directional="true"/>

    <!-- 로봇이 움직일 평면 바닥입니다. -->
    <geom name="floor_ext" size="0 0 0.05"
          type="plane" material="groundplane_ext"/>

    <!-- 호출할 때 전달한 장애물이나 차선을 여기에 넣습니다. -->
    {extra_worldbody}
  </worldbody>

  <!-- 호출할 때 전달한 센서 XML을 여기에 넣습니다. -->
  <sensor>{extra_sensor}</sensor>

  <!-- 호출할 때 전달한 액추에이터 XML을 여기에 넣습니다. -->
  <actuator>{extra_actuator}</actuator>
</mujoco>"""

    # 완성한 XML 문자열을 UTF-8 파일로 저장합니다.
    path.write_text(xml, encoding="utf-8")

    # 생성된 XML 파일 경로를 반환합니다.
    return path


# ============================================================
# 9. JSON 결과 저장
# ============================================================

def save_json(obj, name: str) -> Path:
    """
    파이썬 객체를 사람이 읽기 쉬운 JSON 파일로 저장합니다.

    obj  : 저장할 딕셔너리, 리스트 등의 데이터
    name : 저장할 파일 이름, 예: result.json
    """

    # outputs 폴더를 준비하고 저장할 전체 경로를 가져옵니다.
    path = output_path(name)

    # 파이썬 데이터를 JSON 문자열로 바꿔 파일에 저장합니다.
    path.write_text(
        json.dumps(
            obj,
            # 한글을 유니코드 코드로 바꾸지 않고 그대로 저장합니다.
            ensure_ascii=False,
            # 들여쓰기 2칸을 사용해 읽기 쉽게 만듭니다.
            indent=2,
        ),
        encoding="utf-8",
    )

    # 저장된 JSON 파일 경로를 반환합니다.
    return path