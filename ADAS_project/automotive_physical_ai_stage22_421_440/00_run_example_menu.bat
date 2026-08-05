@echo off
cd /d %~dp0
set /p EXAMPLE=Enter example number 421-440:
python ex%EXAMPLE%\main.py
pause
