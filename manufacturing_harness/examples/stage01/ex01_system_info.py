import os
import platform
import sys
from pathlib import Path


def print_system_info() -> None:
    """현재 Python 실행 환경의 기본 정보를 출력한다."""

    # 구분선 출력
    print("=" * 50)
    # 제목 출력
    print("제조 Physical AI 실행 환경")
    print("=" * 50)

    # 운영체제 이름 출력 (예: Windows, Linux, Darwin)
    print(f"운영체제       : {platform.system()}")
    # 운영체제 세부 빌드/버전 정보 출력
    print(f"운영체제 버전  : {platform.version()}")
    # 파이썬 인터프리터 버전 출력 (예: 3.11.15)
    print(f"Python 버전    : {platform.python_version()}")
    # 실행 중인 파이썬 인터프리터 파일의 절대 경로 출력
    print(f"Python 실행파일: {sys.executable}")
    # 현재 작업 디렉터리(Current Working Directory) 경로 출력
    print(f"현재 작업 폴더 : {Path.cwd()}")
    # OS에서 할당한 현재 프로세스 ID(PID) 출력
    print(f"프로세스 ID    : {os.getpid()}")


if __name__ == "__main__":
    print_system_info()
    
# ==================================================
# 제조 Physical AI 실행 환경
# ==================================================
# 운영체제       : Windows
# 운영체제 버전  : 10.0.19045
# Python 버전    : 3.11.15
# Python 실행파일: C:\Users\sswwd\anaconda3\envs\manufac\python.exe
# 현재 작업 폴더 : C:\work
# 프로세스 ID    : 18740

