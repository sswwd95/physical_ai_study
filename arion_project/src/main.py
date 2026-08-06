import argparse,time,math,cv2,mujoco,mujoco.viewer,numpy as np
from .config import load_config,result_dir
from .scene import build_model
from .vision import ColorDetector,AlphaBetaTracker
from .controller import TrackingController,KinematicDrone
from .logger import CsvLogger
def parse():
 p=argparse.ArgumentParser(); p.add_argument('--viewer',action='store_true'); p.add_argument('--headless',action='store_true'); return p.parse_args()
def move_target(d,m,t):
 bid=mujoco.mj_name2id(m,mujoco.mjtObj.mjOBJ_BODY,'target'); mid=m.body_mocapid[bid]; d.mocap_pos[mid]=[4,8,1.8] if 18<t<23 else [4+.5*math.sin(.35*t),1.4*math.sin(.55*t),1.6+.45*math.sin(.42*t)]
def main():
 a=parse(); cfg=load_config(); s=cfg['simulation']; m,d=build_model(float(s['timestep'])); r=mujoco.Renderer(m,height=s['height'],width=s['width']); det=ColorDetector(cfg['vision']); tr=AlphaBetaTracker(cfg['vision']['alpha'],cfg['vision']['beta']); ctl=TrackingController(cfg['control']); drone=KinematicDrone(m,d); log=CsvLogger(result_dir()/'flight_log.csv'); v=mujoco.viewer.launch_passive(m,d) if a.viewer and not a.headless else None; lost=0; last=time.perf_counter()
 try:
  while d.time<s['duration_sec']:
   t0=time.perf_counter(); move_target(d,m,d.time); mujoco.mj_forward(m,d); r.update_scene(d,camera='tracking_camera'); rgb=r.render(); td=time.perf_counter(); de=det.detect(rgb); dl=(time.perf_counter()-td)*1000
   if de.found: lost=0; center=tr.update(de.center,s['timestep'])
   else: lost+=1; center=tr.predict(s['timestep']) if lost<=cfg['vision']['lost_frame_threshold'] else None
   pos,_=drone.pose(); cmd=ctl.compute(center,de.area_ratio if de.found else 0,(s['height'],s['width']),float(pos[2]),lost); drone.step(cmd,s['timestep']); mujoco.mj_step(m,d); now=time.perf_counter(); fps=1/max(now-last,1e-6); last=now; pos,_=drone.pose(); log.write({'sim_time':d.time,'detected':de.found,'center_x':'' if center is None else float(center[0]),'center_y':'' if center is None else float(center[1]),'area_ratio':de.area_ratio,'confidence':de.confidence,'lost_frames':lost,'state':cmd.state,'safety_active':cmd.safety_active,'fps':fps,'detect_latency_ms':dl,'pipeline_latency_ms':(now-t0)*1000,'drone_x':pos[0],'drone_y':pos[1],'drone_z':pos[2],'vx':cmd.vx,'vy':cmd.vy,'vz':cmd.vz,'yaw_rate':cmd.yaw_rate})
   if de.bbox:
    x,y,w,h=de.bbox; cv2.rectangle(rgb,(x,y),(x+w,y+h),(0,255,0),2)
   cv2.putText(rgb,f'{cmd.state} FPS:{fps:.1f}',(10,28),cv2.FONT_HERSHEY_SIMPLEX,.7,(255,255,255),2)
   if not a.headless:
    cv2.imshow('Tracking Camera',cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1)&0xFF==27:break
   if v:v.sync()
   if s['realtime']:time.sleep(max(0,s['timestep']-(time.perf_counter()-t0)))
 finally:
  log.close(); r.close(); cv2.destroyAllWindows(); v.close() if v else None
if __name__=='__main__':main()
