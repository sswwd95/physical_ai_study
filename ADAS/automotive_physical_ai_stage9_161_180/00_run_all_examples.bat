@echo off
cd /d %~dp0
for /L %%N in (161,1,180) do (
 echo ===== ex%%N =====
 python ex%%N\main.py
 if errorlevel 1 exit /b 1
)
