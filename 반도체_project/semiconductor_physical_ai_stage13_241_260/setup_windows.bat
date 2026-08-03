@echo off
chcp 65001 > nul
call conda env create -f environment.yml
call conda activate semi-physical-ai-stage13
python verify_environment.py
pause
