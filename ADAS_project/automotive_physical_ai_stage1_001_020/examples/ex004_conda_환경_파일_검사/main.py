from pathlib import Path

path = Path(__file__).resolve().parents[2] / "environment.yml"
text = path.read_text(encoding="utf-8")
print(text)
for token in ["python=3.11", "mujoco==3.6.0", "pymc", "arviz"]:
    print(token, "->", "OK" if token in text else "MISSING")
