import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from src.harness.result import TaskResult


def save_result(
    result: TaskResult,
    output_directory: Path,
) -> Path:
    """TaskResult를 JSON 파일로 저장한다."""

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"{result.task_name}_{timestamp}.json"
    output_path = output_directory / file_name

    result_data = asdict(result)

    output_path.write_text(
        json.dumps(
            result_data,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    return output_path