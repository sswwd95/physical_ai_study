try:
    import stable_baselines3 as sb3
except ImportError:
    print("Install stable-baselines3 using environment.yml")
else:
    print("Stable-Baselines3:",sb3.__version__)
