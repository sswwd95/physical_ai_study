from pathlib import Path
import json
import logging
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "operations_stream.csv"
CONFIG_FILE = ROOT / "config" / "app_config.json"
OUTPUT_DIR = ROOT / "outputs"
LOG_DIR = ROOT / "logs"
MODEL_DIR = ROOT / "models"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

from datetime import datetime
artifacts=[]
for path in sorted(OUTPUT_DIR.glob("*")):
    if path.is_file():
        artifacts.append({
            "file":path.name,
            "size_bytes":path.stat().st_size,
            "modified_time":datetime.fromtimestamp(path.stat().st_mtime).isoformat()
        })
manifest={
    "run_id":datetime.now().strftime("RUN_%Y%m%d_%H%M%S"),
    "input_file":str(DATA_FILE.relative_to(ROOT)),
    "artifact_count":len(artifacts),
    "artifacts":artifacts
}
manifest_file=OUTPUT_DIR/"ex378_run_manifest.json"
manifest_file.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
print(manifest_file.read_text(encoding="utf-8"))
