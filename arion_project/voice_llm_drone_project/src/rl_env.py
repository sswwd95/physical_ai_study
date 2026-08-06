import gymnasium as gym, numpy as np
from gymnasium import spaces
class SafetyTuningEnv(gym.Env):
    def __init__(self):
        self.observation_space=spaces.Box(np.array([-1,-1,-1,0],np.float32),np.array([1,1,1,1],np.float32)); self.action_space=spaces.Box(np.array([.1,.1],np.float32),np.array([1.5,2],np.float32)); self.state=np.zeros(4,np.float32); self.steps=0
    def reset(self,seed=None,options=None):
        super().reset(seed=seed); self.state=self.np_random.uniform([-1,-1,-1,0],[1,1,1,1]).astype(np.float32); self.steps=0; return self.state,{}
    def step(self,action):
        speed,gain=action; err=float(np.linalg.norm(self.state[:3])); risk=float(self.state[3]); reward=min(speed,1)*(1-.5*risk)-err-3*risk*max(0,speed-gain); self.state[:3]*=.9; self.state[3]=np.clip(self.state[3]+self.np_random.normal(0,.05),0,1); self.steps+=1; return self.state,reward,err<.05,self.steps>=100,{}
