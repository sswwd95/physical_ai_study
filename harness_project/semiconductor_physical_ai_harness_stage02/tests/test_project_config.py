from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "config" / "project_config.yaml"

def load_config():
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def test_required_sections_exist():
    config = load_config()
    for section in ("project", "paths", "sampling", "monitoring"):
        assert section in config

def test_random_seed_is_integer():
    config = load_config()
    assert isinstance(config["project"]["random_seed"], int)

def test_monitoring_limits_are_valid():
    config = load_config()
    for sensor, limits in config["monitoring"].items():
        assert limits["low"] < limits["high"], sensor
