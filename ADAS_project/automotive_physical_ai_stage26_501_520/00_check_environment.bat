@echo off
cd /d %~dp0
python -c "import mujoco,mujoco.viewer,numpy,pandas; print('MuJoCo:',mujoco.__version__)"
python scripts\02_validate_official_model.py
pause
