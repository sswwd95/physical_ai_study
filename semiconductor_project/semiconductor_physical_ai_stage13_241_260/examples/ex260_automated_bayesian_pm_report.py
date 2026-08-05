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
    alpha=pm.HalfNormal("alpha",3); beta=pm.HalfNormal("beta",150); pm.Weibull("life",alpha=alpha,beta=beta,observed=obs)
    median=pm.Deterministic("median_lifetime",beta*(np.log(2))**(1/alpha))
    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)
summary=az.summary(idata,var_names=["alpha","beta","median_lifetime"],hdi_prob=.94)
a=idata.posterior["alpha"].values.ravel(); b=idata.posterior["beta"].values.ravel()
risk=[]
for _,r in life_df.iterrows():
    t=r["observed_cycles"]; p=1-np.exp(-(((t+20)/b)**a-(t/b)**a))
    risk.append({"equipment_id":r["equipment_id"],"failure_next_20":p.mean(),"observed_cycles":t})
risk_df=pd.DataFrame(risk).sort_values("failure_next_20",ascending=False)
decision_df=risk_df.copy(); decision_df["expected_failure_cost"]=decision_df["failure_next_20"]*5000; decision_df["maintenance_cost"]=1200; decision_df["recommended_action"]=np.where(decision_df["expected_failure_cost"]>1200,"maintenance","monitor")
rul_latest=rul_df.sort_values("cycle").groupby("equipment_id").tail(1)[["equipment_id","cycle","rul_cycles"]]
with pd.ExcelWriter(OUTPUT_DIR/"ex260_bayesian_pm_report.xlsx",engine="openpyxl") as w:
    summary.to_excel(w,sheet_name="lifetime_summary")
    risk_df.to_excel(w,sheet_name="failure_risk",index=False)
    rul_latest.to_excel(w,sheet_name="rul_latest",index=False)
    decision_df.to_excel(w,sheet_name="decision_analysis",index=False)
print("보고서 저장 완료")
