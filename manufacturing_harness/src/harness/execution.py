from collections.abc import Callable
from datetime import datetime
from time import perf_counter
from typing import Any

from src.harness.result import TaskResult


class ExecutionHarness:
    """제조 Physical AI 작업을 안전하게 실행하는 하네스."""

    def run(
        self,
        task_name: str,
        task: Callable[[], dict[str, Any] | None],
    ) -> TaskResult:
        """작업 하나를 실행하고 결과를 반환한다."""

        started_at = datetime.now()
        start_counter = perf_counter()

        try:
            returned_metrics = task()
            metrics = returned_metrics or {}

            success = True
            message = "작업이 정상적으로 완료되었습니다."

        except Exception as error:
            metrics = {}
            success = False
            message = f"{type(error).__name__}: {error}"

        finished_at = datetime.now()
        duration = perf_counter() - start_counter

        return TaskResult(
            task_name=task_name,
            success=success,
            started_at=started_at.isoformat(timespec="seconds"),
            finished_at=finished_at.isoformat(timespec="seconds"),
            duration_seconds=round(duration, 6),
            message=message,
            metrics=metrics,
        )