from common.diff_drive import twist_to_wheels, wheels_to_twist
left, right = twist_to_wheels(0.0, 1.2)
linear, angular = wheels_to_twist(left, right)
print("wheel commands:", round(left,3), round(right,3))
print("recovered twist:", round(linear,3), round(angular,3))
