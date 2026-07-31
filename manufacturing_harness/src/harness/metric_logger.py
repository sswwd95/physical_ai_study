import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class MetricLogger:
    """숫자 실험 지표를 JSONL 파일에 저장한다."""

    def __init__(
        self,
        output_path: Path,
        run_id: str,
    ) -> None:
        self.output_path = output_path
        self.run_id = run_id

        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def log(
        self,
        metric_name: str,
        metric_value: int | float,
        step: int | None = None,
        tags: dict[str, Any] | None = None,
    ) -> None:
        """지표 한 건을 JSONL로 저장한다."""

        if not metric_name.strip():
            raise ValueError(
                "지표 이름은 비어 있을 수 없습니다."
            )

        numeric_value = float(metric_value)

        if not math.isfinite(numeric_value):
            raise ValueError(
                "지표값은 NaN 또는 무한대일 수 없습니다."
            )

        if step is not None and step < 0:
            raise ValueError(
                "step은 0 이상이어야 합니다."
            )

        record = {
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "run_id": self.run_id,
            "metric_name": metric_name,
            "metric_value": metric_value,
            "step": step,
            "tags": tags or {},
        }

        with self.output_path.open(
            mode="a",
            encoding="utf-8",
        ) as file:
            file.write(
                json.dumps(
                    record,
                    ensure_ascii=False,
                    default=str,
                )
                + "\n"
            )
