import argparse,csv,json,time
from collections import deque
import mujoco, mujoco.viewer
from .config import load_config,result_dir
from .scene_builder import load_model
from .llm_planner import LLMPlanner
from .safety import SafetySupervisor
from .drone_controller import KinematicDroneController
from .voice_input import VoiceInput
SCRIPT=deque(['이륙해서 높이 1.5미터로 올라가','앞으로 2미터 이동해','오른쪽으로 1미터 이동해','왼쪽으로 90도 회전해','제자리에서 3초 동안 대기해','착륙해'])
FIELDS=['wall_time','sim_time','source_text','planner_backend','action','approved','modified','risk_level','safety_reasons','planning_latency_ms','position_x','position_y','position_z','target_x','target_y','target_z','position_error','yaw_error_deg','state','success']
def args():
    p=argparse.ArgumentParser(); p.add_argument('--input',choices=['text','voice','scripted'],default='text'); p.add_argument('--viewer',action='store_true'); return p.parse_args()
def command_text(mode,voice):
    if mode=='voice': return voice.listen_once()
    if mode=='scripted':
        if not SCRIPT: return '즉시 정지'
        s=SCRIPT.popleft(); print('[SCRIPT]',s); return s
    return input('\n명령 입력(q=종료): ').strip()
def append(path,row):
    new=not path.exists()
    with path.open('a',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader() if new else None; w.writerow({k:row.get(k,'') for k in FIELDS})
def run():
    a=args(); cfg=load_config(); out=result_dir(); log=out/'mission_log.csv'; log.unlink(missing_ok=True)
    model,source=load_model(cfg); data=mujoco.MjData(model); mujoco.mj_forward(model,data)
    planner=LLMPlanner(cfg['llm']); safety=SafetySupervisor(cfg['safety']); ctrl=KinematicDroneController(model,data,cfg['controller'])
    voice=VoiceInput(**cfg['voice']) if a.input=='voice' else None; viewer=mujoco.viewer.launch_passive(model,data) if (a.viewer or cfg['simulation']['viewer']) else None
    total=successes=interventions=0
    try:
        while True:
            text=command_text(a.input,voice)
            if text.lower() in {'q','quit','exit','종료'}: break
            t=time.perf_counter(); cmd,backend=planner.plan(text); latency=(time.perf_counter()-t)*1000
            pos=tuple(float(x) for x in ctrl.position()); dec=safety.review(cmd,pos); total+=1; interventions+=int(dec.modified or not dec.approved)
            print('[PLAN]',cmd.model_dump()); print('[SAFETY]',dec.model_dump())
            if not dec.approved:
                append(log,{'wall_time':time.time(),'sim_time':data.time,'source_text':text,'planner_backend':backend,'action':cmd.action.value,'approved':False,'modified':dec.modified,'risk_level':dec.risk_level,'safety_reasons':' | '.join(dec.reasons),'planning_latency_ms':latency,'position_x':pos[0],'position_y':pos[1],'position_z':pos[2],'state':'REJECTED','success':False}); continue
            ctrl.set_command(dec.command); start=data.time; status=None
            while data.time-start<20:
                tick=time.perf_counter(); status=ctrl.step(); mujoco.mj_step(model,data)
                if viewer: viewer.sync()
                if cfg['simulation']['realtime']: time.sleep(max(0,model.opt.timestep-(time.perf_counter()-tick)))
                if status.complete: break
            ok=bool(status and status.complete); successes+=int(ok); p=ctrl.position()
            append(log,{'wall_time':time.time(),'sim_time':data.time,'source_text':text,'planner_backend':backend,'action':dec.command.action.value,'approved':True,'modified':dec.modified,'risk_level':dec.risk_level,'safety_reasons':' | '.join(dec.reasons),'planning_latency_ms':latency,'position_x':float(p[0]),'position_y':float(p[1]),'position_z':float(p[2]),'target_x':float(status.target_position[0]),'target_y':float(status.target_position[1]),'target_z':float(status.target_position[2]),'position_error':status.position_error,'yaw_error_deg':status.yaw_error_deg,'state':status.state,'success':ok})
            print('[RESULT]',ok,'error=',round(status.position_error,3))
            if dec.command.action.value=='emergency_stop' or (a.input=='scripted' and not SCRIPT): break
    finally:
        if viewer: viewer.close()
    summary={'model_source':source,'total_commands':total,'successful_commands':successes,'success_rate':successes/max(total,1),'safety_interventions':interventions}
    (out/'mission_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8'); print('[SUMMARY]',summary)
if __name__=='__main__': run()
