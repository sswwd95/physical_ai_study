
# 제조 Physical AI 프로젝트에 필요한 configs, assets, data, logs,
# models, reports, tests, src, examples 폴더를 자동 생성하는
# Python 프로그램을 pathlib 기반으로 작성해줘.
# 이미 폴더가 존재해도 오류가 발생하지 않아야 한다.
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
        #  `parents=True`: 상위 폴더가 없어도 함께 생성
        #  `exist_ok=True`: 이미 폴더가 있어도 오류를 발생시키지 않음        
        print(f"[생성 확인] {directory}")


if __name__ == "__main__":
    project_root = Path.cwd()
    print("현재 생성 위치:", project_root)
    create_project_directories(project_root)