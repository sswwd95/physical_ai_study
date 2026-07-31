
import json
import logging
from datetime import datetime, timezone
from typing import Any


class JsonFormatter(logging.Formatter):
    """로그 레코드를 JSON 문자열로 변환한다."""

    def format(
        self,
        record: logging.LogRecord,
    ) -> str:
        """LogRecord를 JSON 문자열로 반환한다."""

        log_data: dict[str, Any] = {
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "process_id": record.process,
            "thread_name": record.threadName,
        }

        extra_fields = getattr(
            record,
            "extra_fields",
            None,
        )

        if isinstance(extra_fields, dict):
            log_data.update(extra_fields)

        if record.exc_info:
            log_data["exception"] = (
                self.formatException(
                    record.exc_info
                )
            )

        return json.dumps(
            log_data,
            ensure_ascii=False,
            default=str,
        )