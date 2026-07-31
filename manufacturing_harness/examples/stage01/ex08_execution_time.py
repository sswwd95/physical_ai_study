from time import sleep

from src.harness.execution import ExecutionHarness
from src.harness.result import TaskResult


def simulate_sensor_loading() -> dict[str, int]:
    """센서 파일을 읽는 상황을 가정한다."""

    sleep(0.3)

    return {
        "loaded_rows": 10_000,
    }


def check_execution_time(
    result: TaskResult,
    limit_seconds: float,
) -> bool:
    """실행 시간이 제한 이내인지 검사한다."""

    if result.duration_seconds > limit_seconds:
        print(
            f"[경고] {result.task_name}의 실행 시간이 "
            f"{limit_seconds}초를 초과했습니다."
        )
        return False

    print(f"[정상] 실행 시간: {result.duration_seconds}초")
    return True


if __name__ == "__main__":
    harness = ExecutionHarness()

    result = harness.run(
        "sensor_data_loading",
        simulate_sensor_loading,
    )

    check_execution_time(
        result=result,
        limit_seconds=0.2,
    )