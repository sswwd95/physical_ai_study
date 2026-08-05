import numpy as np
from common.sensor_utils import output_path
rng = np.random.default_rng(7)
steps = rng.normal(0, 0.0001, 10000)
random_walk = np.cumsum(steps)
path = output_path("ex157_random_walk.csv")
np.savetxt(path, random_walk, delimiter=",", header="random_walk", comments="")
print("final value:", random_walk[-1])
print("std:", random_walk.std())
print("saved:", path)
