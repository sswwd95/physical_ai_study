import importlib

packages = ["numpy", "pandas", "matplotlib", "mujoco", "pymc", "arviz"]
for name in packages:
    module = importlib.import_module(name)
    print(f"{name:12s} {getattr(module, '__version__', 'unknown')}")
