from common.mujoco_utils import find_tb3_xml
path = find_tb3_xml()
print("selected model:", path)
print("exists:", path.exists())
print("using fallback:", "tb3_burger_training.xml" in path.name)
