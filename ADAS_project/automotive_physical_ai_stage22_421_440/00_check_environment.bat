@echo off
cd /d %~dp0
python -c "import mujoco,mujoco.viewer,numpy,pandas; print('MuJoCo:',mujoco.__version__)"
python -c "from common.project_viewer_utils import load_project; mj,m,d,p=load_project(); print('model:',m.nbody,'bodies, path:',len(p),'points')"
pause
