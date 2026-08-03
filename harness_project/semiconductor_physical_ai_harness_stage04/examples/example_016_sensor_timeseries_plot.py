"""
반도체 Physical AI 하네스 엔지니어링 실습 016~020
Windows 10 / Anaconda / Pandas / Matplotlib
"""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data'/'equipment_sensor_log.csv',parse_dates=['timestamp']).sort_values('timestamp')
sensors=['temperature_c','pressure_kpa','gas_flow_sccm','vibration_rms','motor_current_a']
for sensor in sensors:
    plt.figure(figsize=(12,4))
    plt.plot(df['timestamp'],df[sensor],linewidth=1.0)
    plt.title(f'Sensor Time Series: {sensor}')
    plt.xlabel('Timestamp'); plt.ylabel(sensor); plt.grid(True,alpha=.3); plt.tight_layout()
    out=ROOT/'outputs'/f'timeseries_{sensor}.png'; plt.savefig(out,dpi=150); plt.close(); print('[저장]',out)
print('[완료] 모든 센서 시계열 그래프를 생성했습니다.')
