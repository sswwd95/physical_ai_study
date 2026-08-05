@echo off
cd /d %~dp0
for /L %%N in (221,1,240) do (
 echo ===== ex%%N =====
 python ex%%N\main.py
 if errorlevel 1 exit /b 1
)
