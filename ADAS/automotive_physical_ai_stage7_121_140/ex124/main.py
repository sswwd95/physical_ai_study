from common.diff_drive import twist_to_wheels
left, right = twist_to_wheels(0.20, 0.50)
print("left wheel (rad/s):", round(left, 4))
print("right wheel (rad/s):", round(right, 4))
