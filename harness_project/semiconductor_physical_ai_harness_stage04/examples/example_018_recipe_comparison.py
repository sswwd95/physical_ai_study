"""
반도체 Physical AI 하네스 엔지니어링 실습 016~020
Windows 10 / Anaconda / Pandas / Matplotlib
"""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data'/'equipment_sensor_log.csv',parse_dates=['timestamp'])
s=df.groupby('recipe_id').agg(row_count=('timestamp','size'),mean_quality_score=('quality_score','mean'),std_quality_score=('quality_score','std'),defect_count=('defect_flag','sum'),mean_temperature_c=('temperature_c','mean'),mean_pressure_kpa=('pressure_kpa','mean'),mean_gas_flow_sccm=('gas_flow_sccm','mean')).reset_index()
s['defect_rate_percent']=s.defect_count/s.row_count*100
s.to_csv(ROOT/'outputs'/'recipe_comparison_summary.csv',index=False,encoding='utf-8-sig')
plt.figure(figsize=(8,5)); plt.bar(s.recipe_id,s.mean_quality_score); plt.title('Mean Quality Score by Recipe'); plt.xlabel('Recipe'); plt.ylabel('Mean Quality Score'); plt.grid(True,axis='y',alpha=.3); plt.tight_layout(); plt.savefig(ROOT/'outputs'/'recipe_quality_comparison.png',dpi=150); plt.close(); print(s.round(3))
