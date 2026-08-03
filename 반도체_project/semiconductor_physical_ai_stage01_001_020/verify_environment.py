import importlib
import sys

packages = ["numpy", "pandas", "matplotlib", "scipy", "pymc", "arviz"]
print("Python:", sys.version)

failed = []
for package_name in packages:
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {package_name}: {version}")
    except Exception as error:
        failed.append((package_name, str(error)))
        print(f"[FAIL] {package_name}: {error}")

if failed:
    raise SystemExit(
        "패키지 호환성 문제가 있습니다. 기존 환경을 수정하지 말고 "
        "environment.yml로 새 Conda 환경을 생성하세요."
    )

print("환경 점검을 통과했습니다.")
