@echo off
cd /d "%~dp0"

set /p EXAMPLE=Enter example number 521-540:

python -m ex%EXAMPLE%.main

pause
