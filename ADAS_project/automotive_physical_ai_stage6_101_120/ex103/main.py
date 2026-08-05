from common.mujoco_utils import load_model_and_data
path, model, data = load_model_and_data()
print("model:", path)
print("nq:", model.nq, "nv:", model.nv, "nu:", model.nu, "nsensor:", model.nsensor)
print("simulation time:", data.time)
