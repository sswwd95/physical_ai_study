from collections.abc import Callable
from dataclasses import asdict
from pprint import pprint
from typing import Any

from src.harness.execution import ExecutionHarness


def analyze_temperature() -> dict[str, Any]:
    values = [42.1, 43.5, 44.2, 45.0]

    return {
        "mean": sum(values) / len(values),
        "maximum": max(values),
    }


def analyze_vibration() -> dict[str, Any]:
    values = [0.12, 0.15, 0.11, 0.18]

    return {
        "mean": sum(values) / len(values),
        "maximum": max(values),
    }


def analyze_production() -> dict[str, Any]:
    target_count = 100
    actual_count = 92

    return {
        "target_count": target_count,
        "actual_count": actual_count,
        "achievement_rate": actual_count / target_count,
    }


if __name__ == "__main__":
    tasks: list[tuple[str, Callable[[], dict[str, Any]]]] = [
        ("temperature_analysis", analyze_temperature),
        ("vibration_analysis", analyze_vibration),
        ("production_analysis", analyze_production),
    ]

    harness = ExecutionHarness()

    for task_name, task_function in tasks:
        result = harness.run(task_name, task_function)
        pprint(asdict(result))