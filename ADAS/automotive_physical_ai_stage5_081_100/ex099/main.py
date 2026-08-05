import pandas as pd
from common.sync_utils import out
path_in=out("ex098_integrated_sensor_table.csv")
df=pd.read_csv(path_in)
report=pd.DataFrame({
    "column":df.columns,
    "missing_count":[df[c].isna().sum() for c in df.columns],
    "missing_ratio_pct":[df[c].isna().mean()*100 for c in df.columns],
})
path=out("ex099_sync_quality_report.csv")
report.to_csv(path,index=False)
print(report)
