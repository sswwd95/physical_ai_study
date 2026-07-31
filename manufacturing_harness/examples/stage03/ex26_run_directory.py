from pathlib import Path

from src.harness.run_context import (
    create_run_context,
)


if __name__ == "__main__":
    run_context = create_run_context(
        runs_root=Path("runs"),
        project_name="manufacturing_physical_ai",
        experiment_name="panda_pick_and_place",
    )

    print(f"실행 ID: {run_context.run_id}")
    print(f"실행 폴더: {run_context.run_directory}")
