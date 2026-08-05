@echo off
setlocal
cd /d %~dp0
for /L %%N in (141,1,160) do (
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
