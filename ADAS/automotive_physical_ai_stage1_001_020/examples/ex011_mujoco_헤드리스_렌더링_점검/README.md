# 예제 011 — MuJoCo 헤드리스 렌더링 점검

## 핵심 주제
GUI 없이 모델 계산이 가능한지 확인한다.

## 실행 절차

```bat
conda activate auto_physical_ai
cd /d <압축을_푼_폴더>
python examples\ex011_mujoco_헤드리스_렌더링_점검\main.py
```

## 기대 결과
오류 없이 진단 정보 또는 계산 결과가 출력됩니다. 외부 모델이 필요한 예제는 모델 경로가 없을 때 안전하게 `SKIP` 또는 안내 문구를 출력합니다.

## 초보자 체크포인트
- `python` 실행 경로가 `auto_physical_ai` 환경인지 확인합니다.
- 패키지 오류가 나면 `conda env update -f environment.yml --prune`을 실행합니다.
- 경로 문제를 줄이기 위해 압축 해제 위치에 한글과 공백을 사용하지 않는 것을 권장합니다.

## 라인별 해설
| 줄 | 코드 | 설명 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 표준/외부 모듈을 불러옵니다. |
| 2 | `import mujoco` | 필요한 표준/외부 모듈을 불러옵니다. |
| 3 | `` | 가독성을 위한 빈 줄입니다. |
| 4 | `xml = Path(__file__).resolve().parents[2] / "common" / "minimal_car.xml"` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 5 | `model = mujoco.MjModel.from_xml_path(str(xml))` | MJCF XML 파일을 읽어 MuJoCo 모델로 컴파일합니다. |
| 6 | `data = mujoco.MjData(model)` | 변수에 값, 객체 또는 계산 결과를 저장합니다. |
| 7 | `for _ in range(10):` | 여러 항목 또는 여러 시뮬레이션 스텝을 반복합니다. |
| 8 | `    mujoco.mj_step(model, data)` | 물리 시뮬레이션을 한 타임스텝 전진시킵니다. |
| 9 | `print("headless simulation OK; time=", data.time)` | 실행 결과나 진단 정보를 화면에 출력합니다. |
| 10 | `print("GUI는 별도 예제에서 mujoco.viewer를 사용합니다.")` | 실행 결과나 진단 정보를 화면에 출력합니다. |
