from copy import deepcopy
from typing import Any


def deep_merge(
    base_config: dict[str, Any],
    override_config: dict[str, Any],
) -> dict[str, Any]:
    """기본 설정에 재정의 설정을 재귀적으로 병합한다."""

    merged_config = deepcopy(base_config)

    for key, override_value in override_config.items():
        base_value = merged_config.get(key)

        if (
            isinstance(base_value, dict)
            and isinstance(override_value, dict)
        ):
            merged_config[key] = deep_merge(
                base_config=base_value,
                override_config=override_value,
            )
        else:
            merged_config[key] = deepcopy(override_value)

    return merged_config