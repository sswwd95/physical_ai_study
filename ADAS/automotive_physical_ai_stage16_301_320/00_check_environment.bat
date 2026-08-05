@echo off
cd /d %~dp0
python -c "import sys,numpy,pandas,matplotlib; print('Python:',sys.version); print('NumPy:',numpy.__version__); print('Pandas:',pandas.__version__)"
python ex301\main.py
python ex319\main.py
pause
