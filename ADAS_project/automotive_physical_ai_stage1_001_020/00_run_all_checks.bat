@echo off
setlocal
chcp 65001 > nul
call conda activate auto_physical_ai
python common\diagnose_environment.py
python common\locate_tb3_model.py
python examples\ex010_mujoco_minimal_model\main.py
python examples\ex014_pymc_coin_test\main.py
python examples\ex020_integrated_smoke_test\main.py
endlocal
