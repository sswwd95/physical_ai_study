@echo off
chcp 65001 > nul

call conda activate semi-physical-ai

echo.
echo ============================================
echo Running all example files...
echo ============================================
echo.

for %%f in (examples\ex*.py) do (
    echo --------------------------------------------
    echo Running: %%f
    python "%%f"

    if errorlevel 1 (
        echo [FAILED] %%f
    ) else (
        echo [SUCCESS] %%f
    )

    echo.
)

echo ============================================
echo All examples finished.
echo ============================================

exit
