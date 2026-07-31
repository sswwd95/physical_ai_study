# 실습 예제 12

from pathlib import Path
from pprint import pprint

from src.harness.config_loader import load_yaml


if __name__ == "__main__":
    config = load_yaml(
        Path("configs/base.yaml")
    )

    pprint(config)


# ------------------------------------------------------------

# 실습 예제 13
print("===============================================")

from pathlib import Path

from src.harness.config_loader import load_yaml
from src.harness.config_loader import get_config_value



if __name__ == "__main__":
    config = load_yaml(Path("configs/base.yaml"))

    temperature_limit = get_config_value(
        config,
        "sensors.temperature.critical_limit",
    )

    camera_enabled = get_config_value(
        config,
        "sensors.camera.enabled",
        default=False,
    )

    print(f"온도 위험 기준: {temperature_limit}")
    print(f"카메라 활성화: {camera_enabled}")

# ------------------------------------------------------------
# 실습 예제 14
print("===============================================")

from pathlib import Path

from src.harness.config_loader import load_yaml
from src.harness.config_validator import validate_config_type


if __name__ == "__main__":
    config = load_yaml(Path("configs/base.yaml"))

    validate_config_type(
        config,
        "experiment.seed",
        int,
    )

    validate_config_type(
        config,
        "simulation.timestep",
        float,
    )

    validate_config_type(
        config,
        "simulation.render",
        bool,
    )

    validate_config_type(
        config,
        "reinforcement_learning.algorithm",
        str,
    )

    print("설정 타입 검증 완료")
# ----------------------------------------------------------
# 실습 15 프로그램 실행 전에 필수 설정이 모두 있는지 확인
print("===============================================")

from pathlib import Path

from src.harness.config_loader import load_yaml
from src.harness.config_validator import (
    REQUIRED_CONFIG_KEYS,
    validate_required_keys,
)


if __name__ == "__main__":
    config = load_yaml(Path("configs/base.yaml"))

    validate_required_keys(
        config=config,
        required_keys=REQUIRED_CONFIG_KEYS,
    )

    print("필수 설정값 검증 완료")

# ----------------------------------------------------------
# 실습 16. 
print("===============================================")

from pathlib import Path
from pprint import pprint

from src.harness.config_loader import load_yaml
from src.harness.config_merge import deep_merge


if __name__ == "__main__":
    base_config = load_yaml(
        Path("configs/base.yaml")
    )

    development_config = load_yaml(
        Path("configs/development.yaml")
    )

    merged_config = deep_merge(
        base_config=base_config,
        override_config=development_config,
    )

    pprint(merged_config["simulation"])
    pprint(merged_config["reinforcement_learning"])

# ----------------------------------------------------------
# 실습 17
print("===============================================")
import os
from pathlib import Path

from dotenv import load_dotenv


def get_required_environment_variable(name: str) -> str:
    """필수 환경변수를 읽는다."""

    value = os.getenv(name)

    if value is None or not value.strip():
        raise EnvironmentError(
            f"필수 환경변수가 없습니다: {name}"
        )

    return value


def mask_secret(secret: str) -> str:
    """민감한 문자열의 일부만 표시한다."""

    if len(secret) <= 4:
        return "*" * len(secret)

    return (
        secret[:2]
        + "*" * (len(secret) - 4)
        + secret[-2:]
    )


if __name__ == "__main__":
    env_path = Path(".env")

    if not env_path.exists():
        raise FileNotFoundError(
            ".env 파일이 없습니다. "
            ".env.example을 복사해 .env를 생성하세요."
        )

    load_dotenv(
        dotenv_path=env_path,
        override=False,
    )

    environment_name = (
        get_required_environment_variable(
            "MANUFACTURING_ENV"
        )
    )

    database_user = (
        get_required_environment_variable(
            "MANUFACTURING_DB_USER"
        )
    )

    database_password = (
        get_required_environment_variable(
            "MANUFACTURING_DB_PASSWORD"
        )
    )

    print(f"실행 환경: {environment_name}")
    print(f"DB 사용자: {database_user}")
    print(
        "DB 비밀번호: "
        f"{mask_secret(database_password)}"
    )
# ----------------------------------------------------------
# 실습 18
print("===============================================")
from pathlib import Path

from src.harness.config_loader import (
    get_config_value,
    load_yaml,
    resolve_project_path
)


if __name__ == "__main__":
    project_root = Path.cwd()
    config = load_yaml(Path("configs/base.yaml"))

    configured_model_path = get_config_value(
        config,
        "simulation.model_path",
    )

    model_path = resolve_project_path(
        project_root=project_root,
        configured_path=configured_model_path,
        must_exist=False,
        expected_type="file",
    )

    results_directory = resolve_project_path(
        project_root=project_root,
        configured_path=get_config_value(
            config,
            "paths.results",
        ),
    )

    results_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    print(f"Panda 모델 경로: {model_path}")
    print(f"결과 저장 경로: {results_directory}")

# ----------------------------------------------------------
# 실습 19
print("===============================================")

from pathlib import Path
from pprint import pprint

from src.harness.app_config import build_app_config
from src.harness.config_loader import load_yaml


if __name__ == "__main__":
    project_root = Path.cwd()

    raw_config = load_yaml(
        Path("configs/base.yaml")
    )

    app_config = build_app_config(
        raw_config=raw_config,
        project_root=project_root,
    )

    pprint(app_config)

    print(
        "Panda 모델: "
        f"{app_config.simulation.model_path}"
    )

    print(
        "온도 위험 기준: "
        f"{app_config.sensor_thresholds.temperature_critical}"
    )
# ----------------------------------------------------------
# 실습 20
print("===============================================")


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