@echo off
chcp 65001 > nul
call conda env create -f environment.yml
call conda activate semi-physical-ai-stage20
echo 환경 준비 완료
pause
