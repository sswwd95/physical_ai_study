import json,pandas as pd
from .config import result_dir
def main():
 rd=result_dir(); d=pd.read_csv(rd/'flight_log.csv'); s=json.loads((rd/'analysis_summary.json').read_text(encoding='utf-8')); st=d.groupby('state').size().reset_index(name='frames'); txt=f'''# 추적 비행 결과 보고서

- 전체 프레임: {s['frames']}
- 평균 FPS: {s['mean_fps']:.2f}
- 평균 지연: {s['mean_pipeline_latency_ms']:.3f} ms
- 지연 사후평균: {s['latency_posterior_mean_ms']:.3f} ms
- 지연 94% HDI: {s['latency_hdi_94']}
- 추적 성공률 사후평균: {s['tracking_rate_posterior_mean']:.4f}
- 추적 성공률 94% HDI: {s['tracking_rate_hdi_94']}
- 안전거리 개입: {s['safety_interventions']}
- 재탐색 프레임: {s['search_frames']}

## 상태별 결과
{st.to_markdown(index=False)}
''' ; (rd/'final_report.md').write_text(txt,encoding='utf-8')
if __name__=='__main__':main()
