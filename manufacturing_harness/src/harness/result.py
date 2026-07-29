from dataclasses import dataclass, field
from typing import Any


@dataclass
class TaskResult:
    """하네스에서 실행한 하나의 작업 결과."""

    task_name: str
    success: bool
    started_at: str
    finished_at: str
    duration_seconds: float
    message: str = ""
    metrics: dict[str, Any] = field(default_factory=dict)