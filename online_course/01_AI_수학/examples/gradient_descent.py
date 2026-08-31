"""1차 선형회귀를 경사하강법으로 학습하는 예제."""
import numpy as np


def train(x: np.ndarray, y: np.ndarray, lr: float = 0.05, epochs: int = 1000):
    w = 0.0
    b = 0.0
    n = len(x)
    for _ in range(epochs):
        pred = w * x + b
        error = pred - y
        dw = (2 / n) * np.sum(error * x)
        db = (2 / n) * np.sum(error)
        w -= lr * dw
        b -= lr * db
    return w, b


if __name__ == "__main__":
    x = np.array([0., 1., 2., 3., 4.])
    y = np.array([1.0, 3.1, 4.9, 7.2, 9.0])
    w, b = train(x, y)
    print(f"y = {w:.3f}x + {b:.3f}")
