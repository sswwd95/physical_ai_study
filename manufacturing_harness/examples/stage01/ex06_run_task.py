from dataclasses import asdict
from pprint import pprint

from src.harness.execution import ExecutionHarness


def analyze_motor_temperature() -> dict[str, float]:
    """모터 온도 데이터의 요약 통계를 계산한다."""

    temperatures = [
        41.2,
        42.5,
        43.1,
        44.0,
        43.8,
        45.2,
        46.1,
        44.9,
        43.7,
        42.8,
    ]

    average_temperature = sum(temperatures) / len(temperatures)
    maximum_temperature = max(temperatures)

    return {
        "average_temperature": round(average_temperature, 2),
        "maximum_temperature": maximum_temperature,
        "sample_count": len(temperatures),
    }


if __name__ == "__main__":
    harness = ExecutionHarness()

    result = harness.run(
        task_name="motor_temperature_analysis",
        task=analyze_motor_temperature,
    )

    pprint(asdict(result))