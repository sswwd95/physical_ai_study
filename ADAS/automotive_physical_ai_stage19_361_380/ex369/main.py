import numpy as np
for action in [np.array([0,0]),np.array([.5,.2]),np.array([1,-1])]:
    cost=.05*float(np.sum(action**2))
    print(action,cost)
