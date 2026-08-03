from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
LIFE_FILE = ROOT / "data" / "bayesian_equipment_lifetime.csv"
RUL_FILE = ROOT / "data" / "bayesian_rul_snapshots.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

life_df = pd.read_csv(LIFE_FILE)
rul_df = pd.read_csv(RUL_FILE)

obs=life_df.loc[life_df["event_observed"]==1,"observed_cycles"].to_numpy()
with pm.Model() as model:
    alpha=pm.HalfNormal("alpha",3); beta=pm.HalfNormal("beta",150)
    pm.Weibull("lifetime",alpha=alpha,beta=beta,observed=obs)
    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)
a=idata.posterior["alpha"].values.ravel(); b=idata.posterior["beta"].values.ravel()
rows=[]
for _,r in life_df.iterrows():
    t=r["observed_cycles"]
    cond=1-np.exp(-(((t+20)/b)**a-(t/b)**a))
    rows.append({"equipment_id":r["equipment_id"],"observed_cycles":t,"failure_next_20_mean":cond.mean()})
out=pd.DataFrame(rows).sort_values("failure_next_20_mean",ascending=False)
print(out.head(10).round(4)); out.to_csv(OUTPUT_DIR/"ex252_failure_risk.csv",index=False,encoding="utf-8-sig")
