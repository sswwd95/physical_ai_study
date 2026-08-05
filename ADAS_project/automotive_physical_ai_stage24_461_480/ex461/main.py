from common.traffic_utils import load_project
mujoco,model,data,plan=load_project()
print(plan)
mujoco.viewer.launch(model,data)
