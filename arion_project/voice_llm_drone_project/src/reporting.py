import json, pandas as pd
from .config import result_dir
def read(p): return json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
def main():
    out=result_dir(); df=pd.read_csv(out/'mission_log.csv'); mission=read(out/'mission_summary.json'); bayes=read(out/'bayesian_summary.json')
    table=df.groupby('action').agg(count=('action','size'),success_rate=('success',lambda s:s.astype(str).str.lower().eq('true').mean()),mean_latency_ms=('planning_latency_ms','mean')).reset_index().to_markdown(index=False)
    text=f'''# 음성 LLM 자연어 드론 실습 결과 보고서\n\n## 전체 결과\n- 모델: {mission.get('model_source')}\n- 명령 수: {mission.get('total_commands')}\n- 성공률: {mission.get('success_rate')}\n- 안전 개입: {mission.get('safety_interventions')}\n\n## 명령별 집계\n{table}\n\n## 베이지안 분석\n- 계획 지연 사후평균(ms): {bayes.get('latency_mean_posterior_ms','분석 미실행')}\n- 계획 지연 94% HDI: {bayes.get('latency_mu_hdi_94','분석 미실행')}\n- 성공률 사후평균: {bayes.get('success_rate_posterior_mean','분석 미실행')}\n- 성공률 94% HDI: {bayes.get('success_rate_hdi_94','분석 미실행')}\n\n## 안전 검토\nLLM 출력은 직접 actuator에 연결하지 않고 스키마 검증과 안전 감독기를 통과시켰다.\n'''
    (out/'final_report.md').write_text(text,encoding='utf-8'); print(out/'final_report.md')
if __name__=='__main__': main()
