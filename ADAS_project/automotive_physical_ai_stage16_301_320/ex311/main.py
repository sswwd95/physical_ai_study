from common.control_utils import twist_to_wheels, wheels_to_twist
left,right=twist_to_wheels(0.20,0.60)
v,w=wheels_to_twist(left,right)
print("wheel rad/s:",left,right)
print("recovered twist:",v,w)
