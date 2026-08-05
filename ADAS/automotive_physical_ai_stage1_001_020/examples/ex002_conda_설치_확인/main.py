from __future__ import annotations
import os, shutil, subprocess

conda = shutil.which("conda")
print("conda path:", conda)
print("active env:", os.getenv("CONDA_DEFAULT_ENV", "not activated"))
if conda:
    result = subprocess.run([conda, "--version"], capture_output=True, text=True)
    print(result.stdout.strip() or result.stderr.strip())
else:
    print("Anaconda Prompt에서 실행하세요.")
