from pathlib import Path

root = Path.cwd()
rules = root / "AGENTS.md"
rules.write_text("""# Project rules
- Never delete files outside this project.
- Ask before running destructive commands.
- Use the auto_physical_ai conda environment.
- Run smoke tests after code changes.
- Keep MuJoCo pinned to 3.6.0.
""", encoding="utf-8")
print("written:", rules.resolve())
