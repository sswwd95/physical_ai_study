from __future__ import annotations
import os, platform, struct
from pathlib import Path

print("OS:", platform.platform())
print("64-bit:", struct.calcsize("P") * 8 == 64)
print("CPU cores:", os.cpu_count())
print("Home:", Path.home())
print("ASCII project path recommended:", Path.cwd())
