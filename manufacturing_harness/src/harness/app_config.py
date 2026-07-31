from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class SimulationConfig:
    model_path: Path
    timestep: float
    control_frequency: int
    episode_seconds: float
    render: bool


@dataclass(frozen=True)
class SensorThresholdConfig:
    temperature_warning: float
    temperature_critical: float
    vibration_warning: float
    vibration_critical: float
    current_warning: float
    current_critical: float


@dataclass(frozen=True)
class ProductionConfig:
    target_count_per_hour: int
    maximum_defect_rate: float
    target_cycle_time_seconds: float


@dataclass(frozen=True)
class PathConfig:
    raw_data: Path
    processed_data: Path
    results: Path
    logs: Path
    models: Path
    reports: Path


@dataclass(frozen=True)
class ReinforcementLearningConfig:
    algorithm: str
    total_timesteps: int
    learning_rate: float
    batch_size: int
    device: str


@dataclass(frozen=True)
class AppConfig:
    project_name: str
    environment: str
    seed: int
    simulation: SimulationConfig
    sensor_thresholds: SensorThresholdConfig
    production: ProductionConfig
    paths: PathConfig
    reinforcement_learning: ReinforcementLearningConfig


def build_app_config(
    raw_config: dict[str, Any],
    project_root: Path,
) -> AppConfig:
    """검증된 설정 딕셔너리를 AppConfig로 변환한다."""

    simulation = raw_config["simulation"]
    sensors = raw_config["sensors"]
    production = raw_config["production"]
    paths = raw_config["paths"]
    rl = raw_config["reinforcement_learning"]

    return AppConfig(
        project_name=raw_config["project"]["name"],
        environment=raw_config["project"]["environment"],
        seed=int(raw_config["experiment"]["seed"]),
        simulation=SimulationConfig(
            model_path=(
                project_root
                / simulation["model_path"]
            ).resolve(),
            timestep=float(simulation["timestep"]),
            control_frequency=int(
                simulation["control_frequency"]
            ),
            episode_seconds=float(
                simulation["episode_seconds"]
            ),
            render=bool(simulation["render"]),
        ),
        sensor_thresholds=SensorThresholdConfig(
            temperature_warning=float(
                sensors["temperature"]["warning_limit"]
            ),
            temperature_critical=float(
                sensors["temperature"]["critical_limit"]
            ),
            vibration_warning=float(
                sensors["vibration"]["warning_limit"]
            ),
            vibration_critical=float(
                sensors["vibration"]["critical_limit"]
            ),
            current_warning=float(
                sensors["motor_current"]["warning_limit"]
            ),
            current_critical=float(
                sensors["motor_current"]["critical_limit"]
            ),
        ),
        production=ProductionConfig(
            target_count_per_hour=int(
                production["target_count_per_hour"]
            ),
            maximum_defect_rate=float(
                production["maximum_defect_rate"]
            ),
            target_cycle_time_seconds=float(
                production["target_cycle_time_seconds"]
            ),
        ),
        paths=PathConfig(
            raw_data=(
                project_root / paths["raw_data"]
            ).resolve(),
            processed_data=(
                project_root / paths["processed_data"]
            ).resolve(),
            results=(
                project_root / paths["results"]
            ).resolve(),
            logs=(
                project_root / paths["logs"]
            ).resolve(),
            models=(
                project_root / paths["models"]
            ).resolve(),
            reports=(
                project_root / paths["reports"]
            ).resolve(),
        ),
        reinforcement_learning=(
            ReinforcementLearningConfig(
                algorithm=str(rl["algorithm"]),
                total_timesteps=int(
                    rl["total_timesteps"]
                ),
                learning_rate=float(
                    rl["learning_rate"]
                ),
                batch_size=int(rl["batch_size"]),
                device=str(rl["device"]),
            )
        ),
    )