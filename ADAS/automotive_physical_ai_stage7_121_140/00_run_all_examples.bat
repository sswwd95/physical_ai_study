@echo off
setlocal
cd /d %~dp0
for /L %%N in (121,1,140) do (
  echo.
  echo ===== Running ex%%N =====
  python ex%%N\main.py
  if errorlevel 1 (
    echo FAILED: ex%%N
    exit /b 1
  )
)
echo.
echo All examples completed.
