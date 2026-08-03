"""
반도체 Physical AI 하네스 엔지니어링 실습 016~020
Windows 10 / Anaconda / Pandas / Matplotlib
"""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data'/'equipment_sensor_log.csv',parse_dates=['timestamp'])
total=len(df); lots=df.lot_id.nunique(); recipes=df.recipe_id.nunique(); defects=int(df.defect_flag.sum()); rate=defects/total*100; quality=float(df.quality_score.mean())
s=df.groupby('lot_id').agg(row_count=('timestamp','size'),mean_quality=('quality_score','mean'),defect_count=('defect_flag','sum'),mean_temperature=('temperature_c','mean'),mean_vibration=('vibration_rms','mean')).reset_index(); s['defect_rate_percent']=s.defect_count/s.row_count*100
table=s.round(3).to_html(index=False,border=0,classes='summary-table')
page=f"""<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><title>반도체 공정 기초 대시보드</title><style>body{{font-family:Arial,sans-serif;margin:30px;background:#f4f6f8}}.kpi-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}}.kpi,.panel{{background:white;border-radius:10px;padding:18px;box-shadow:0 2px 8px #0002}}.value{{font-size:26px;font-weight:bold}}table{{border-collapse:collapse;width:100%}}th,td{{padding:10px;border-bottom:1px solid #ddd;text-align:right}}th:first-child,td:first-child{{text-align:left}}</style></head><body><h1>반도체 Physical AI 기초 공정 대시보드</h1><p>합성 센서 데이터 기반 교육용 요약</p><div class="kpi-grid"><div class="kpi">전체 행<div class="value">{total}</div></div><div class="kpi">Lot 수<div class="value">{lots}</div></div><div class="kpi">Recipe 수<div class="value">{recipes}</div></div><div class="kpi">평균 품질<div class="value">{quality:.2f}</div></div><div class="kpi">불량률<div class="value">{rate:.2f}%</div></div></div><div class="panel"><h2>Lot별 상태 요약</h2>{table}</div><p>교육용 합성 데이터이며 실제 공정 승인이나 설비 제어 판단에 직접 사용할 수 없습니다.</p></body></html>"""
(ROOT/'outputs'/'basic_process_dashboard.html').write_text(page,encoding='utf-8'); print('[완료]',ROOT/'outputs'/'basic_process_dashboard.html')
