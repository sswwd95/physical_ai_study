from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
MODELS = ROOT / "models"

def output_path(name):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def model_path(name):
    MODELS.mkdir(parents=True, exist_ok=True)
    return MODELS / name

def save_json(data, name):
    p = output_path(name)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return p

def evaluate_policy_manual(model, env, episodes=10, deterministic=True):
    returns=[]
    lengths=[]
    terminations={"collision":0,"lane_departure":0,"truncated":0}
    for ep in range(episodes):
        obs,info=env.reset(seed=ep)
        total=0.0
        steps=0
        while True:
            action,_=model.predict(obs,deterministic=deterministic)
            obs,reward,terminated,truncated,info=env.step(action)
            total+=float(reward)
            steps+=1
            if terminated or truncated:
                terminations["collision"]+=int(info.get("collision",False))
                terminations["lane_departure"]+=int(info.get("lane_departure",False))
                terminations["truncated"]+=int(truncated)
                break
        returns.append(total)
        lengths.append(steps)
    return {
        "episodes":episodes,
        "mean_return":float(np.mean(returns)),
        "std_return":float(np.std(returns)),
        "mean_length":float(np.mean(lengths)),
        "terminations":terminations,
    }

def safety_filter(action, obstacle_distance, lateral_error):
    action=np.asarray(action,dtype=np.float32).copy()
    if obstacle_distance < 3.0:
        action[0]=min(action[0],-0.5)
    if abs(lateral_error) > 1.8:
        action[1]=float(np.clip(action[1]-0.6*np.sign(lateral_error),-1,1))
    return np.clip(action,-1,1)
