import numpy as np
from gymnasium import spaces
obs_space=spaces.Box(
    low=np.array([-5,-3,-3.14,0,0],dtype=np.float32),
    high=np.array([5,3,3.14,2,20],dtype=np.float32))
print(obs_space)
print("sample:",obs_space.sample())
