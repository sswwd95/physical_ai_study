@echo off
cd /d %~dp0\..
python -m src.main --input voice --viewer
