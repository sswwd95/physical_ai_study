from pathlib import Path
from typing import Any

import yaml


def load_yaml(config_path: Path) -> dict[str, Any]:
    """YAML 설정 파일을 읽어 딕셔너리로 반환한다."""

    if not config_path.exists():
        raise FileNotFoundError(
            f"설정 파일을 찾을 수 없습니다: {config_path}"
        )

    if not config_path.is_file():
        raise ValueError(
            f"설정 경로가 파일이 아닙니다: {config_path}"
        )

    with config_path.open(
        mode="r",
        encoding="utf-8",
    ) as file:
        loaded_data = yaml.safe_load(file)

    if loaded_data is None:
        return {}

    if not isinstance(loaded_data, dict):
        raise ValueError(
            "YAML 최상위 구조는 키와 값으로 구성된 "
            "딕셔너리여야 합니다."
        )

    return loaded_data


def save_yaml(data: dict[str, Any], config_path: Path) -> Path:
    """딕셔너리 데이터를 YAML 파일로 저장한다."""

    config_path.parent.mkdir(parents=True, exist_ok=True)

    with config_path.open(mode="w", encoding="utf-8") as file:
        yaml.safe_dump(
            data,
            file,
            allow_unicode=True,
            sort_keys=False,
        )

    return config_path

#==========================================================
# 실습 13. 중첩 설정값 안전하게 조회

from typing import Any


_MISSING = object()


def get_config_value(
    config: dict[str, Any],
    key_path: str,
    default: Any = _MISSING,
) -> Any:
    """점으로 구분한 경로를 사용해 중첩 설정값을 조회한다."""

    if not key_path.strip():
        raise ValueError("설정 키 경로가 비어 있습니다.")

    current_value: Any = config

    for key in key_path.split("."):
        if not isinstance(current_value, dict):
            raise TypeError(
                f"'{key}'를 조회하기 전에 만난 값이 "
                "딕셔너리가 아닙니다."
            )

        if key not in current_value:
            if default is not _MISSING:
                return default

            raise KeyError(
                f"필수 설정값을 찾을 수 없습니다: {key_path}"
            )

        current_value = current_value[key]

    return current_value

#==========================================================
# 실습 18. Windows 경로 안전 처리

from pathlib import Path
from typing import Literal


PathType = Literal[
    "any",
    "file",
    "directory",
]


def resolve_project_path(
    project_root: Path,
    configured_path: str | Path,
    must_exist: bool = False,
    expected_type: PathType = "any",
) -> Path:
    """설정 경로를 프로젝트 기준 절대경로로 변환한다."""

    path = Path(configured_path).expanduser()

    if not path.is_absolute():
        path = project_root / path

    resolved_path = path.resolve()

    if must_exist and not resolved_path.exists():
        raise FileNotFoundError(
            f"경로를 찾을 수 없습니다: {resolved_path}"
        )

    if (
        must_exist
        and expected_type == "file"
        and not resolved_path.is_file()
    ):
        raise ValueError(
            f"파일 경로가 아닙니다: {resolved_path}"
        )

    if (
        must_exist
        and expected_type == "directory"
        and not resolved_path.is_dir()
    ):
        raise ValueError(
            f"디렉터리 경로가 아닙니다: {resolved_path}"
        )

    return resolved_path