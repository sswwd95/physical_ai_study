@echo off
chcp 65001 > nul

call conda activate semi-physical-ai

echo.
echo ============================================
echo Running all example files...
echo ============================================
echo.

for %%f in (examples\ex*.py) do (
    echo Running %%f
    python "%%f"
    echo.
)

echo ============================================
echo All examples finished.
echo ============================================

pause
