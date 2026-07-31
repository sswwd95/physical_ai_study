from pathlib import Path

from src.harness.logging_config import (
    setup_logger,
    run_sensor_analysis,
)


if __name__ == "__main__":
    logger = setup_logger(Path("logs"))

    result = run_sensor_analysis(
        logger=logger,
        sensor_values=[],
    )

    print(result)
