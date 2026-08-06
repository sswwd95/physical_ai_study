# Skydio X2 영상 객체 탐지·실시간 추적 비행 프로젝트

MuJoCo 카메라 영상에서 빨간색 표적을 탐지하고, 중심 오차와 크기를 이용해 드론을 추적 제어하는 교육용 Physical AI 프로젝트입니다.

## 기능
- RGB 입력, HSV 객체 탐지, 바운딩 박스·중심 좌표
- Alpha-Beta 추적, 이탈 감지, 재탐색
- yaw·roll·pitch·고도 제어, 안전거리 후진
- FPS·지연 측정, CSV 로그, PyMC 분석, 보고서
- StableBaselines3 PPO 제어 이득 튜닝 확장

## 설치
```bat
conda env create -f environment.yml
conda activate skydio-tracking
scripts\setup_menagerie.bat
```
새 Anaconda Prompt에서:
```bat
scripts\run_demo.bat
scripts\run_analysis.bat
```
