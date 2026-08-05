import os, sys

print("python version:", sys.version)
print("executable:", sys.executable)
print("conda env:", os.getenv("CONDA_DEFAULT_ENV"))
assert sys.version_info[:2] == (3, 11), "Python 3.11 환경을 권장합니다."
