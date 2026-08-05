from common.mujoco_utils import load_model_and_data
_, model, _ = load_model_and_data()
print("bodies:", model.nbody)
print("joints:", model.njnt)
print("geoms:", model.ngeom)
print("sites:", model.nsite)
print("actuators:", model.nu)
print("sensors:", model.nsensor)
