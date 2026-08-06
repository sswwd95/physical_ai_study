import math
from copy import deepcopy
from .mission_schema import ActionName, SafetyDecision
class SafetySupervisor:
    def __init__(self,cfg):
        self.max_alt=float(cfg['max_altitude_m']); self.min_alt=float(cfg['min_altitude_m']); self.max_dist=float(cfg['max_horizontal_distance_m'])
        self.max_speed=float(cfg['max_speed_mps']); self.max_wait=float(cfg['max_wait_sec']); self.allowed=set(cfg['allowed_actions'])
    def review(self,cmd,pos):
        safe=deepcopy(cmd); reasons=[]; modified=False
        if safe.action.value not in self.allowed: return SafetyDecision(approved=False,reasons=['허용되지 않은 동작'],command=safe,risk_level='critical')
        if safe.action==ActionName.EMERGENCY_STOP: return SafetyDecision(approved=True,reasons=['비상 정지 최우선 승인'],command=safe,risk_level='critical')
        old=safe.speed_mps; safe.speed_mps=max(.1,min(old,self.max_speed)); modified|=safe.speed_mps!=old
        if safe.speed_mps!=old: reasons.append('속도 상한 적용')
        old=safe.duration_sec; safe.duration_sec=max(0,min(old,self.max_wait)); modified|=safe.duration_sec!=old
        if safe.duration_sec!=old: reasons.append('대기 시간 상한 적용')
        if safe.action==ActionName.TAKEOFF:
            old=safe.z_m; safe.z_m=min(max(old,self.min_alt),self.max_alt); modified|=safe.z_m!=old
            if safe.z_m!=old: reasons.append('이륙 고도 제한')
        if safe.action==ActionName.GOTO:
            r=math.hypot(safe.x_m,safe.y_m)
            if r>self.max_dist:
                s=self.max_dist/r; safe.x_m*=s; safe.y_m*=s; modified=True; reasons.append('지오펜스 안으로 좌표 축소')
            safe.z_m=min(max(safe.z_m,self.min_alt),self.max_alt)
        if safe.action==ActionName.MOVE_RELATIVE:
            tx,ty,tz=pos[0]+safe.x_m,pos[1]+safe.y_m,pos[2]+safe.z_m
            if math.hypot(tx,ty)>self.max_dist: return SafetyDecision(approved=False,reasons=['지오펜스 이탈 예상'],command=safe,risk_level='high')
            if not self.min_alt<=tz<=self.max_alt: return SafetyDecision(approved=False,reasons=['고도 제한 위반 예상'],command=safe,risk_level='high')
        safe.yaw_deg=max(-180,min(180,safe.yaw_deg))
        return SafetyDecision(approved=True,modified=modified,reasons=reasons or ['안전 규칙 통과'],command=safe,risk_level='medium' if modified else 'low')
