from common.dynamics_utils import load_project
mujoco,model,data,plan=load_project()
print(plan)
print("bodies",model.nbody,"joints",model.njnt,"sensors",model.nsensor)
mujoco.viewer.launch(model,data)
