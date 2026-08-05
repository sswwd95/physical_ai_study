@echo off
setlocal
chcp 65001 > nul

echo [1/5] Conda 확인
where conda || (echo Anaconda Prompt에서 실행하세요. & exit /b 1)

echo [2/5] 기존 환경 제거 여부는 사용자가 직접 결정합니다.
call conda env create -f environment.yml
if errorlevel 1 exit /b 1

echo [3/5] 환경 활성화
call conda activate auto_physical_ai
if errorlevel 1 exit /b 1

echo [4/5] 커널 등록
python -m ipykernel install --user --name auto_physical_ai --display-name "Python (auto_physical_ai)"

echo [5/5] 진단 실행
python common\diagnose_environment.py
endlocal
