# Python dataclass를 사용해 제조 Physical AI 작업 실행 결과를
# 표현하는 TaskResult 클래스를 작성해줘.

# 필드는 task_name, success, started_at, finished_at,
# duration_seconds, message, metrics를 포함해야 한다.

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