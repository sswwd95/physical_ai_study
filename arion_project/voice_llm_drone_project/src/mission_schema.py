from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field, model_validator
class ActionName(str, Enum):
    TAKEOFF='takeoff'; LAND='land'; MOVE_RELATIVE='move_relative'; GOTO='goto'; ROTATE='rotate'; HOVER='hover'; EMERGENCY_STOP='emergency_stop'
class MissionCommand(BaseModel):
    action: ActionName
    x_m: float=0.0; y_m: float=0.0; z_m: float=0.0
    yaw_deg: float=0.0; duration_sec: float=0.0; speed_mps: float=0.8
    reason: str=''; source_text: str=''
    @model_validator(mode='after')
    def defaults(self):
        if self.action==ActionName.TAKEOFF and self.z_m<=0: self.z_m=1.5
        if self.action==ActionName.HOVER and self.duration_sec<=0: self.duration_sec=3.0
        return self
class SafetyDecision(BaseModel):
    approved: bool; modified: bool=False; reasons: list[str]=Field(default_factory=list)
    command: MissionCommand; risk_level: Literal['low','medium','high','critical']='low'
