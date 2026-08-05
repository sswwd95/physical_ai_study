from common.diff_drive import wheels_to_twist
linear, angular = wheels_to_twist(3.0, 7.0)
print("linear velocity (m/s):", round(linear, 4))
print("angular velocity (rad/s):", round(angular, 4))
