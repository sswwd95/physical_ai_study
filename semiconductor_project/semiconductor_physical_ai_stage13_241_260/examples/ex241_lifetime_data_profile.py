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

print("수명 데이터 크기:", life_df.shape)
print("RUL 스냅샷 크기:", rul_df.shape)
print("\n검열 분포:")
print(life_df["event_observed"].value_counts())
print("\n챔버별 관측 수명:")
print(life_df.groupby("chamber_type")["observed_cycles"].describe().round(2))
