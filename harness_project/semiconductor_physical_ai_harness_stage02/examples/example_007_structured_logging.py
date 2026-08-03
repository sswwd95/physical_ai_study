"""
반도체 Physical AI 하네스 엔지니어링 실습 006~010
Windows 10 / Anaconda / PyMC / Antigravity
"""

from pathlib import Path
import logging
import logging.config
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_CONFIG_PATH = PROJECT_ROOT / "config" / "logging_config.yaml"

# 1. 로그 파일 경로가 상대경로이므로 프로젝트 루트로 이동하지 않고
#    설정 내용을 읽어 절대경로로 바꾼다.
with LOG_CONFIG_PATH.open("r", encoding="utf-8") as file:
    log_config = yaml.safe_load(file)

relative_log_path = Path(log_config["handlers"]["file"]["filename"])
absolute_log_path = PROJECT_ROOT / relative_log_path
absolute_log_path.parent.mkdir(parents=True, exist_ok=True)
log_config["handlers"]["file"]["filename"] = str(absolute_log_path)

# 2. YAML 설정을 logging 모듈에 적용한다.
logging.config.dictConfig(log_config)

# 3. 이 예제를 위한 이름 있는 로거를 만든다.
logger = logging.getLogger("semiconductor.harness")

# 4. 일반 실행 정보, 경고, 오류 상황을 구조화된 형식으로 기록한다.
logger.info("하네스 실행 시작")
logger.info("센서 로그 입력 준비 완료")
logger.warning("교육용 임계값은 실제 공정 승인 기준이 아님")

try:
    # 5. 오류 기록 예시를 위해 의도적으로 0으로 나눈다.
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("예제 오류를 기록했습니다.")

logger.info("하네스 실행 종료")
print(f"[완료] 로그 파일: {absolute_log_path}")
