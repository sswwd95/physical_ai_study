from dataclasses import dataclass
import math, numpy as np, mujoco
@dataclass
class ControlOutput:
    vx:float; vy:float; vz:float; yaw_rate:float; state:str; safety_active:bool
class TrackingController:
    def __init__(self,cfg):self.c=cfg
    def compute(self,center,area,shape,alt,lost):
        h,w=shape
        if center is None or lost>0:return ControlOutput(0,0,0,self.c['search_yaw_rate'],'SEARCH',False)
        ex=(center[0]-w/2)/(w/2); ey=(center[1]-h/2)/(h/2); safe=area>=self.c['safe_area_ratio']
        if safe:vx=-self.c['max_horizontal_speed']*.6; state='SAFETY_BACKOFF'
        else:vx=float(np.clip(self.c['pitch_gain']*(self.c['target_area_ratio']-area)*12,-self.c['max_horizontal_speed'],self.c['max_horizontal_speed'])); state='TRACK'
        vy=float(np.clip(-self.c['roll_gain']*ex,-self.c['max_horizontal_speed'],self.c['max_horizontal_speed'])); vz=float(np.clip(self.c['altitude_gain']*(self.c['desired_altitude']-alt)-.25*ey,-self.c['max_vertical_speed'],self.c['max_vertical_speed'])); yr=float(np.clip(-self.c['yaw_gain']*ex,-.8,.8)); return ControlOutput(vx,vy,vz,yr,state,safe)
class KinematicDrone:
    def __init__(self,m,d):self.m=m; self.d=d; self.adr=int(m.jnt_qposadr[0])
    def pose(self):
        p=self.d.qpos[self.adr:self.adr+3].copy(); q=self.d.qpos[self.adr+3:self.adr+7]; mat=np.zeros(9); mujoco.mju_quat2Mat(mat,q); mat=mat.reshape(3,3); return p,math.atan2(mat[1,0],mat[0,0])
    def step(self,c,dt):
        p,y=self.pose(); co,si=math.cos(y),math.sin(y); p+=np.array([co*c.vx-si*c.vy,si*c.vx+co*c.vy,c.vz])*dt; p[2]=max(.2,p[2]); y+=c.yaw_rate*dt; q=np.array([math.cos(y/2),0,0,math.sin(y/2)]); self.d.qpos[self.adr:self.adr+3]=p; self.d.qpos[self.adr+3:self.adr+7]=q; self.d.qvel[:]=0; mujoco.mj_forward(self.m,self.d)
