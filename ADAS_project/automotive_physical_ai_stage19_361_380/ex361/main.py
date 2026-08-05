try:
    import gymnasium as gym
except ImportError:
    print("Install gymnasium using environment.yml")
else:
    print("Gymnasium version:", gym.__version__)
    print("Environment components: observation, action, reward, termination")
