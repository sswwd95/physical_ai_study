@echo off
cd /d %~dp0
python -c "import sys,mujoco; print('Python:',sys.version); print('MuJoCo:',mujoco.__version__)"
python ex102\main.py
pause
