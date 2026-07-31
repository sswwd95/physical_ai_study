from typing import Any

from src.harness.config_loader import get_config_value


def validate_config_type(
    config: dict[str, Any],
    key_path: str,
    expected_type: type,
    allow_integer_for_float: bool = True,
) -> None:
    """설정값이 기대한 데이터 타입인지 검사한다."""

    value = get_config_value(
        config=config,
        key_path=key_path,
    )

    if expected_type is int and isinstance(value, bool):
        raise TypeError(
            f"{key_path}는 int여야 하지만 bool입니다."
        )

    if expected_type is float:
        if isinstance(value, bool):
            raise TypeError(
                f"{key_path}는 float여야 하지만 bool입니다."
            )

        if allow_integer_for_float:
            valid = isinstance(value, (int, float))
        else:
            valid = isinstance(value, float)

    else:
        valid = isinstance(value, expected_type)

    if not valid:
        raise TypeError(
            f"{key_path}의 타입이 잘못되었습니다. "
            f"기대 타입={expected_type.__name__}, "
            f"실제 타입={type(value).__name__}, "
            f"실제 값={value!r}"
        )



# 실습 15. 필수 설정 누락 검사

REQUIRED_CONFIG_KEYS = [
    "project.name",
    "experiment.seed",
    "simulation.model_path",
    "simulation.timestep",
    "simulation.control_frequency",
    "sensors.temperature.critical_limit",
    "sensors.vibration.critical_limit",
    "production.target_count_per_hour",
    "production.maximum_defect_rate",
    "paths.results",
]


def validate_required_keys(
    config: dict[str, Any],
    required_keys: list[str],
) -> None:
    """필수 설정값이 모두 존재하는지 검사한다."""

    missing_keys: list[str] = []

    for key_path in required_keys:
        try:
            get_config_value(
                config=config,
                key_path=key_path,
            )
        except (KeyError, TypeError):
            missing_keys.append(key_path)

    if missing_keys:
        formatted_keys = "\n".join(
            f"  - {key}" for key in missing_keys
        )

        raise ValueError(
            "다음 필수 설정값이 누락되었습니다.\n"
            f"{formatted_keys}"
        )

# 실습 20. 설정값 범위 검증 추가
from typing import Any

from src.harness.config_loader import get_config_value


def validate_number_range(
    config: dict[str, Any],
    key_path: str,
    minimum: float | None = None,
    maximum: float | None = None,
    include_minimum: bool = True,
    include_maximum: bool = True,
) -> None:
    """숫자 설정값이 허용 범위 안에 있는지 검사한다."""

    value = get_config_value(
        config=config,
        key_path=key_path,
    )

    if isinstance(value, bool) or not isinstance(
        value,
        (int, float),
    ):
        raise TypeError(
            f"{key_path}는 숫자여야 합니다."
        )

    numeric_value = float(value)

    if minimum is not None:
        if include_minimum:
            minimum_valid = numeric_value >= minimum
        else:
            minimum_valid = numeric_value > minimum

        if not minimum_valid:
            operator = ">=" if include_minimum else ">"
            raise ValueError(
                f"{key_path}는 {operator} {minimum}이어야 "
                f"합니다. 실제 값={numeric_value}"
            )

    if maximum is not None:
        if include_maximum:
            maximum_valid = numeric_value <= maximum
        else:
            maximum_valid = numeric_value < maximum

        if not maximum_valid:
            operator = "<=" if include_maximum else "<"
            raise ValueError(
                f"{key_path}는 {operator} {maximum}이어야 "
                f"합니다. 실제 값={numeric_value}"
            )

# 실습 20. 추가 검증 : 경고 기준과 위험 기준 (위험 기준 > 경고 기준)
from typing import Any

from src.harness.config_loader import get_config_value


def validate_threshold_order(
    config: dict[str, Any],
    warning_key: str,
    critical_key: str,
) -> None:
    """경고 임계값이 위험 임계값보다 작은지 검사한다."""

    warning_value = float(
        get_config_value(config, warning_key)
    )

    critical_value = float(
        get_config_value(config, critical_key)
    )

    if warning_value >= critical_value:
        raise ValueError(
            f"경고 기준은 위험 기준보다 작아야 합니다. "
            f"{warning_key}={warning_value}, "
            f"{critical_key}={critical_value}"
        )