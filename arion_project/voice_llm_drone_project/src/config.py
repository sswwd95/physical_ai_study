from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]
def load_config(path=None):
    p = Path(path) if path else ROOT/'config'/'project.yaml'
    return yaml.safe_load(p.read_text(encoding='utf-8'))
def result_dir():
    p = ROOT/'results'; p.mkdir(exist_ok=True); return p
