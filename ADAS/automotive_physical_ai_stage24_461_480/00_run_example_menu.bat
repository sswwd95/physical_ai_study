@echo off
cd /d %~dp0
set /p EXAMPLE=Enter example number 461-480:
python ex%EXAMPLE%\main.py
pause
