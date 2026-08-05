@echo off
setlocal
cd /d %~dp0\..
if not exist vendor mkdir vendor
if exist vendor\robotis_mujoco_menagerie (
  echo Repository already exists.
) else (
  git clone https://github.com/ROBOTIS-GIT/robotis_mujoco_menagerie.git vendor\robotis_mujoco_menagerie
  if errorlevel 1 (
    echo Clone failed. Check Git installation and network.
    exit /b 1
  )
)
set ROBOTIS_MENAGERIE_ROOT=%CD%\vendor\robotis_mujoco_menagerie
echo ROBOTIS_MENAGERIE_ROOT=%ROBOTIS_MENAGERIE_ROOT%
python scripts\02_validate_official_model.py
pause
