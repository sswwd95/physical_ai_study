from pathlib import Path
import numpy as np
import mujoco
import pymc as pm

xml = Path(__file__).resolve().parents[2] / "common" / "minimal_car.xml"
model = mujoco.MjModel.from_xml_path(str(xml))
data = mujoco.MjData(model)
values = []
for _ in range(50):
    mujoco.mj_step(model, data)
    values.append(float(data.sensordata[2]))
values = np.asarray(values)
with pm.Model():
    mu = pm.Normal("mu", mu=-9.81, sigma=2.0)
    sigma = pm.HalfNormal("sigma", sigma=1.0)
    pm.Normal("acc_z", mu=mu, sigma=sigma + 1e-6, observed=values)
    idata = pm.sample(300, tune=300, chains=2, cores=1, random_seed=42, progressbar=False)
print("samples:", len(values))
print("acc_z observed mean:", values.mean())
print("posterior mu mean:", float(idata.posterior["mu"].mean()))
print("INTEGRATED TEST PASS")
