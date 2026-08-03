"""
반도체 Physical AI 하네스 엔지니어링 실습 006~010
Windows 10 / Anaconda / PyMC / Antigravity
"""

from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "agent_safety_policy.json"

# 1. 코딩 에이전트가 지켜야 할 작업 경계를 정의한다.
policy = {
    "workspace_root": str(PROJECT_ROOT),
    "allowed_write_paths": [
        str(PROJECT_ROOT / "examples"),
        str(PROJECT_ROOT / "tests"),
        str(PROJECT_ROOT / "outputs"),
        str(PROJECT_ROOT / "logs"),
        str(PROJECT_ROOT / "docs"),
    ],
    "forbidden_actions": [
        "프로젝트 루트 밖 파일 수정 또는 삭제",
        "실제 반도체 장비에 제어 명령 전송",
        "인터록 또는 안전 장치 우회",
        "검증되지 않은 공정 레시피 적용",
        "사용자 승인 없이 패키지 또는 시스템 설정 변경",
        "원본 생산 데이터 덮어쓰기",
    ],
    "required_behaviors": [
        "변경 전 대상 파일 목록 제시",
        "기존 파일은 백업 또는 새 파일명으로 보존",
        "코드 생성 후 자동 테스트 실행",
        "실패 시 변경 내용을 되돌릴 수 있도록 로그 기록",
        "합성 데이터 또는 비식별 데이터 우선 사용",
    ],
}

# 2. 허용된 쓰기 경로가 프로젝트 내부인지 확인한다.
project_root_resolved = PROJECT_ROOT.resolve()

for allowed_path_text in policy["allowed_write_paths"]:
    allowed_path = Path(allowed_path_text).resolve()
    if project_root_resolved not in allowed_path.parents:
        raise ValueError(
            f"허용 경로가 프로젝트 밖에 있습니다: {allowed_path}"
        )

# 3. 정책을 JSON 파일로 저장한다.
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text(
    json.dumps(policy, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print("[완료] Antigravity 안전 작업 정책 생성")
print("정책 파일:", OUTPUT_PATH)
