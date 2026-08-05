@echo off
cd /d %~dp0
python -c "import numpy,pandas,matplotlib,sklearn; print(numpy.__version__,pandas.__version__,sklearn.__version__)"
python ex341\main.py
python ex359\main.py
pause
