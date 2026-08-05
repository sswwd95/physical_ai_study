from common.tb3_burger_utils import load_tb3
mujoco,model,data,ids=load_tb3()
print("nbody:",model.nbody,"njnt:",model.njnt,"nu:",model.nu)
for key,value in ids.items():
    print(key,value)
for i in range(model.nu):
    print("actuator",i,mujoco.mj_id2name(model,mujoco.mjtObj.mjOBJ_ACTUATOR,i))
