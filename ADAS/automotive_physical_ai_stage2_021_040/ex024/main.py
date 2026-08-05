front_distance_m = 2.6

if front_distance_m < 1.5:
    state = "STOP"
elif front_distance_m < 3.0:
    state = "CAUTION"
else:
    state = "NORMAL"

print("전방 거리:", front_distance_m, "m")
print("판정:", state)
