from dataclasses import asdict
from pprint import pprint

from src.harness.execution import ExecutionHarness


def analyze_empty_sensor_data() -> dict[str, float]:
    """비어 있는 센서 데이터를 분석한다."""

    sensor_values: list[float] = []

    if not sensor_values:
        raise ValueError("센서 데이터가 비어 있습니다.")

    return {
        "mean": sum(sensor_values) / len(sensor_values),
    }


if __name__ == "__main__":
    harness = ExecutionHarness()

    result = harness.run(
        task_name="empty_sensor_test",
        task=analyze_empty_sensor_data,
    )

    pprint(asdict(result))

    print("프로그램이 중단되지 않고 다음 작업을 수행합니다.")