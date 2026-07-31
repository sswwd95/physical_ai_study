from pathlib import Path

from src.harness.metric_logger import MetricLogger
from src.harness.run_context import (
    create_run_context,
)


if __name__ == "__main__":
    run_context = create_run_context(
        runs_root=Path("runs"),
        project_name="manufacturing_physical_ai",
        experiment_name="production_metric_test",
    )

    metric_logger = MetricLogger(
        output_path=(
            run_context.metrics_directory
            / "metrics.jsonl"
        ),
        run_id=run_context.run_id,
    )

    metric_logger.log(
        metric_name="cycle_time_seconds",
        metric_value=28.4,
        step=1,
        tags={
            "robot_id": "panda_01",
            "product_type": "part_A",
        },
    )

    metric_logger.log(
        metric_name="defect_rate",
        metric_value=0.018,
        step=1,
        tags={
            "line_id": "line_01",
        },
    )

    metric_logger.log(
        metric_name="production_count",
        metric_value=118,
        step=1,
        tags={
            "line_id": "line_01",
            "unit": "count_per_hour",
        },
    )
