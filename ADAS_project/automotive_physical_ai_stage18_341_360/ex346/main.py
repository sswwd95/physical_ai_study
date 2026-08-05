import pandas as pd
from common.safety_utils import braking_distance,output_path
rows=[]
for mu in [.4,.5,.6,.7,.8,.9]:
    for speed in [5,10,15]:
        rows.append({"friction":mu,"speed_mps":speed,"braking_distance_m":braking_distance(speed,mu)})
r=pd.DataFrame(rows)
p=output_path("ex346_friction_braking_distance.csv"); r.to_csv(p,index=False,encoding="utf-8-sig")
print(r)
