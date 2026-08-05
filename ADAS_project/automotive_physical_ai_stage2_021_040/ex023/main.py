sensor_frame = {
    "time_s": 1.2,
    "speed_mps": 6.8,
    "steering_deg": 3.5,
    "front_distance_m": 8.1,
}

for name, value in sensor_frame.items():
    print(f"{name:20s}: {value}")
