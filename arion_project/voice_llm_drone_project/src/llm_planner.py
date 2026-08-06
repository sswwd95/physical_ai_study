import json, os, re, requests
from .mission_schema import ActionName, MissionCommand
SYSTEM_PROMPT='''너는 드론 임무 계획기다. 사용자 한국어 명령을 JSON 한 개로만 변환한다. action은 takeoff, land, move_relative, goto, rotate, hover, emergency_stop 중 하나다. 필드는 action,x_m,y_m,z_m,yaw_deg,duration_sec,speed_mps,reason이다. x 전진+, y 왼쪽+, z 위쪽+, 왼쪽 회전+다. 불명확하거나 위험하면 emergency_stop. 설명문과 코드펜스 금지.'''
class LLMPlanner:
    def __init__(self,cfg):
        self.backend=os.getenv('DRONE_LLM_BACKEND',cfg.get('backend','auto')); self.model=os.getenv('DRONE_LLM_MODEL',cfg.get('model','qwen2.5:3b'))
        self.url=cfg.get('ollama_url'); self.timeout=float(cfg.get('timeout_sec',8))
    def plan(self,text):
        if self.backend in {'auto','ollama'}:
            try: return self._ollama(text),'ollama'
            except Exception as exc:
                if self.backend=='ollama': print('[LLM] fallback:',exc)
        return self._rule(text),'rule_fallback'
    def _ollama(self,text):
        r=requests.post(self.url,json={'model':self.model,'prompt':SYSTEM_PROMPT+'\n사용자: '+text,'stream':False,'format':'json'},timeout=self.timeout); r.raise_for_status()
        d=json.loads(r.json().get('response','{}')); d['source_text']=text
        return MissionCommand.model_validate(d)
    @staticmethod
    def _number(text,default=1.0):
        m=re.search(r'-?\d+(?:\.\d+)?',text); return float(m.group()) if m else default
    def _rule(self,text):
        v=self._number(text)
        if any(w in text for w in ['즉시 정지','비상 정지','멈춰']): return MissionCommand(action=ActionName.EMERGENCY_STOP,reason='비상 정지',source_text=text)
        if '착륙' in text or '내려' in text: return MissionCommand(action=ActionName.LAND,reason='착륙',source_text=text)
        if '이륙' in text or '올라가' in text: return MissionCommand(action=ActionName.TAKEOFF,z_m=max(v,1),reason='이륙/상승',source_text=text)
        if any(w in text for w in ['대기','호버','제자리']): return MissionCommand(action=ActionName.HOVER,duration_sec=max(v,1),reason='대기',source_text=text)
        if '회전' in text or '돌아' in text:
            return MissionCommand(action=ActionName.ROTATE,yaw_deg=(-v if '오른' in text else v),reason='회전',source_text=text)
        if '좌표' in text:
            n=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',text)]; n=(n+[0,0,1.5])[:3]
            return MissionCommand(action=ActionName.GOTO,x_m=n[0],y_m=n[1],z_m=n[2],reason='절대 좌표',source_text=text)
        dirs={'앞':(v,0,0),'뒤':(-v,0,0),'왼':(0,v,0),'오른':(0,-v,0),'위':(0,0,v),'아래':(0,0,-v)}
        for k,(x,y,z) in dirs.items():
            if k in text: return MissionCommand(action=ActionName.MOVE_RELATIVE,x_m=x,y_m=y,z_m=z,reason=k+' 방향',source_text=text)
        return MissionCommand(action=ActionName.EMERGENCY_STOP,reason='해석 불가',source_text=text)
