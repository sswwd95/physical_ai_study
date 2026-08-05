@echo off
cd /d %~dp0\..
if not exist vendor mkdir vendor
if not exist vendor\robotis_mujoco_menagerie git clone https://github.com/ROBOTIS-GIT/robotis_mujoco_menagerie.git vendor\robotis_mujoco_menagerie
pause
