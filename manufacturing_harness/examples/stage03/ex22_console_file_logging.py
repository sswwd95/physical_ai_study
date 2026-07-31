from pathlib import Path

from src.harness.logging_config import setup_logger


if __name__ == "__main__":
    logger = setup_logger(Path("logs"))

    logger.debug("디버그용 상세 메시지입니다.")
    logger.info("온도 센서 수집을 시작합니다.")
    logger.warning("온도가 경고 기준에 접근했습니다.")
