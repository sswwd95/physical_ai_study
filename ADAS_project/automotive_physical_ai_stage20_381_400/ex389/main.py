from stable_baselines3.common.monitor import Monitor
from envs.simple_car_env import SimpleCarEnv
from common.sb3_utils import output_path
log_file=output_path("ex389_monitor.csv")
env=Monitor(SimpleCarEnv(max_steps=80),filename=str(log_file))
obs,_=env.reset(seed=42)
for _ in range(80):
    obs,r,term,trunc,info=env.step(env.action_space.sample())
    if term or trunc: break
env.close()
print("monitor base:",log_file)
