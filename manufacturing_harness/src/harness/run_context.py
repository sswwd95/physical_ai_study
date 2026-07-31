from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from uuid import uuid4


@dataclass(frozen=True)
class RunContext:
    """하나의 실험 실행 정보를 표현한다."""

    run_id: str
    project_name: str
    experiment_name: str
    started_at: str
    run_directory: Path
    logs_directory: Path
    metrics_directory: Path
    models_directory: Path
    artifacts_directory: Path
    config_directory: Path
    reports_directory: Path


def create_run_context(
    runs_root: Path,
    project_name: str,
    experiment_name: str,
) -> RunContext:
    """새 실행 ID와 전용 디렉터리를 생성한다."""

    started_at = datetime.now()

    timestamp = started_at.strftime(
        "%Y%m%d_%H%M%S"
    )

    unique_suffix = uuid4().hex[:6]

    run_id = (
        f"run_{timestamp}_{unique_suffix}"
    )

    run_directory = (
        runs_root / run_id
    ).resolve()

    subdirectories = {
        "logs": run_directory / "logs",
        "metrics": run_directory / "metrics",
        "models": run_directory / "models",
        "artifacts": run_directory / "artifacts",
        "config": run_directory / "config",
        "reports": run_directory / "reports",
    }

    for directory in subdirectories.values():
        directory.mkdir(
            parents=True,
            exist_ok=False,
        )

    return RunContext(
        run_id=run_id,
        project_name=project_name,
        experiment_name=experiment_name,
        started_at=started_at.isoformat(
            timespec="seconds"
        ),
        run_directory=run_directory,
        logs_directory=subdirectories["logs"],
        metrics_directory=subdirectories["metrics"],
        models_directory=subdirectories["models"],
        artifacts_directory=subdirectories["artifacts"],
        config_directory=subdirectories["config"],
        reports_directory=subdirectories["reports"],
    )
