@echo off
setlocal
cd /d %~dp0
for /L %%N in (61,1,80) do (
  echo.
  echo ===== Running ex0%%N =====
  python ex0%%N\main.py
  if errorlevel 1 (
    echo FAILED: ex0%%N
    exit /b 1
  )
)
echo.
echo All examples completed.
