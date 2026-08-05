@echo off
cd /d %~dp0
python -c "import numpy,pandas,sklearn; print(numpy.__version__,pandas.__version__,sklearn.__version__)"
python ex221\main.py
pause
