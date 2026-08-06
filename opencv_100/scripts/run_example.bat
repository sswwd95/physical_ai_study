@echo off
chcp 65001 > nul
cd /d "%~dp0.."
set /p EXAMPLE=실행할 예제 번호를 입력하세요 (1-100): 
python run_example.py %EXAMPLE%
pause
