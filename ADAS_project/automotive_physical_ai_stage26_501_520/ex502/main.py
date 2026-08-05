from common.tb3_burger_utils import load_tb3
mujoco,model,data,ids=load_tb3()
print(ids)
mujoco.viewer.launch(model,data)
