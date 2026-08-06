import math
from dataclasses import dataclass
import mujoco, numpy as np
from .mission_schema import ActionName
@dataclass
class ControllerStatus:
    complete: bool; position_error: float; yaw_error_deg: float; target_position: np.ndarray; target_yaw: float; state: str
class KinematicDroneController:
    def __init__(self,model,data,cfg):
        self.model=model; self.data=data; self.pos_tol=float(cfg['position_tolerance_m']); self.yaw_tol=float(cfg['yaw_tolerance_deg'])
        self.adr=self._free_adr(); self.target_position=self.position().copy(); self.target_yaw=0.; self.command=None; self.start=0.; self.stopped=False
    def _free_adr(self):
        for j in range(self.model.njnt):
            if self.model.jnt_type[j]==mujoco.mjtJoint.mjJNT_FREE: return int(self.model.jnt_qposadr[j])
        raise RuntimeError('free joint not found')
    def position(self): return self.data.qpos[self.adr:self.adr+3]
    def yaw(self):
        q=self.data.qpos[self.adr+3:self.adr+7]; a=np.zeros(9); mujoco.mju_quat2Mat(a,q); a=a.reshape(3,3); return math.atan2(a[1,0],a[0,0])
    def set_command(self,c):
        self.command=c; self.start=float(self.data.time); p=self.position().copy(); y=self.yaw()
        if c.action==ActionName.TAKEOFF: self.target_position=p.copy(); self.target_position[2]=c.z_m
        elif c.action==ActionName.LAND: self.target_position=p.copy(); self.target_position[2]=.2
        elif c.action==ActionName.MOVE_RELATIVE: self.target_position=p+np.array([c.x_m,c.y_m,c.z_m])
        elif c.action==ActionName.GOTO: self.target_position=np.array([c.x_m,c.y_m,c.z_m],float)
        elif c.action==ActionName.ROTATE: self.target_yaw=y+math.radians(c.yaw_deg)
        elif c.action==ActionName.HOVER: self.target_position=p.copy(); self.target_yaw=y
        elif c.action==ActionName.EMERGENCY_STOP: self.stopped=True; self.target_position=p.copy(); self.target_yaw=y
    def step(self):
        p=self.position().copy(); y=self.yaw(); dt=float(self.model.opt.timestep)
        if self.stopped:
            self.data.qvel[:]=0; return ControllerStatus(True,0,0,self.target_position.copy(),self.target_yaw,'EMERGENCY_STOP')
        speed=self.command.speed_mps if self.command else .8; d=self.target_position-p; dist=float(np.linalg.norm(d))
        if dist>1e-9: p += d*min(1.,speed*dt/dist)
        e=math.atan2(math.sin(self.target_yaw-y),math.cos(self.target_yaw-y)); y += float(np.clip(e,-math.radians(60)*dt,math.radians(60)*dt))
        q=np.array([math.cos(y/2),0,0,math.sin(y/2)]); self.data.qpos[self.adr:self.adr+3]=p; self.data.qpos[self.adr+3:self.adr+7]=q; self.data.qvel[:]=0; mujoco.mj_forward(self.model,self.data)
        pe=float(np.linalg.norm(self.target_position-p)); ye=abs(math.degrees(e)); complete=pe<=self.pos_tol and ye<=self.yaw_tol
        if self.command and self.command.action==ActionName.HOVER: complete=self.data.time-self.start>=self.command.duration_sec
        return ControllerStatus(complete,pe,ye,self.target_position.copy(),self.target_yaw,'COMPLETE' if complete else 'EXECUTING')
