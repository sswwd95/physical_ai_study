from pathlib import Path

from src.harness.context_adapter import (
    create_context_logger,
    setup_context_logger,
)
from src.harness.run_context import (
    create_run_context,
)


if __name__ == "__main__":
    run_context = create_run_context(
        runs_root=Path("runs"),
        project_name="manufacturing_physical_ai",
        experiment_name="panda_torque_test",
    )

    base_logger = setup_context_logger(
        run_context.logs_directory
        / "context.log"
    )

    logger = create_context_logger(
        logger=base_logger,
        run_id=run_context.run_id,
        task_name="panda_joint_monitoring",
        robot_id="panda_01",
    )

    logger.info(
        "Panda 관절 모니터링 시작"
    )

    logger.warning(
        "관절 토크 경고",
        extra={
            "joint_name": "panda_joint4",
            "torque": 31.2,
        },
    )
