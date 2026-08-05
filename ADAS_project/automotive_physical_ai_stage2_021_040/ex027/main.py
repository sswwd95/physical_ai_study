import numpy as np

speed = np.array([5.0, 5.5, 6.2, 6.8], dtype=float)
steering = np.array([0.0, 2.0, -1.5, 3.2], dtype=float)

print("speed:", speed)
print("shape:", speed.shape)
print("dtype:", speed.dtype)
print("2열 센서 행렬:")
print(np.column_stack([speed, steering]))
