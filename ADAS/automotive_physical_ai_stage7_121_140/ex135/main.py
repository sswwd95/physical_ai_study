from common.diff_drive import twist_to_wheels, wheels_to_twist
true_radius = 0.033
wrong_radius = 0.031
left, right = twist_to_wheels(0.20, 0.0, wheel_radius=true_radius)
estimated_linear, _ = wheels_to_twist(left, right, wheel_radius=wrong_radius)
error_pct = (estimated_linear - 0.20) / 0.20 * 100
print("estimated linear:", round(estimated_linear,4))
print("error percent:", round(error_pct,2))
