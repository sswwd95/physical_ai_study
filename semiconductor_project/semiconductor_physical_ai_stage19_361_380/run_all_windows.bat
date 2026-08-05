@echo off
chcp 65001 > nul
call conda activate semi-physical-ai-stage19
for %%f in (examples\ex*.py) do (
  echo ==================================================
  echo 실행: %%f
  python "%%f"
)
pause
