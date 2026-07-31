import json
import logging
from dataclasses import asdict
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from src.harness.context_adapter import (
    ContextLoggerAdapter,
    create_context_logger,
)
from src.harness.json_formatter import JsonFormatter
from src.harness.metric_logger import MetricLogger
from src.harness.run_context import (
    RunContext,
    create_run_context,
)


class SafeContextFormatter(logging.Formatter):
    """로그 컨텍스트가 없을 때 기본값을 제공한다."""

    def format(
        self,
        record: logging.LogRecord,
    ) -> str:
        defaults = {
            "run_id": "unknown",
            "task_name": "unknown",
            "robot_id": "unknown",
        }

        for key, value in defaults.items():
            if not hasattr(record, key):
                setattr(record, key, value)

        return super().format(record)


class ManufacturingLoggingHarness:
    """제조 Physical AI 통합 로깅 하네스."""

    def __init__(
        self,
        runs_root: Path,
        project_name: str,
        experiment_name: str,
    ) -> None:
        self.run_context = create_run_context(
            runs_root=runs_root,
            project_name=project_name,
            experiment_name=experiment_name,
        )

        self.logger = self._create_logger()
        self.json_logger = self._create_json_logger()

        self.metric_logger = MetricLogger(
            output_path=(
                self.run_context.metrics_directory
                / "metrics.jsonl"
            ),
            run_id=self.run_context.run_id,
        )

        self.finished_at: str | None = None
        self.success: bool | None = None
        self.error_message: str | None = None

        self.logger.info(
            "실행 시작 | experiment=%s",
            experiment_name,
            extra={
                "run_id": self.run_context.run_id,
                "task_name": "harness_initialization",
                "robot_id": "unknown",
            },
        )

        self.json_logger.info(
            "실행 시작",
            extra={
                "extra_fields": {
                    "run_id": (
                        self.run_context.run_id
                    ),
                    "project_name": project_name,
                    "experiment_name": (
                        experiment_name
                    ),
                    "event_type": "run_started",
                }
            },
        )

    def _create_logger(self) -> logging.Logger:
        """텍스트·콘솔 로거를 생성한다."""

        logger_name = (
            f"manufacturing."
            f"{self.run_context.run_id}"
        )

        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        formatter = SafeContextFormatter(
            fmt=(
                "%(asctime)s | %(levelname)-8s | "
                "run_id=%(run_id)s | "
                "task=%(task_name)s | "
                "robot=%(robot_id)s | "
                "%(filename)s:%(lineno)d | "
                "%(message)s"
            ),
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        rotating_handler = RotatingFileHandler(
            filename=(
                self.run_context.logs_directory
                / "manufacturing.log"
            ),
            maxBytes=5_000_000,
            backupCount=5,
            encoding="utf-8",
        )
        rotating_handler.setLevel(logging.DEBUG)
        rotating_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(rotating_handler)

        return logger

    def _create_json_logger(
        self,
    ) -> logging.Logger:
        """JSON 구조화 로거를 생성한다."""

        logger_name = (
            f"manufacturing_json."
            f"{self.run_context.run_id}"
        )

        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        file_handler = logging.FileHandler(
            filename=(
                self.run_context.logs_directory
                / "events.jsonl"
            ),
            encoding="utf-8",
        )

        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(JsonFormatter())

        logger.addHandler(file_handler)

        return logger

    def get_task_logger(
        self,
        task_name: str,
        robot_id: str = "unknown",
    ) -> ContextLoggerAdapter:
        """작업별 컨텍스트 로거를 반환한다."""

        return create_context_logger(
            logger=self.logger,
            run_id=self.run_context.run_id,
            task_name=task_name,
            robot_id=robot_id,
        )

    def log_metric(
        self,
        metric_name: str,
        metric_value: int | float,
        step: int | None = None,
        tags: dict[str, Any] | None = None,
    ) -> None:
        """숫자 지표를 기록한다."""

        self.metric_logger.log(
            metric_name=metric_name,
            metric_value=metric_value,
            step=step,
            tags=tags,
        )

    def log_event(
        self,
        message: str,
        event_type: str,
        fields: dict[str, Any] | None = None,
        level: int = logging.INFO,
    ) -> None:
        """JSON 구조화 이벤트를 기록한다."""

        event_fields = {
            "run_id": self.run_context.run_id,
            "event_type": event_type,
            **(fields or {}),
        }

        self.json_logger.log(
            level=level,
            msg=message,
            extra={
                "extra_fields": event_fields,
            },
        )

    def finish(
        self,
        success: bool,
        error_message: str | None = None,
    ) -> Path:
        """실행 종료 정보와 요약 파일을 저장한다."""

        self.finished_at = datetime.now().isoformat(
            timespec="seconds"
        )

        self.success = success
        self.error_message = error_message

        level = (
            logging.INFO
            if success
            else logging.ERROR
        )

        self.logger.log(
            level,
            "실행 종료 | success=%s | error=%s",
            success,
            error_message,
            extra={
                "run_id": self.run_context.run_id,
                "task_name": "harness_finish",
                "robot_id": "unknown",
            },
        )

        self.log_event(
            message="실행 종료",
            event_type="run_finished",
            level=level,
            fields={
                "success": success,
                "error_message": error_message,
                "finished_at": self.finished_at,
            },
        )

        summary_path = (
            self.run_context.reports_directory
            / "run_summary.json"
        )

        summary_data = {
            "run_context": self._convert_paths(
                asdict(self.run_context)
            ),
            "finished_at": self.finished_at,
            "success": success,
            "error_message": error_message,
        }

        summary_path.write_text(
            json.dumps(
                summary_data,
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        return summary_path

    def _convert_paths(
        self,
        value: Any,
    ) -> Any:
        """중첩 데이터의 Path를 문자열로 변환한다."""

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
