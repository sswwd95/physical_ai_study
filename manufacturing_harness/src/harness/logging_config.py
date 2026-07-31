import logging


def create_basic_logger(
    logger_name: str = "manufacturing_harness",
    level: int = logging.INFO,
) -> logging.Logger:
    """기본 콘솔 로거를 생성한다."""

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.propagate = False

    return logger

# 실습 22
import logging
from pathlib import Path


def setup_logger(
    log_directory: Path,
    logger_name: str = "manufacturing_harness",
) -> logging.Logger:
    """콘솔과 파일에 동시에 기록하는 로거를 생성한다."""

    log_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | %(levelname)-8s | "
            "%(name)s | %(filename)s:%(lineno)d | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        filename=log_directory / "manufacturing.log",
        mode="a",
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.propagate = False

    return logger


# 실습 23
def log_temperature_state(
    logger: logging.Logger,
    temperature: float,
    warning_limit: float,
    critical_limit: float,
) -> str:
    """온도 상태를 판단하고 적절한 로그 수준으로 기록한다."""

    if warning_limit >= critical_limit:
        raise ValueError(
            "경고 기준은 위험 기준보다 작아야 합니다."
        )

    if temperature >= critical_limit:
        state = "critical"

        logger.error(
            "설비 온도 위험 | temperature=%.2f | "
            "critical_limit=%.2f",
            temperature,
            critical_limit,
        )

    elif temperature >= warning_limit:
        state = "warning"

        logger.warning(
            "설비 온도 경고 | temperature=%.2f | "
            "warning_limit=%.2f",
            temperature,
            warning_limit,
        )

    else:
        state = "normal"

        logger.info(
            "설비 온도 정상 | temperature=%.2f",
            temperature,
        )

    return state