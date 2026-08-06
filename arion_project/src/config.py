from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
def load_config():
    return yaml.safe_load((ROOT/'config'/'project.yaml').read_text(encoding='utf-8'))
def result_dir():
    p=ROOT/'results'; p.mkdir(exist_ok=True); return p
