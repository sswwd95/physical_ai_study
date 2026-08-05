# 실습 378 — run_manifest

## 1. 학습 목표
실행 이력과 산출물 manifest를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
실행ID·입력파일·산출물목록이 포함된 manifest를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage19
python examples\ex378_run_manifest.py
```

## 4. 예상 결과
요청한 시스템 통합·운영 자동화 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import json` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import logging` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `DATA_FILE = ROOT / "data" / "operations_stream.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `CONFIG_FILE = ROOT / "config" / "app_config.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 10 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 11 | `LOG_DIR = ROOT / "logs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 12 | `MODEL_DIR = ROOT / "models"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 13 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 14 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 15 | `LOG_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `MODEL_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 18 | `from datetime import datetime` | 필요한 라이브러리를 불러옵니다. |
| 19 | `artifacts=[]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `for path in sorted(OUTPUT_DIR.glob("*")):` | 여러 파일·배치·장비를 반복 처리합니다. |
| 21 | `    if path.is_file():` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 22 | `        artifacts.append({` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 23 | `            "file":path.name,` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 24 | `            "size_bytes":path.stat().st_size,` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 25 | `            "modified_time":datetime.fromtimestamp(path.stat().st_mtime).isoformat()` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 26 | `        })` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 27 | `manifest={` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    "run_id":datetime.now().strftime("RUN_%Y%m%d_%H%M%S"),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 29 | `    "input_file":str(DATA_FILE.relative_to(ROOT)),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 30 | `    "artifact_count":len(artifacts),` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 31 | `    "artifacts":artifacts` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 32 | `}` | 시스템 통합 또는 운영 자동화 단계를 수행합니다. |
| 33 | `manifest_file=OUTPUT_DIR/"ex378_run_manifest.json"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `manifest_file.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `print(manifest_file.read_text(encoding="utf-8"))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 설정·로그·모델·출력 파일 경로가 분리되어 있는가?
2. 실패 시 재실행과 복구 절차가 준비되어 있는가?
3. 운영 KPI와 경보가 담당자 행동으로 연결되는가?