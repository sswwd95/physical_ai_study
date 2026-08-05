from common.safety_utils import braking_distance
for speed in [3,5,8,12,16]:
    print(speed,braking_distance(speed,friction=.7))
