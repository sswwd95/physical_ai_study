"""
반도체 Physical AI 하네스 엔지니어링 실습
Windows 10 / Anaconda / PyMC
"""

from pathlib import Path
import json

# 1. 현재 파일이 속한 프로젝트 루트 경로를 계산한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 2. 프로젝트에서 공통으로 사용할 폴더를 정의한다.
PATHS = {
    "data": PROJECT_ROOT / "data",
    "outputs": PROJECT_ROOT / "outputs",
    "docs": PROJECT_ROOT / "docs",
}

# 3. 폴더가 없으면 자동으로 만든다.
for path in PATHS.values():
    path.mkdir(parents=True, exist_ok=True)

# 4. 실습 전체에서 공유할 기본 설정을 만든다.
CONFIG = {
    "project_name": "semiconductor_physical_ai",
    "random_seed": 42,
    "sample_interval_sec": 1.0,
    "sensor_units": {
        "temperature_c": "degC",
        "pressure_kpa": "kPa",
        "gas_flow_sccm": "sccm",
        "vibration_rms": "mm/s",
        "motor_current_a": "A",
    },
}

# 5. 설정을 JSON 파일로 저장한다.
config_path = PATHS["outputs"] / "project_config.json"
config_path.write_text(
    json.dumps(CONFIG, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(f"[완료] 프로젝트 루트: {PROJECT_ROOT}")
print(f"[완료] 설정 파일: {config_path}")
