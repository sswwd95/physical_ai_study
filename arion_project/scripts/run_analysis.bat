@echo off
cd /d %~dp0\..
python -m src.analysis
python -m src.reporting
