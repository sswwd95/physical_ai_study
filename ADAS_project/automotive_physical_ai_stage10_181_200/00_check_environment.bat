@echo off
cd /d %~dp0
python -c "import pymc,arviz,numpy,pandas; print('PyMC:',pymc.__version__); print('ArviZ:',arviz.__version__); print('NumPy:',numpy.__version__); print('Pandas:',pandas.__version__)"
python ex181\main.py
pause
