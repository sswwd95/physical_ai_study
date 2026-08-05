@echo off
setlocal
cd /d %~dp0
for /L %%N in (41,1,60) do (
  set NUM=00%%N
  call set NUM=%%NUM:~-3%%
  echo ===== Running ex%%NUM%% =====
  python ex%%NUM%%\main.py
  if errorlevel 1 exit /b 1
)
echo All examples completed successfully.
