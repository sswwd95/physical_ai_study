import numpy as np

distance = np.array([8.0, 5.5, 3.2, 2.8, 1.9, 4.1])
mask = distance < 3.0

print("위험 마스크:", mask)
print("위험 거리:", distance[mask])
print("위험 샘플 수:", int(mask.sum()))
