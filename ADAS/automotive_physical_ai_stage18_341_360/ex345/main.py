from common.safety_utils import safe_distance
for speed in [3,5,8,12]:
    print(speed,safe_distance(speed,reaction_time=1.2,friction=.7,margin=2))
