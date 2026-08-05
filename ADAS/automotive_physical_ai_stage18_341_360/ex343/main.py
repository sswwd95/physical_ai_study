from common.safety_utils import load_data,ttc
df=load_data()
for row in df.iloc[[0,200,600,1000]].itertuples():
    print(row.time_s,ttc(row.distance_m,row.relative_speed_mps))
