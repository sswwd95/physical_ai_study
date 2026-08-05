from common.diff_drive import twist_to_wheels, wheels_to_twist
true_base = 0.160
wrong_base = 0.175
left, right = twist_to_wheels(0.0, 1.0, wheel_base=true_base)
_, estimated_angular = wheels_to_twist(left, right, wheel_base=wrong_base)
error_pct = (estimated_angular - 1.0) * 100
print("estimated angular:", round(estimated_angular,4))
print("error percent:", round(error_pct,2))
