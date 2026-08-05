@echo off
cd /d %~dp0
python -c "import pymc,arviz; print(pymc.__version__,arviz.__version__)"
python ex161\main.py
pause
