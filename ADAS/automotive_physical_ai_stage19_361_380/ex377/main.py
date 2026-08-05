from gymnasium.utils.env_checker import check_env
from envs.simple_car_env import SimpleCarEnv
env=SimpleCarEnv()
check_env(env,skip_render_check=True)
print("environment check passed")
env.close()
