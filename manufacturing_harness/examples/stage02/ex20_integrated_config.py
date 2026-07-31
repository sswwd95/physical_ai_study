from pathlib import Path

from src.harness.configuration_harness import (
    ConfigurationHarness,
)


if __name__ == "__main__":
    project_root = Path.cwd()

    harness = ConfigurationHarness(
        project_root=project_root
    )

    app_config = harness.load(
        base_config_path=Path(
            "configs/base.yaml"
        ),
        environment_config_path=Path(
            "configs/development.yaml"
        ),
        env_file_path=Path(".env"),
    )

    print("=" * 60)
    print("설정 하네스 검증 완료")
    print("=" * 60)

    print(
        f"프로젝트: {app_config.project_name}"
    )

    print(
        f"실행 환경: {app_config.environment}"
    )

    print(
        f"랜덤 시드: {app_config.seed}"
    )

    print(
        "MuJoCo 모델: "
        f"{app_config.simulation.model_path}"
    )

    print(
        "물리 시간 간격: "
        f"{app_config.simulation.timestep}초"
    )

    print(
        "제어 주기: "
        f"{app_config.simulation.control_frequency}Hz"
    )

    print(
        "온도 위험 기준: "
        f"{app_config.sensor_thresholds.temperature_critical}℃"
    )

    print(
        "허용 불량률: "
        f"{app_config.production.maximum_defect_rate:.2%}"
    )

    print(
        "강화학습 알고리즘: "
        f"{app_config.reinforcement_learning.algorithm}"
    )

#2단계 통합 확인 코드
from pathlib import Path

from src.harness.configuration_harness import (
    ConfigurationHarness,
)


def run_configuration_check() -> dict[str, object]:
    project_root = Path.cwd()

    config_harness = ConfigurationHarness(
        project_root=project_root,
    )

    app_config = config_harness.load(
        base_config_path=Path(
            "configs/base.yaml"
        ),
        environment_config_path=Path(
            "configs/development.yaml"
        ),
        env_file_path=Path(".env"),
    )

    physics_frequency = (
        1.0
        / app_config.simulation.timestep
    )

    physics_steps_per_control = round(
        physics_frequency
        / app_config.simulation.control_frequency
    )

    panda_model_exists = (
        app_config.simulation.model_path.exists()
    )

    return {
        "project_name": app_config.project_name,
        "environment": app_config.environment,
        "seed": app_config.seed,
        "physics_frequency_hz": physics_frequency,
        "control_frequency_hz": (
            app_config.simulation.control_frequency
        ),
        "physics_steps_per_control": (
            physics_steps_per_control
        ),
        "panda_model_exists": panda_model_exists,
        "temperature_critical": (
            app_config
            .sensor_thresholds
            .temperature_critical
        ),
        "maximum_defect_rate": (
            app_config
            .production
            .maximum_defect_rate
        ),
    }


if __name__ == "__main__":
    results = run_configuration_check()

    for key, value in results.items():
        print(f"{key}: {value}")