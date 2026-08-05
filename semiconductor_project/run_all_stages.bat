@echo off
chcp 65001 > nul
setlocal EnableDelayedExpansion

rem 실행을 시작할 폴더
set "START_FOLDER=%~1"

if not defined START_FOLDER (
    set "START_FOLDER=semiconductor_physical_ai_stage07_121_140"
)

set "START_EXECUTION=0"

echo.
echo ============================================
echo 모든 프로젝트 실행을 시작합니다.
echo 시작 폴더: %START_FOLDER%
echo ============================================
echo.

for /d %%d in (semiconductor_physical_ai_sta*) do (

    rem 지정한 폴더를 만나면 실행 시작
    if /i "%%d"=="%START_FOLDER%" (
        set "START_EXECUTION=1"
    )

    if "!START_EXECUTION!"=="1" (
        if exist "%%d\run_all_windows.bat" (
            echo.
            echo ============================================
            echo 실행 중: %%d
            echo ============================================

            pushd "%%d"
            call run_all_windows.bat
            set "RESULT=!ERRORLEVEL!"
            popd

            if "!RESULT!"=="0" (
                echo 완료: %%d
            ) else (
                echo 오류 발생: %%d
                echo 종료 코드: !RESULT!
            )
        ) else (
            echo 건너뜀: %%d 안에 run_all_windows.bat 파일이 없습니다.
        )
    ) else (
        echo 이전 단계 건너뜀: %%d
    )
)

if "!START_EXECUTION!"=="0" (
    echo.
    echo 오류: 시작 폴더를 찾지 못했습니다.
    echo 입력한 폴더: %START_FOLDER%
    echo 폴더 이름을 정확히 확인해 주세요.
)

echo.
echo ============================================
echo 모든 프로젝트 실행이 완료되었습니다.
echo ============================================
echo 창을 닫으려면 아무 키나 누르세요.

endlocal
pause >nul