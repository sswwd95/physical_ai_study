from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "digital_twin_sensor_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/digital_twin_sensor_stream.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE)

temp = sensor_df["temp_sensor_a_c"].interpolate(limit_direction="both")
pressure = sensor_df["pressure_sensor_a_pa"].interpolate(limit_direction="both")

state = np.array([temp.iloc[0], pressure.iloc[0]], dtype=float)
state_covariance = np.eye(2)
transition = np.eye(2)
observation = np.eye(2)
process_covariance = np.diag([0.02, 0.01])
measurement_covariance = np.diag([0.45**2, 0.18**2])

estimated_states = []

for temp_value, pressure_value in zip(temp, pressure):
    state = transition @ state
    state_covariance = (
        transition @ state_covariance @ transition.T
        + process_covariance
    )

    measurement = np.array([temp_value, pressure_value])
    innovation = measurement - observation @ state
    innovation_covariance = (
        observation @ state_covariance @ observation.T
        + measurement_covariance
    )

    kalman_gain = (
        state_covariance
        @ observation.T
        @ np.linalg.inv(innovation_covariance)
    )

    state = state + kalman_gain @ innovation
    state_covariance = (
        np.eye(2) - kalman_gain @ observation
    ) @ state_covariance

    estimated_states.append(state.copy())

estimated_states = np.vstack(estimated_states)

sensor_df["estimated_temperature_c"] = estimated_states[:, 0]
sensor_df["estimated_pressure_pa"] = estimated_states[:, 1]

print(
    sensor_df[
        ["estimated_temperature_c", "estimated_pressure_pa"]
    ].head()
)
