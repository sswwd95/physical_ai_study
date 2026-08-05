def mps_to_kph(speed_mps: float) -> float:
    return speed_mps * 3.6

for speed in [0.0, 5.0, 10.0, 13.9]:
    print(f"{speed:4.1f} m/s -> {mps_to_kph(speed):5.1f} km/h")
