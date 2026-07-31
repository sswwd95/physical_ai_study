from pathlib import Path


PROJECT_DIRECTORIES = [
    "configs",
    "assets",
    "data/raw",
    "data/processed",
    "data/results",
    "logs",
    "models",
    "reports",
    "tests",
    "src/harness",
    "src/simulation",
    "src/sensors",
    "src/monitoring",
    "src/maintenance",
    "src/quality",
    "src/collaboration",
    "src/rl",
    "src/digital_twin",
    "examples/stage01",
]


def create_project_directories(root: Path) -> None:
    """프로젝트에서 사용할 디렉터리를 생성한다."""

    for relative_path in PROJECT_DIRECTORIES:
        directory = root / relative_path
        directory.mkdir(parents=True, exist_ok=True)
        print(f"[생성 확인] {directory}")


if __name__ == "__main__":
    project_root = Path.cwd()
    create_project_directories(project_root)