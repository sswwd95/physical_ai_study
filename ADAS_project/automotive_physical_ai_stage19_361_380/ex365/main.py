from envs.simple_car_env import SimpleCarEnv
env=SimpleCarEnv(seed=42)
obs,info=env.reset(seed=42)
print("observation:",obs)
print("info:",info)
env.close()
