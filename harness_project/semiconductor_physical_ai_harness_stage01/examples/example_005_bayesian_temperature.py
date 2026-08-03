"""
반도체 Physical AI 하네스 엔지니어링 실습
Windows 10 / Anaconda / PyMC
"""

from pathlib import Path
import arviz as az
import pandas as pd
import pymc as pm

PROJECT_ROOT = Path(__file__).resolve().parents[1]
csv_path = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
summary_path = PROJECT_ROOT / "outputs" / "bayesian_temperature_summary.csv"

# 1. 장비 온도 데이터를 읽고 초기 정상 구간 200개를 선택한다.
df = pd.read_csv(csv_path, parse_dates=["timestamp"])
observed_temperature = df["temperature_c"].iloc[:200].to_numpy()

# 2. 베이지안 모델을 정의한다.
with pm.Model() as model:
    # 정상 평균 온도에 대한 사전 믿음이다.
    mu = pm.Normal("mu", mu=65.0, sigma=5.0)

    # 온도 변동 폭은 양수여야 하므로 HalfNormal 분포를 사용한다.
    sigma = pm.HalfNormal("sigma", sigma=2.0)

    # 관측 온도가 평균 mu와 표준편차 sigma를 따른다고 가정한다.
    pm.Normal(
        "temperature_obs",
        mu=mu,
        sigma=sigma,
        observed=observed_temperature,
    )

    # 사후분포를 MCMC로 추정한다.
    trace = pm.sample(
        draws=1000,
        tune=1000,
        chains=2,
        cores=1,
        random_seed=42,
        progressbar=True,
    )

# 3. 평균과 변동 폭의 사후분포를 요약한다.
summary = az.summary(trace, var_names=["mu", "sigma"], hdi_prob=0.95)
summary.to_csv(summary_path, encoding="utf-8-sig")

# 4. 공정 관리에 필요한 해석 정보를 출력한다.
mu_mean = float(summary.loc["mu", "mean"])
mu_hdi_low = float(summary.loc["mu", "hdi_2.5%"])
mu_hdi_high = float(summary.loc["mu", "hdi_97.5%"])

print(summary)
print(
    f"[해석] 정상 평균 온도 추정값은 약 {mu_mean:.3f}°C이며, "
    f"95% HDI는 {mu_hdi_low:.3f}~{mu_hdi_high:.3f}°C입니다."
)
print(f"[완료] 요약 저장: {summary_path}")
