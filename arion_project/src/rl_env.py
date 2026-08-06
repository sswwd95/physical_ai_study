import gymnasium as gym,numpy as np
from gymnasium import spaces
class TrackingGainEnv(gym.Env):
 def __init__(self):super().__init__(); self.observation_space=spaces.Box(-1,1,(4,),dtype=np.float32); self.action_space=spaces.Box(np.array([.1,.1,.1],np.float32),np.array([1.5,1.5,1.5],np.float32)); self.s=np.zeros(4,np.float32); self.n=0
 def reset(self,seed=None,options=None):super().reset(seed=seed); self.s=self.np_random.uniform(-1,1,4).astype(np.float32); self.n=0; return self.s,{}
 def step(self,a):
  yg,pg,rg=a; ex,ey,ed,risk=self.s; corr=np.array([rg*ex,yg*ex,pg*ed]); rew=-abs(ex)-abs(ey)-abs(ed)-2*risk*float(np.linalg.norm(corr)); self.s[:3]*=.88; self.s[3]=np.clip(self.s[3]+self.np_random.normal(0,.04),-1,1); self.n+=1; return self.s,float(rew),np.linalg.norm(self.s[:3])<.05,self.n>=100,{}
