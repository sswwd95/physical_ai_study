@echo off
setlocal
cd /d %~dp0
for /L %%N in (361,1,380) do (
  echo.
  echo ===== Running ex%%N =====
  python ex%%N\main.py
  if errorlevel 1 exit /b 1
)
echo All examples completed.
