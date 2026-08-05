@echo off
python -c "import mujoco,mujoco.viewer; print(mujoco.__version__)"
python -c "from common.adas_tb3_utils import repo,burger_model; print(repo()); print(burger_model())"
pause
