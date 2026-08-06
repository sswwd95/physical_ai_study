import pathlib
import mujoco

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()
SKYDIO_DIR = PROJECT_ROOT / "external" / "mujoco_menagerie" / "skydio_x2"
SKYDIO_XML_PATH = SKYDIO_DIR / "x2.xml"
ASSETS_DIR = (SKYDIO_DIR / "assets").as_posix()

def build_model(dt):
    with open(SKYDIO_XML_PATH, "r", encoding="utf-8") as f:
        x2_xml = f.read()

    # assetdir 경로를 절대경로로 변경
    x2_xml = x2_xml.replace('assetdir="assets"', f'assetdir="{ASSETS_DIR}"')

    # x2 body 내부에 전방 카메라 (tracking_camera) 추가
    camera_xml = '<camera name="tracking_camera" pos=".28 0 .03" xyaxes="0 -1 0 0 0 1" fovy="60"/>'
    idx = x2_xml.rfind('</body>')
    if idx != -1:
        x2_xml = x2_xml[:idx] + f'  {camera_xml}\n  ' + x2_xml[idx:]

    # worldbody에 지면, 조명 및 tracking target 추가
    extra_worldbody = '''
    <light pos="0 0 8"/>
    <geom type="plane" size="20 20 .1" rgba=".2 .3 .2 1"/>
    <body name="target" mocap="true" pos="4 0 1.6">
      <geom type="sphere" size=".28" rgba="1 0 0 1" contype="0" conaffinity="0"/>
    </body>
    '''
    
    wb_idx = x2_xml.rfind('</worldbody>')
    if wb_idx != -1:
        full_xml = x2_xml[:wb_idx] + extra_worldbody + x2_xml[wb_idx:]
    else:
        full_xml = x2_xml

    m = mujoco.MjModel.from_xml_string(full_xml)
    m.opt.timestep = dt
    d = mujoco.MjData(m)

    # 드론 초기 위치 설정 (pos: 0 0 1.6)
    bid = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_BODY, "x2")
    if bid != -1:
        jnt_adr = m.body_jntadr[bid]
        qpos_adr = m.jnt_qposadr[jnt_adr]
        d.qpos[qpos_adr:qpos_adr+3] = [0, 0, 1.6]
        d.qpos[qpos_adr+3:qpos_adr+7] = [1, 0, 0, 0]

    mujoco.mj_forward(m, d)
    return m, d

