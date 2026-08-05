import numpy as np

def make_data(seed: int):
    return np.random.default_rng(seed).normal(1.0, 0.1, 5)

a = make_data(123)
b = make_data(123)
print("a:", a)
print("b:", b)
print("same:", np.allclose(a, b))
assert np.allclose(a, b)
