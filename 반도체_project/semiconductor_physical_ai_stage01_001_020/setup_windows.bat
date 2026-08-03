@echo off
chcp 65001 > nul
echo [1/3] Conda 환경을 생성합니다.
call conda env create -f environment.yml
echo [2/3] 환경을 활성화합니다.
call conda activate semi-physical-ai
echo [3/3] 샘플 데이터를 생성합니다.
python examples\ex001_generate_sensor_data.py
echo 설치가 완료되었습니다.
pause
