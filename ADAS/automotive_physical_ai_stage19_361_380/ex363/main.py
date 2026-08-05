import numpy as np
from gymnasium import spaces
action_space=spaces.Box(
    low=np.array([-1,-1],dtype=np.float32),
    high=np.array([1,1],dtype=np.float32))
print(action_space)
print("sample:",action_space.sample())
