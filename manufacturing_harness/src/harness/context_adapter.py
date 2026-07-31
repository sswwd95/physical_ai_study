import logging
from collections.abc import Mapping
from typing import Any


class ContextLoggerAdapter(logging.LoggerAdapter):
    """실행 컨텍스트를 로그에 자동 추가한다."""

    def process(
        self,
        msg: Any,
        kwargs: dict[str, Any],
    ) -> tuple[Any, dict[str, Any]]:
        """로그 호출 전에 extra 값을 병합한다."""

        provided_extra = kwargs.get(
            "extra",
            {},
        )

        merged_extra = {
            **self.extra,
            **provided_extra,
        }

        kwargs["extra"] = merged_extra

        return msg, kwargs


def create_context_logger(
    logger: logging.Logger,
    run_id: str,
    task_name: str,
    robot_id: str = "unknown",
) -> ContextLoggerAdapter:
    """컨텍스트가 포함된 LoggerAdapter를 생성한다."""

    context: Mapping[str, Any] = {
        "run_id": run_id,
        "task_name": task_name,
        "robot_id": robot_id,
    }

    return ContextLoggerAdapter(
        logger=logger,
        extra=dict(context),
    )

import logging


class SafeContextFormatter(logging.Formatter):
    """없는 컨텍스트 필드에 기본값을 넣는다."""

    def format(
        self,
        record: logging.LogRecord,
    ) -> str:
        if not hasattr(record, "run_id"):
            record.run_id = "unknown"

        if not hasattr(record, "task_name"):
            record.task_name = "unknown"

        if not hasattr(record, "robot_id"):
            record.robot_id = "unknown"

        return super().format(record)

# --------------------------------------------------------
import logging
from pathlib import Path


def setup_context_logger(
    log_path: Path,
) -> logging.Logger:
    """컨텍스트 필드를 출력하는 로거를 생성한다."""

    log_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger = logging.getLogger(
        "manufacturing_context"
    )
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    formatter = SafeContextFormatter(
        fmt=(
            "%(asctime)s | %(levelname)s | "
            "run_id=%(run_id)s | "
            "task=%(task_name)s | "
            "robot=%(robot_id)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        log_path,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.propagate = False

    return logger