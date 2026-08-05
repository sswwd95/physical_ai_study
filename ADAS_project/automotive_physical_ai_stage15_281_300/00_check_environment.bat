@echo off
cd /d %~dp0
python -c "import pymc,arviz,numpy,pandas; print('PyMC:',pymc.__version__); print('ArviZ:',arviz.__version__)"
python ex281\main.py
pause
