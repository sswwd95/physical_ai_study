import os
import platform
import sys
from pathlib import Path


def print_system_info() -> None:
    """현재 Python 실행 환경의 기본 정보를 출력한다."""

    print("=" * 50)
    print("제조 Physical AI 실행 환경")
    print("=" * 50)

    print(f"운영체제       : {platform.system()}")
    print(f"운영체제 버전  : {platform.version()}")
    print(f"Python 버전    : {platform.python_version()}")
    print(f"Python 실행파일: {sys.executable}")
    print(f"현재 작업 폴더 : {Path.cwd()}")
    print(f"프로세스 ID    : {os.getpid()}")


if __name__ == "__main__":
    print_system_info()
    
# ==================================================
# 제조 Physical AI 실행 환경
# ==================================================
# 운영체제       : Windows
# 운영체제 버전  : 10.0.19045
# Python 버전    : 3.11.15
# Python 실행파일: C:\Users\sswwd\anaconda3\envs\physical_ai\python.exe
# 현재 작업 폴더 : C:\work\physical_ai\Harness_Engineering\examples\stage01
# 프로세스 ID    : 14248


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