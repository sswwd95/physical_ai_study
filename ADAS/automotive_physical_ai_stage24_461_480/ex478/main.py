import time,json
from common.traffic_utils import load_project,set_ego,output_path
mujoco,model,data,plan=load_project()
request_time=None; response_time=None
def key(k):
    global response_time
    if k==32 and request_time is not None and response_time is None: response_time=time.time()
with mujoco.viewer.launch_passive(model,data,key_callback=key) as viewer:
    start=time.time()
    while viewer.is_running() and time.time()-start<15:
        if time.time()-start>5 and request_time is None:
            request_time=time.time(); print("TAKEOVER REQUEST - press SPACE")
        set_ego(data,4,4)
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
result={"response_s":None if response_time is None else response_time-request_time}
p=output_path("ex478_takeover_response.json"); p.write_text(json.dumps(result,indent=2)); print(result,p)
