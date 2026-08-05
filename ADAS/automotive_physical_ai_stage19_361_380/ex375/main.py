import numpy as np
def safety_filter(action,obstacle_distance):
    action=np.asarray(action,dtype=np.float32).copy()
    if obstacle_distance<3.0:
        action[0]=min(action[0],-.5)
    return np.clip(action,-1,1)
for d in [8,2.8,1.2]:
    print(d,safety_filter([.8,.2],d))
