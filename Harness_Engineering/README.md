# 가상환경
- physical_ai

# 개발 환경

| 구분 | 내용 |
|---|---|
| 운영체제 | Windows 10 64-bit |
| Python 관리 | Anaconda |
| Python 버전 | Python 3.10 |
| 물리 시뮬레이터 | MuJoCo 3.6.0 |
| 로봇 모델 | MuJoCo Menagerie Franka Emika Panda |
| 강화학습 | Stable-Baselines3 |
| 환경 API | Gymnasium |
| 데이터 분석 | NumPy, Pandas, Matplotlib, Scikit-learn |
| 개발 도구 | Antigravity |
| 향후 연동 | ROS2 Humble |

# Project Structure

```text
manufacturing_harness/
│
├─ configs/
│  ├─ base.yaml
│  ├─ simulation.yaml
│  └─ training.yaml
│
├─ assets/
│  └─ mujoco_menagerie/
│     └─ franka_emika_panda/
│
├─ data/
│  ├─ raw/
│  ├─ processed/
│  └─ results/
│
├─ logs/
├─ models/
├─ reports/
├─ tests/
│
├─ src/
│  ├─ harness/
│  ├─ simulation/
│  ├─ sensors/
│  ├─ monitoring/
│  ├─ maintenance/
│  ├─ quality/
│  ├─ collaboration/
│  ├─ rl/
│  └─ digital_twin/
│
├─ examples/
│  ├─ stage01/
│  ├─ stage02/
│  └─ ...
│
├─ requirements.txt
└─ README.md
```