from pathlib import Path

from src.harness.execution import ExecutionHarness
from src.harness.storage import save_result


def inspect_production_line() -> dict[str, float]:
    """생산 라인의 기본 지표를 반환한다."""

    production_count = 950
    target_count = 1_000
    defect_count = 18

    return {
        "production_count": production_count,
        "target_count": target_count,
        "achievement_rate": production_count / target_count,
        "defect_rate": defect_count / production_count,
    }


if __name__ == "__main__":
    harness = ExecutionHarness()

    result = harness.run(
        task_name="production_line_inspection",
        task=inspect_production_line,
    )

    saved_path = save_result(
        result=result,
        output_directory=Path("data/results"),
    )

    print(f"결과 저장 완료: {saved_path}")