import json, arviz as az, matplotlib.pyplot as plt, pandas as pd, pymc as pm
from .config import load_config,result_dir
def main():
    cfg=load_config()['report']; out=result_dir(); df=pd.read_csv(out/'mission_log.csv'); latency=df.planning_latency_ms.dropna().to_numpy(float); success=df.success.astype(str).str.lower().eq('true').astype(int).to_numpy()
    with pm.Model() as m:
        mu=pm.Normal('mu',mu=max(float(latency.mean()),1),sigma=100); sigma=pm.HalfNormal('sigma',sigma=100); pm.Normal('obs',mu=mu,sigma=sigma,observed=latency)
        tr=pm.sample(draws=cfg['draws'],tune=cfg['tune'],chains=2,cores=1,random_seed=cfg['random_seed'],progressbar=False)
    az.plot_posterior(tr,var_names=['mu','sigma'],hdi_prob=.94); plt.tight_layout(); plt.savefig(out/'pymc_latency.png',dpi=150); plt.close()
    with pm.Model() as m2:
        rate=pm.Beta('success_rate',1,1); pm.Bernoulli('obs',p=rate,observed=success); tr2=pm.sample(draws=cfg['draws'],tune=cfg['tune'],chains=2,cores=1,random_seed=cfg['random_seed'],progressbar=False)
    az.plot_posterior(tr2,var_names=['success_rate'],hdi_prob=.94); plt.tight_layout(); plt.savefig(out/'pymc_success_rate.png',dpi=150); plt.close()
    mus=tr.posterior['mu'].values.ravel(); rates=tr2.posterior['success_rate'].values.ravel(); s={'latency_mean_posterior_ms':float(mus.mean()),'latency_mu_hdi_94':[float(x) for x in az.hdi(mus,hdi_prob=.94)],'success_rate_posterior_mean':float(rates.mean()),'success_rate_hdi_94':[float(x) for x in az.hdi(rates,hdi_prob=.94)],'observations':len(df)}
    (out/'bayesian_summary.json').write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8'); print(s)
if __name__=='__main__': main()
