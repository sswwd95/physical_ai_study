import json,arviz as az,matplotlib.pyplot as plt,pandas as pd,pymc as pm
from .config import load_config,result_dir
def main():
 c=load_config(); d=pd.read_csv(result_dir()/'flight_log.csv'); lat=d.pipeline_latency_ms.dropna().to_numpy(); suc=d.detected.astype(bool).astype(int).to_numpy(); r=c['report']
 with pm.Model() as m1:
  mu=pm.Normal('mu',mu=float(lat.mean()),sigma=50); sig=pm.HalfNormal('sigma',50); pm.Normal('obs',mu=mu,sigma=sig,observed=lat); t1=pm.sample(draws=r['draws'],tune=r['tune'],chains=2,cores=1,random_seed=r['seed'],progressbar=False)
 az.plot_posterior(t1,var_names=['mu','sigma'],hdi_prob=.94); plt.tight_layout(); plt.savefig(result_dir()/'latency_posterior.png',dpi=150); plt.close()
 with pm.Model() as m2:
  p=pm.Beta('tracking_rate',1,1); pm.Bernoulli('obs',p=p,observed=suc); t2=pm.sample(draws=r['draws'],tune=r['tune'],chains=2,cores=1,random_seed=r['seed'],progressbar=False)
 az.plot_posterior(t2,var_names=['tracking_rate'],hdi_prob=.94); plt.tight_layout(); plt.savefig(result_dir()/'tracking_rate_posterior.png',dpi=150); plt.close(); ms=t1.posterior['mu'].values.ravel(); ps=t2.posterior['tracking_rate'].values.ravel(); out={'frames':len(d),'mean_fps':float(d.fps.mean()),'mean_pipeline_latency_ms':float(d.pipeline_latency_ms.mean()),'latency_posterior_mean_ms':float(ms.mean()),'latency_hdi_94':[float(x) for x in az.hdi(ms,hdi_prob=.94)],'tracking_rate_posterior_mean':float(ps.mean()),'tracking_rate_hdi_94':[float(x) for x in az.hdi(ps,hdi_prob=.94)],'safety_interventions':int(d.safety_active.astype(bool).sum()),'search_frames':int((d.state=='SEARCH').sum())}; (result_dir()/'analysis_summary.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':main()
