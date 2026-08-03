@echo off
chcp 65001 > nul
call conda env create -f environment.yml
call conda activate semi-physical-ai-stage02
python generate_base_data.py
echo 환경과 기본 데이터 준비가 완료되었습니다.
pause
