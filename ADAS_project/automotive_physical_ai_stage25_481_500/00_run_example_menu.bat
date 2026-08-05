@echo off
cd /d %~dp0
set /p EXAMPLE=Enter example number 481-500:
python ex%EXAMPLE%\main.py
pause
