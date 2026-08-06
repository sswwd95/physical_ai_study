"""OpenCV 실습 예제

초보자용 상세 주석판입니다.

읽는 순서:
1. 위에서 아래로 주석을 먼저 읽습니다.
2. 바로 아래 코드가 어떤 작업을 하는지 확인합니다.
3. 실행 후 나타나는 창이나 터미널 결과를 비교합니다.

실행 위치: 이 프로젝트의 opencv_100 폴더
주의: cv2.imshow()가 있는 예제는 화면 창에서 아무 키나 눌러야 종료됩니다.
"""

# 이 예제에서 필요한 외부 기능을 불러오기
from __future__ import annotations

# 이 예제에서 필요한 외부 기능을 불러오기
import argparse
import runpy
# 파일과 폴더 경로를 안전하게 다루기 위한 기능을 불러오기
from pathlib import Path

# ROOT 변수에 이후 처리에 사용할 값을 저장
ROOT = Path(__file__).resolve().parent


# example_path 작업을 반복해서 사용할 수 있도록 함수로 정의함
def example_path(number: int) -> Path:
    # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
    if not 1 <= number <= 100:
        raise ValueError("예제 번호는 1~100이어야 합니다.")
    # stage 변수에 이후 처리에 사용할 값을 저장
    stage = (number - 1) // 10 + 1
    # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
    return ROOT / f"stage{stage:02d}" / f"ex{number:03d}.py"


# 프로그램 실행 순서를 담당하는 main 함수를 정의함
def main() -> None:
    # parser 변수에 이후 처리에 사용할 값을 저장
    parser = argparse.ArgumentParser(description="OpenCV 100제 예제 실행기")
    parser.add_argument("number", type=int, help="실행할 예제 번호(1~100)")
    # args 변수에 이후 처리에 사용할 값을 저장
    args = parser.parse_args()
    # path 변수에 이후 처리에 사용할 값을 저장
    path = example_path(args.number)
    # 현재 상태 또는 계산 결과의 터미널 출력
    print(f"실행: {path.relative_to(ROOT)}")
    runpy.run_path(str(path), run_name="__main__")


# 이 파일을 직접 실행했을 때만 main 함수를 호출하도록 확인
if __name__ == "__main__":
    main()
