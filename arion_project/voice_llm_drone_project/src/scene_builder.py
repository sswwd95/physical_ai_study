import os
from pathlib import Path
import mujoco
from .config import ROOT
FALLBACK_XML='''<mujoco model="voice_llm_quad"><option timestep="0.01" gravity="0 0 -9.81"/><visual><global azimuth="140" elevation="-25"/></visual><worldbody><light pos="0 0 8"/><geom type="plane" size="20 20 .1" rgba=".25 .3 .25 1"/><body name="drone" pos="0 0 .3"><freejoint/><geom type="box" size=".22 .16 .06" mass="1.4" rgba=".1 .2 .8 1"/><geom type="capsule" fromto="-.35 -.25 0 .35 .25 0" size=".018"/><geom type="capsule" fromto="-.35 .25 0 .35 -.25 0" size=".018"/></body><body name="goal" mocap="true" pos="2 0 1.5"><geom type="sphere" size=".12" rgba="1 .1 .1 .8" contype="0" conaffinity="0"/></body></worldbody></mujoco>'''
def load_model(cfg):
    env=cfg['simulation'].get('menagerie_env_var','MUJOCO_MENAGERIE_PATH'); base=os.getenv(env)
    candidates=[]
    if base: candidates += [Path(base)/'skydio_x2'/'scene.xml',Path(base)/'skydio_x2'/'x2.xml']
    candidates += [ROOT/'external'/'mujoco_menagerie'/'skydio_x2'/'scene.xml',ROOT/'external'/'mujoco_menagerie'/'skydio_x2'/'x2.xml']
    if cfg['simulation'].get('use_menagerie',True):
        for p in candidates:
            if p.exists():
                try:
                    m=mujoco.MjModel.from_xml_path(str(p)); m.opt.timestep=float(cfg['simulation']['timestep']); return m,'menagerie:'+str(p)
                except Exception as exc: print('[SCENE] load failed:',p,exc)
    m=mujoco.MjModel.from_xml_string(FALLBACK_XML); m.opt.timestep=float(cfg['simulation']['timestep']); return m,'fallback_minimal_quadrotor'
