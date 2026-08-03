"""
반도체 Physical AI 하네스 엔지니어링 실습 006~010
Windows 10 / Anaconda / PyMC / Antigravity
"""

from pathlib import Path
import yaml

# 1. 현재 예제 파일을 기준으로 프로젝트 루트를 계산한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# 2. YAML 설정 파일의 위치를 만든다.
CONFIG_PATH = PROJECT_ROOT / "config" / "project_config.yaml"

# 3. YAML 파일을 읽어 Python 사전으로 변환한다.
with CONFIG_PATH.open("r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# 4. 설정값을 꺼내 사용할 경로를 만든다.
data_dir = PROJECT_ROOT / config["paths"]["data_dir"]
output_dir = PROJECT_ROOT / config["paths"]["output_dir"]
log_dir = PROJECT_ROOT / config["paths"]["log_dir"]

# 5. 필요한 폴더가 없으면 생성한다.
for directory in (data_dir, output_dir, log_dir):
    directory.mkdir(parents=True, exist_ok=True)

# 6. 핵심 설정을 출력해 정상 로딩 여부를 확인한다.
print("[설정 로딩 완료]")
print("프로젝트명:", config["project"]["name"])
print("버전:", config["project"]["version"])
print("난수 시드:", config["project"]["random_seed"])
print("샘플링 주기:", config["sampling"]["interval_sec"], "초")
print("데이터 폴더:", data_dir)
print("결과 폴더:", output_dir)
print("로그 폴더:", log_dir)
