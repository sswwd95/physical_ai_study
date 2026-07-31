from pathlib import Path

from src.harness.logging_config import setup_logger, log_temperature_state



if __name__ == "__main__":
    logger = setup_logger(Path("logs"))

    test_temperatures = [
        52.3,
        66.5,
        76.2,
    ]

    for value in test_temperatures:
        state = log_temperature_state(
            logger=logger,
            temperature=value,
            warning_limit=65.0,
            critical_limit=75.0,
        )

        print(f"{value}℃ 상태: {state}")
