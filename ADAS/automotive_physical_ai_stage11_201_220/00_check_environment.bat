@echo off
cd /d %~dp0
python -c "import sys,numpy,pandas,matplotlib,sklearn; print('Python:',sys.version); print('NumPy:',numpy.__version__); print('Pandas:',pandas.__version__); print('scikit-learn:',sklearn.__version__)"
python ex201\main.py
pause
