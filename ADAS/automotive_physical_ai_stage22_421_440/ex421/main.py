from common.project_viewer_utils import load_project
mujoco,model,data,path=load_project()
print("bodies:",model.nbody,"geoms:",model.ngeom,"sensors:",model.nsensor)
mujoco.viewer.launch(model,data)
