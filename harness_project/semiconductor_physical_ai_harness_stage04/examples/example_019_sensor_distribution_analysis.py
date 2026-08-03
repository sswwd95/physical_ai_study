"""
반도체 Physical AI 하네스 엔지니어링 실습 016~020
Windows 10 / Anaconda / Pandas / Matplotlib
"""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data'/'equipment_sensor_log.csv',parse_dates=['timestamp'])
sensors=['temperature_c','pressure_kpa','gas_flow_sccm','vibration_rms','motor_current_a']; rows=[]
for sensor in sensors:
    x=df[sensor].dropna(); rows.append({'sensor':sensor,'count':int(x.count()),'mean':float(x.mean()),'median':float(x.median()),'std':float(x.std()),'skewness':float(x.skew()),'kurtosis':float(x.kurt()),'q01':float(x.quantile(.01)),'q99':float(x.quantile(.99))})
    plt.figure(figsize=(8,5)); plt.hist(x,bins=30,edgecolor='black',alpha=.8); plt.title(f'Distribution: {sensor}'); plt.xlabel(sensor); plt.ylabel('Frequency'); plt.grid(True,axis='y',alpha=.3); plt.tight_layout(); plt.savefig(ROOT/'outputs'/f'distribution_{sensor}.png',dpi=150); plt.close()
s=pd.DataFrame(rows); s.to_csv(ROOT/'outputs'/'sensor_distribution_summary.csv',index=False,encoding='utf-8-sig'); print(s.round(4))
