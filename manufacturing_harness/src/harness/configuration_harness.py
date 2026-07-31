import json
import os
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from src.harness.app_config import (
    AppConfig,
    build_app_config,
)
from src.harness.config_loader import load_yaml
from src.harness.config_merge import deep_merge
from src.harness.config_validator import (
    REQUIRED_CONFIG_KEYS,
    validate_config_type,
    validate_number_range,
    validate_required_keys,
    validate_threshold_order, # 실습 20번 추가
)



class ConfigurationHarness:
    """프로젝트 설정을 읽고 검증하는 통합 하네스."""

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root.resolve()

    def load(
        self,
        base_config_path: Path,
        environment_config_path: Path | None = None,
        env_file_path: Path | None = None,
    ) -> AppConfig:
        """설정을 읽고 검증하여 AppConfig를 반환한다."""

        if env_file_path is not None:
            self._load_environment_file(
                env_file_path
            )

        base_config = load_yaml(
            self._resolve_path(base_config_path)
        )

        merged_config = base_config

        if environment_config_path is not None:
            environment_config = load_yaml(
                self._resolve_path(
                    environment_config_path
                )
            )

            merged_config = deep_merge(
                base_config=base_config,
                override_config=environment_config,
            )

        self._validate_config(merged_config)
        self._create_output_directories(merged_config)

        app_config = build_app_config(
            raw_config=merged_config,
            project_root=self.project_root,
        )

        self._save_validation_report(
            app_config=app_config,
        )

        return app_config

    def _resolve_path(self, path: Path) -> Path:
        """상대경로를 프로젝트 기준 절대경로로 바꾼다."""

        if path.is_absolute():
            return path.resolve()

        return (self.project_root / path).resolve()

    def _load_environment_file(
        self,
        env_file_path: Path,
    ) -> None:
        """환경변수 파일을 불러온다."""

        resolved_path = self._resolve_path(
            env_file_path
        )

        if not resolved_path.exists():
            raise FileNotFoundError(
                f"환경변수 파일이 없습니다: {resolved_path}"
            )

        load_dotenv(
            dotenv_path=resolved_path,
            override=False,
        )

    def _validate_config(
        self,
        config: dict[str, Any],
    ) -> None:
        """필수값, 타입, 범위를 검증한다."""

        validate_required_keys(
            config=config,
            required_keys=REQUIRED_CONFIG_KEYS,
        )

        type_rules = [
            ("project.name", str),
            ("experiment.seed", int),
            ("simulation.model_path", str),
            ("simulation.timestep", float),
            ("simulation.control_frequency", int),
            ("simulation.episode_seconds", float),
            ("simulation.render", bool),
            (
                "production.target_count_per_hour",
                int,
            ),
            (
                "production.maximum_defect_rate",
                float,
            ),
            (
                "reinforcement_learning.algorithm",
                str,
            ),
            (
                "reinforcement_learning.total_timesteps",
                int,
            ),
        ]

        for key_path, expected_type in type_rules:
            validate_config_type(
                config=config,
                key_path=key_path,
                expected_type=expected_type,
            )

        validate_number_range(
            config=config,
            key_path="simulation.timestep",
            minimum=0.0,
            maximum=0.1,
            include_minimum=False,
        )

        validate_number_range(
            config=config,
            key_path="simulation.control_frequency",
            minimum=1,
            maximum=1000,
        )

        validate_number_range(
            config=config,
            key_path="production.maximum_defect_rate",
            minimum=0.0,
            maximum=1.0,
        )

        validate_number_range(
            config=config,
            key_path=(
                "monitoring.anomaly_score_threshold"
            ),
            minimum=0.0,
            maximum=1.0,
        )

        validate_number_range(
            config=config,
            key_path=(
                "reinforcement_learning.learning_rate"
            ),
            minimum=0.0,
            maximum=1.0,
            include_minimum=False,
        )

        # 실습 20번 추가
        validate_threshold_order(
            config=config,
            warning_key=(
                "sensors.temperature.warning_limit"
            ),
            critical_key=(
                "sensors.temperature.critical_limit"
            ),
        )

        validate_threshold_order(
            config=config,
            warning_key=(
                "sensors.vibration.warning_limit"
            ),
            critical_key=(
                "sensors.vibration.critical_limit"
            ),
        )

        validate_threshold_order(
            config=config,
            warning_key=(
                "sensors.motor_current.warning_limit"
            ),
            critical_key=(
                "sensors.motor_current.critical_limit"
            ),
        )



    def _create_output_directories(
        self,
        config: dict[str, Any],
    ) -> None:
        """설정에 지정된 출력 폴더를 생성한다."""

        output_keys = [
            "raw_data",
            "processed_data",
            "results",
            "logs",
            "models",
            "reports",
        ]

        for key in output_keys:
            relative_path = Path(
                config["paths"][key]
            )

            directory = (
                self.project_root / relative_path
            ).resolve()

            directory.mkdir(
                parents=True,
                exist_ok=True,
            )

    def _save_validation_report(
        self,
        app_config: AppConfig,
    ) -> Path:
        """설정 검증 결과를 JSON으로 저장한다."""

        report_directory = (
            app_config.paths.results
            / "configuration"
        )

        report_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        report_path = (
            report_directory
            / f"config_validation_{timestamp}.json"
        )

        report_data = {
            "success": True,
            "validated_at": (
                datetime.now().isoformat(
                    timespec="seconds"
                )
            ),
            "project_name": (
                app_config.project_name
            ),
            "environment": (
                app_config.environment
            ),
            "seed": app_config.seed,
            "model_path": str(
                app_config.simulation.model_path
            ),
            "configuration": self._convert_paths(
                asdict(app_config)
            ),
            "environment_variable_status": {
                "MANUFACTURING_ENV": os.getenv(
                    "MANUFACTURING_ENV"
                ),
                "database_password_configured": bool(
                    os.getenv(
                        "MANUFACTURING_DB_PASSWORD"
                    )
                ),
            },
        }

        report_path.write_text(
            json.dumps(
                report_data,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        return report_path

    def _convert_paths(self, value: Any) -> Any:
        """중첩 구조 안의 Path를 문자열로 변환한다."""

        if isinstance(value, Path):
            return str(value)

        if isinstance(value, dict):
            return {
                key: self._convert_paths(item)
                for key, item in value.items()
            }

        if isinstance(value, list):
            return [
                self._convert_paths(item)
                for item in value
            ]

        return value