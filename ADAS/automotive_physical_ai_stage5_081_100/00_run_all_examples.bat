@echo off
setlocal
cd /d %~dp0
for /L %%N in (81,1,99) do (
  echo ===== Running ex0%%N =====
  python ex0%%N\main.py
  if errorlevel 1 exit /b 1
)
echo ===== Running ex100 =====
python ex100\main.py
if errorlevel 1 exit /b 1
echo All examples completed.
