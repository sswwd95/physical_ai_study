import json,numpy as np
from gymnasium.utils.env_checker import check_env
from envs.simple_car_env import SimpleCarEnv
from common.rl_utils import output_path
env=SimpleCarEnv(max_steps=100,seed=42)
check_env(env,skip_render_check=True)
returns=[]; lengths=[]; terminations={"collision":0,"lane_departure":0,"truncated":0}
for seed in range(15):
    obs,_=env.reset(seed=seed); total=0
    for _ in range(100):
        steering=np.clip(-1.2*obs[1]-.8*obs[2],-1,1)
        throttle=.45 if obs[4]>3 else -.6
        obs,r,term,trunc,info=env.step(np.array([throttle,steering],dtype=np.float32))
        total+=r
        if term or trunc:
            terminations["collision"]+=int(info.get("collision",False))
            terminations["lane_departure"]+=int(info.get("lane_departure",False))
            terminations["truncated"]+=int(trunc)
            break
    returns.append(total); lengths.append(env.steps)
report={
    "episodes":len(returns),
    "mean_return":float(np.mean(returns)),
    "std_return":float(np.std(returns)),
    "mean_length":float(np.mean(lengths)),
    "terminations":terminations,
    "observation_shape":list(env.observation_space.shape),
    "action_shape":list(env.action_space.shape),
}
p=output_path("ex380_integrated_rl_env_report.json")
p.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report); print(p)
env.close()
