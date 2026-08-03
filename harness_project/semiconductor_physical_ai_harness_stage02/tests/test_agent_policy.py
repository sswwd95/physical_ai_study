from pathlib import Path
import json
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "examples" / "example_010_safe_agent_workspace.py"
POLICY_PATH = PROJECT_ROOT / "outputs" / "agent_safety_policy.json"

def test_agent_policy_is_created():
    subprocess.run([sys.executable, str(SCRIPT)], check=True)
    assert POLICY_PATH.exists()

def test_forbidden_actions_include_external_write():
    data = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    joined = " ".join(data["forbidden_actions"])
    assert "프로젝트 루트 밖" in joined
