@echo off
cd /d %~dp0
python -c "import mujoco,mujoco.viewer,numpy,pandas; print('MuJoCo:',mujoco.__version__)"
python -c "from common.traffic_utils import load_project; mj,m,d,p=load_project(); print('bodies:',m.nbody,'signal phases:',len(p))"
pause
