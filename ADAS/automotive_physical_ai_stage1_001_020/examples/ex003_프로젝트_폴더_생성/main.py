from pathlib import Path

root = Path.home() / "auto_physical_ai"
for name in ["data/raw", "data/processed", "models", "logs", "notebooks", "src", "reports"]:
    (root / name).mkdir(parents=True, exist_ok=True)
    print("created:", root / name)
