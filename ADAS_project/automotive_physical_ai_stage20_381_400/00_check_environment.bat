@echo off
cd /d %~dp0
python -c "import gymnasium,stable_baselines3,torch; print('Gymnasium:',gymnasium.__version__); print('SB3:',stable_baselines3.__version__); print('PyTorch:',torch.__version__)"
python ex381\main.py
pause
