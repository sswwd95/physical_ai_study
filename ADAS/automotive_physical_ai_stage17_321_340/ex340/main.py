import json,pandas as pd
from common.path_tracking import *
path=load_path("path_sine.csv")
def pp(path,x,y,yaw,speed): return pure_pursuit_control(path,x,y,yaw,speed,.8)
def st(path,x,y,yaw,speed): return stanley_control(path,x,y,yaw,speed,1.2)
pp_df=simulate_tracker(path,pp,.6,23)
st_df=simulate_tracker(path,st,.6,23)
pp_path=output_path("ex340_pure_pursuit_log.csv"); pp_df.to_csv(pp_path,index=False,encoding="utf-8-sig")
st_path=output_path("ex340_stanley_log.csv"); st_df.to_csv(st_path,index=False,encoding="utf-8-sig")
comparison=pd.DataFrame([
    {"controller":"pure_pursuit",**tracking_metrics(pp_df)},
    {"controller":"stanley",**tracking_metrics(st_df)}
])
cmp_path=output_path("ex340_comparison.csv"); comparison.to_csv(cmp_path,index=False,encoding="utf-8-sig")
best=comparison.sort_values("rmse_cte_m").iloc[0]
report={
    "recommended_controller":str(best["controller"]),
    "recommended_rmse_cte_m":float(best["rmse_cte_m"]),
    "pure_pursuit":tracking_metrics(pp_df),
    "stanley":tracking_metrics(st_df)
}
json_path=output_path("ex340_integrated_report.json")
json_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(report)
print(pp_path,st_path,cmp_path,json_path)
