import math
wheel_radius_m = 0.033
ticks_per_rev = 4096
distance_per_tick = 2 * math.pi * wheel_radius_m / ticks_per_rev
print("distance per tick (m):", distance_per_tick)
print("distance per tick (mm):", distance_per_tick * 1000)
