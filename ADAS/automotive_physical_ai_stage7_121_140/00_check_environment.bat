@echo off
cd /d %~dp0
python -c "import sys,numpy,pandas,matplotlib; print('Python:',sys.version); print('NumPy:',numpy.__version__); print('Pandas:',pandas.__version__); print('Matplotlib:',matplotlib.__version__)"
python ex121\main.py
pause
