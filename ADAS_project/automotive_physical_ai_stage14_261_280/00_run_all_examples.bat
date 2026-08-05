@echo off
setlocal
cd /d %~dp0
for /L %%N in (261,1,280) do (
  echo.
  echo ===== Running ex%%N =====
  python ex%%N\main.py
  if errorlevel 1 exit /b 1
)
echo All examples completed.
