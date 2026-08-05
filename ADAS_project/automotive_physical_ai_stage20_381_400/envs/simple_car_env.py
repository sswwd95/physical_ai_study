import math
import numpy as np
import gymnasium as gym
from gymnasium import spaces

class SimpleCarEnv(gym.Env):
    metadata={"render_modes":[]}

    def __init__(self,max_steps=300,dt=0.1,seed=42):
        super().__init__()
        self.max_steps=int(max_steps)
        self.dt=float(dt)
        self.rng=np.random.default_rng(seed)
        self.observation_space=spaces.Box(
            low=np.array([-5,-3,-math.pi,0,0],dtype=np.float32),
            high=np.array([5,3,math.pi,2,20],dtype=np.float32),
            dtype=np.float32)
        self.action_space=spaces.Box(
            low=np.array([-1,-1],dtype=np.float32),
            high=np.array([1,1],dtype=np.float32),
            dtype=np.float32)
        self.state=None
        self.steps=0

    def _get_obs(self):
        return self.state.astype(np.float32)

    def reset(self,seed=None,options=None):
        super().reset(seed=seed)
        if seed is not None:
            self.rng=np.random.default_rng(seed)
        self.state=np.array([
            0.0,
            self.rng.uniform(-1,1),
            self.rng.uniform(-0.3,0.3),
            self.rng.uniform(0.2,0.8),
            self.rng.uniform(8,18)
        ],dtype=np.float32)
        self.steps=0
        return self._get_obs(),{}

    def step(self,action):
        action=np.clip(np.asarray(action,dtype=np.float32),-1,1)
        throttle,steering=float(action[0]),float(action[1])
        x,e,heading,speed,obstacle=self.state
        accel=1.2*throttle-0.25*speed
        yaw_rate=1.4*steering
        speed=float(np.clip(speed+accel*self.dt,0,2))
        heading=float(np.clip(heading+yaw_rate*self.dt,-math.pi,math.pi))
        x+=speed*math.cos(heading)*self.dt
        e+=speed*math.sin(heading)*self.dt
        obstacle-=speed*self.dt

        progress=speed*self.dt
        lane_penalty=1.5*abs(e)
        heading_penalty=0.4*abs(heading)
        action_penalty=0.05*float(np.sum(action**2))
        collision=obstacle<=0.5
        lane_departure=abs(e)>=2.5

        reward=progress-lane_penalty-heading_penalty-action_penalty
        if collision: reward-=25
        if lane_departure: reward-=15

        self.state=np.array([x,e,heading,speed,obstacle],dtype=np.float32)
        self.steps+=1
        terminated=bool(collision or lane_departure)
        truncated=bool(self.steps>=self.max_steps)
        info={
            "collision":collision,
            "lane_departure":lane_departure,
            "progress_reward":progress,
            "lane_penalty":lane_penalty,
            "heading_penalty":heading_penalty,
            "action_penalty":action_penalty
        }
        return self._get_obs(),float(reward),terminated,truncated,info
