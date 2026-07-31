from pathlib import Path
from time import perf_counter, sleep

from src.harness.logging_harness import (
    ManufacturingLoggingHarness,
)


def simulate_panda_production_cycle(
    harness: ManufacturingLoggingHarness,
) -> dict[str, float]:
    """Panda 생산 사이클을 단순 모의 실행한다."""

    logger = harness.get_task_logger(
        task_name="panda_production_cycle",
        robot_id="panda_01",
    )

    logger.info("Panda 생산 사이클 시작")

    start_time = perf_counter()

    temperature = 58.4
    vibration = 0.17
    motor_current = 5.8

    logger.debug(
        "센서 원본값 | temperature=%.2f | "
        "vibration=%.3f | current=%.2f",
        temperature,
        vibration,
        motor_current,
    )

    sleep(0.1)

    logger.info("부품 접근 동작 완료")
    sleep(0.1)

    logger.info("부품 집기 완료")
    sleep(0.1)

    logger.info("부품 이동 완료")
    sleep(0.1)

    logger.info("부품 배치 완료")

    cycle_time = perf_counter() - start_time
    defect_rate = 0.012
    anomaly_score = 0.18

    harness.log_metric(
        metric_name="production.cycle_time_seconds",
        metric_value=cycle_time,
        step=1,
        tags={
            "robot_id": "panda_01",
            "product_type": "part_A",
        },
    )

    harness.log_metric(
        metric_name="quality.defect_rate",
        metric_value=defect_rate,
        step=1,
        tags={
            "line_id": "line_01",
        },
    )

    harness.log_metric(
        metric_name="maintenance.anomaly_score",
        metric_value=anomaly_score,
        step=1,
        tags={
            "equipment_id": "panda_01",
        },
    )

    harness.log_event(
        message="Panda 생산 사이클 완료",
        event_type="production_cycle_completed",
        fields={
            "robot_id": "panda_01",
            "cycle_id": 1,
            "cycle_time_seconds": cycle_time,
            "defect_rate": defect_rate,
            "anomaly_score": anomaly_score,
        },
    )

    logger.info(
        "Panda 생산 사이클 완료 | "
        "cycle_time=%.3f초",
        cycle_time,
    )

    return {
        "cycle_time_seconds": cycle_time,
        "defect_rate": defect_rate,
        "anomaly_score": anomaly_score,
    }


if __name__ == "__main__":
    harness = ManufacturingLoggingHarness(
        runs_root=Path("runs"),
        project_name="manufacturing_physical_ai",
        experiment_name="panda_cycle_logging_test",
    )

    task_logger = harness.get_task_logger(
        task_name="main",
        robot_id="panda_01",
    )

    try:
        metrics = simulate_panda_production_cycle(
            harness
        )

        task_logger.info(
            "모든 작업 정상 완료 | metrics=%s",
            metrics,
        )

        summary_path = harness.finish(
            success=True,
        )

        print(f"실행 ID: {harness.run_context.run_id}")
        print(
            "실행 디렉터리: "
            f"{harness.run_context.run_directory}"
        )
        print(f"요약 파일: {summary_path}")

    except Exception as error:
        task_logger.exception(
            "통합 실행 중 오류 발생"
        )

        harness.log_event(
            message="통합 실행 실패",
            event_type="run_failed",
            fields={
                "error_type": type(error).__name__,
                "error_message": str(error),
            },
        )

        harness.finish(
            success=False,
            error_message=(
                f"{type(error).__name__}: {error}"
            ),
        )
