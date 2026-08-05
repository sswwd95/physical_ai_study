from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"

def output_path(name):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def save_json(data, name):
    p = output_path(name)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return p

def normalize(value, low, high):
    return 2.0 * (value - low) / (high - low) - 1.0

def denormalize(value, low, high):
    return low + (value + 1.0) * 0.5 * (high - low)

def seed_everything(seed=42):
    return np.random.default_rng(seed)
