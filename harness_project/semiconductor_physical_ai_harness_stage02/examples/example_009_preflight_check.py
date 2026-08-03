"""
반도체 Physical AI 하네스 엔지니어링 실습 006~010
Windows 10 / Anaconda / PyMC / Antigravity
"""

from pathlib import Path
import importlib
import platform
import sys
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 1. 필수 파일과 폴더를 정의한다.
required_paths = [
    PROJECT_ROOT / "config" / "project_config.yaml",
    PROJECT_ROOT / "config" / "logging_config.yaml",
    PROJECT_ROOT / "examples",
    PROJECT_ROOT / "outputs",
]

# 2. 필수 Python 패키지를 정의한다.
required_packages = [
    "numpy",
    "pandas",
    "pymc",
    "arviz",
    "yaml",
]

issues = []

# 3. 운영체제와 Python 버전을 검사한다.
if platform.system() != "Windows":
    print(
        "[참고] 현재 운영체제는 Windows가 아닙니다. "
        "코드는 플랫폼 독립적으로 작성되어 계속 검사합니다."
    )

if sys.version_info < (3, 10):
    issues.append(
        f"Python 3.10 이상 필요, 현재 {sys.version_info.major}."
        f"{sys.version_info.minor}"
    )

# 4. 필수 경로 존재 여부를 검사한다.
for path in required_paths:
    if not path.exists():
        issues.append(f"필수 경로 누락: {path}")

# 5. 필수 패키지 import 가능 여부를 검사한다.
for package_name in required_packages:
    try:
        importlib.import_module(package_name)
    except ImportError:
        issues.append(f"필수 패키지 누락: {package_name}")

# 6. YAML 설정의 핵심 항목을 검사한다.
config_path = PROJECT_ROOT / "config" / "project_config.yaml"
if config_path.exists():
    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    required_sections = [
        "project",
        "paths",
        "sampling",
        "monitoring",
    ]

    for section in required_sections:
        if section not in config:
            issues.append(f"YAML 필수 섹션 누락: {section}")

# 7. 최종 검사 결과를 출력한다.
if issues:
    print("[사전 점검 실패]")
    for issue in issues:
        print("-", issue)
    raise SystemExit(1)

print("[사전 점검 통과]")
print("Python:", sys.version.split()[0])
print("운영체제:", platform.system(), platform.release())
print("프로젝트 루트:", PROJECT_ROOT)
