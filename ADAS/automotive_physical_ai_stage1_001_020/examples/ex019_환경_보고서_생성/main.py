from pathlib import Path
import platform, sys
import mujoco, pymc, numpy, pandas, arviz

lines = [
    f"OS={platform.platform()}", f"Python={sys.version}",
    f"MuJoCo={mujoco.__version__}", f"PyMC={pymc.__version__}",
    f"NumPy={numpy.__version__}", f"Pandas={pandas.__version__}", f"ArviZ={arviz.__version__}",
]
path = Path(__file__).resolve().parents[2] / "environment_report.txt"
path.write_text("\n".join(lines), encoding="utf-8")
print(path.read_text(encoding="utf-8"))
