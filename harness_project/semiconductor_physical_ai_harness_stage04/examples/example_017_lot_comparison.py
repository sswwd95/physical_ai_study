"""
반도체 Physical AI 하네스 엔지니어링 실습 016~020
Windows 10 / Anaconda / Pandas / Matplotlib
"""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data'/'equipment_sensor_log.csv',parse_dates=['timestamp'])
cols=['temperature_c','pressure_kpa','gas_flow_sccm','vibration_rms','motor_current_a','quality_score','defect_flag']
s=df.groupby('lot_id')[cols].agg(['mean','std','min','max']); s.columns=[f'{a}_{b}' for a,b in s.columns]; s=s.reset_index()
s.to_csv(ROOT/'outputs'/'lot_comparison_summary.csv',index=False,encoding='utf-8-sig')
names=sorted(df.lot_id.unique()); data=[df.loc[df.lot_id==x,'temperature_c'].to_numpy() for x in names]
plt.figure(figsize=(8,5)); plt.boxplot(data,tick_labels=names); plt.title('Temperature Distribution by Lot'); plt.xlabel('Lot'); plt.ylabel('Temperature (°C)'); plt.grid(True,axis='y',alpha=.3); plt.tight_layout(); plt.savefig(ROOT/'outputs'/'lot_temperature_comparison.png',dpi=150); plt.close()
print(s.round(3))
