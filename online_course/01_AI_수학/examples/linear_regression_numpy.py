"""NumPy로 정규방정식 기반 선형회귀를 구현하는 최소 예제."""
import numpy as np


def add_bias(x: np.ndarray) -> np.ndarray:
    return np.c_[np.ones(len(x)), x]


def fit_normal_equation(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    design = add_bias(x)
    return np.linalg.pinv(design) @ y


def predict(x: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return add_bias(x) @ weights


if __name__ == "__main__":
    x = np.array([[1.0], [2.0], [3.0], [4.0], [5.0]])
    y = np.array([2.2, 3.9, 6.1, 7.8, 10.2])

    w = fit_normal_equation(x, y)
    y_hat = predict(x, w)

    print("weights:", w)
    print("predictions:", np.round(y_hat, 3))
