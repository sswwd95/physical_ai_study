# 자동차 Physical AI 하네스 엔지니어링 — 1단계 001~020제

대상: ROS 2 Humble 강의 전, 전공자·비전공자 혼합 취업 준비생  
환경: Windows 10 64-bit / Anaconda / Google Antigravity / MuJoCo 3.6.0 / PyMC / ROBOTIS `robotis_mujoco_menagerie`의 `robotis_tb3`

## 설치 순서

1. Anaconda Distribution 또는 Miniconda를 설치합니다.
2. **Anaconda Prompt**를 엽니다.
3. 이 폴더로 이동합니다: `cd /d C:\work\automotive_physical_ai_stage1_001_020`
4. `conda env create -f environment.yml`
5. `conda activate auto_physical_ai`
6. `python common\diagnose_environment.py`
7. 선택: ROBOTIS 저장소를 별도 폴더에 준비하고 환경변수를 설정합니다.

```bat
set ROBOTIS_MUJOCO_MENAGERIE=C:\work\robotis_mujoco_menagerie
python common\locate_tb3_model.py
```

영구 환경변수는 Windows 사용자 환경변수 화면에서 추가하는 방법을 권장합니다. 저장소 안의 `robotis_tb3` 폴더가 존재해야 합니다.

## Antigravity 안전 설정

- 프로젝트 폴더만 Workspace로 엽니다.
- 터미널 명령 자동 실행은 승인 방식으로 사용합니다.
- `AGENTS.md`의 안전 규칙을 유지합니다.
- 삭제·이동·환경 제거 명령은 실행 전에 사람이 확인합니다.
- 생성 코드가 끝나면 `00_run_all_checks.bat`로 검증합니다.

## 전체 실습 목록

| 번호 | 핵심 주제 | 실행 파일 |
|---:|---|---|
| 001 | Windows 사전 점검 | `examples/ex001_windows_사전_점검/main.py` |
| 002 | Conda 설치 확인 | `examples/ex002_conda_설치_확인/main.py` |
| 003 | 프로젝트 폴더 생성 | `examples/ex003_프로젝트_폴더_생성/main.py` |
| 004 | Conda 환경 파일 검사 | `examples/ex004_conda_환경_파일_검사/main.py` |
| 005 | Python 실행기 확인 | `examples/ex005_python_실행기_확인/main.py` |
| 006 | 필수 패키지 가져오기 | `examples/ex006_필수_패키지_가져오기/main.py` |
| 007 | MuJoCo 3.6.0 검증 | `examples/ex007_mujoco_3_6_0_검증/main.py` |
| 008 | PyMC 검증 | `examples/ex008_pymc_검증/main.py` |
| 009 | Antigravity 작업공간 준비 | `examples/ex009_antigravity_작업공간_준비/main.py` |
| 010 | 최소 MuJoCo 모델 로드 | `examples/ex010_최소_mujoco_모델_로드/main.py` |
| 011 | MuJoCo 헤드리스 렌더링 점검 | `examples/ex011_mujoco_헤드리스_렌더링_점검/main.py` |
| 012 | TurtleBot3 저장소 경로 설정 | `examples/ex012_turtlebot3_저장소_경로_설정/main.py` |
| 013 | TurtleBot3 XML 로드 점검 | `examples/ex013_turtlebot3_xml_로드_점검/main.py` |
| 014 | PyMC 동전 확률 추정 | `examples/ex014_pymc_동전_확률_추정/main.py` |
| 015 | 센서 평균 베이지안 추정 | `examples/ex015_센서_평균_베이지안_추정/main.py` |
| 016 | ArviZ 요약 확인 | `examples/ex016_arviz_요약_확인/main.py` |
| 017 | 데이터 폴더 쓰기 점검 | `examples/ex017_데이터_폴더_쓰기_점검/main.py` |
| 018 | 재현성 시드 점검 | `examples/ex018_재현성_시드_점검/main.py` |
| 019 | 환경 보고서 생성 | `examples/ex019_환경_보고서_생성/main.py` |
| 020 | 통합 스모크 테스트 | `examples/ex020_통합_스모크_테스트/main.py` |

## 권장 진행

001~009로 OS·Conda·IDE를 준비하고, 010~013으로 MuJoCo와 TurtleBot3 모델을 점검한 뒤, 014~016으로 PyMC 샘플링을 확인합니다. 017~020은 데이터 저장, 재현성, 보고서, 통합 테스트입니다.

## 주의

- `mujoco-py`가 아니라 공식 `mujoco` Python 패키지를 사용합니다.
- ROS 2 Humble 자체는 이 단계에서 설치하지 않습니다. 이 단계의 목적은 ROS 2 강의 전 데이터·시뮬레이션·베이즈 통계 기반을 마련하는 것입니다.
- `robotis_tb3` 저장소 구조가 변경되면 `common/locate_tb3_model.py`의 후보 파일명을 조정할 수 있습니다.
