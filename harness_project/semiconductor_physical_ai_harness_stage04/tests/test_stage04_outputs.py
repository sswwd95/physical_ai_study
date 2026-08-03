from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
def test_dashboard():
 subprocess.run([sys.executable,str(ROOT/'examples'/'example_020_basic_process_dashboard.py')],check=True)
 p=ROOT/'outputs'/'basic_process_dashboard.html'; assert p.exists(); assert '불량률' in p.read_text(encoding='utf-8')
