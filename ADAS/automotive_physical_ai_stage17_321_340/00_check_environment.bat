@echo off
cd /d %~dp0
python -c "import numpy,pandas,matplotlib; print(numpy.__version__,pandas.__version__)"
python ex321\main.py
python ex339\main.py
pause
