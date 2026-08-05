@echo off
cd /d "%~dp0"

set /p EXAMPLE=Enter example number 501-520:

python -m ex%EXAMPLE%.main

pause