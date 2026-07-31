
from pathlib import Path

from src.harness.logging_config import setup_rotating_logger


if __name__ == "__main__":
    logger = setup_rotating_logger(
        log_directory=Path("logs/rotating"),
        max_bytes=5_000,
        backup_count=3,
    )

    for index in range(1_000):
        logger.info(
            "생산 센서 데이터 | index=%d | "
            "temperature=%.2f | vibration=%.3f",
            index,
            40.0 + index * 0.01,
            0.12,
        )