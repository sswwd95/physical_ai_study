@echo off
cd /d %~dp0
python -c "import gymnasium,numpy,pandas; print('Gymnasium:',gymnasium.__version__)"
python ex361\main.py
python ex377\main.py
pause
