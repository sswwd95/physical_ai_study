from pathlib import Path
from src.harness.logging_config import setup_json_logger



if __name__ == "__main__":
    logger = setup_json_logger(
        Path("logs/json/manufacturing.jsonl")
    )

    logger.info(
        "Panda 로봇 사이클 완료",
        extra={
            "extra_fields": {
                "robot_id": "panda_01",
                "cycle_id": 105,
                "cycle_time_seconds": 28.4,
                "product_id": "part_A",
                "success": True,
            }
        },
    )