@echo off
chcp 65001 > nul
call conda env create -f environment.yml
call conda activate semi-physical-ai-stage03
echo 환경 준비가 완료되었습니다.
pause
