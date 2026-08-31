"""가상의 센서 시계열 데이터를 Matplotlib으로 시각화하는 예제."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    t = np.linspace(0, 10, 200)
    sensor = np.sin(t) + 0.1 * np.cos(5 * t)

    plt.plot(t, sensor)
    plt.xlabel("time")
    plt.ylabel("sensor value")
    plt.title("Sensor signal")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
