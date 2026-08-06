@echo off
chcp 65001 > nul
cd /d "%~dp0.."
for /L %%n in (61,1,70) do (
    echo ==================================================
    echo 예제 %%n 실행
    python run_example.py %%n
    if errorlevel 1 (
        echo 예제 %%n 실행 중 오류가 발생했습니다.
        pause
    )
)
pause
