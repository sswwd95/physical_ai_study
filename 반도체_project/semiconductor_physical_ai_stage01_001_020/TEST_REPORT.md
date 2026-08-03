# 검증 보고서

## 검증 결과
- 001~020 Python 소스 20개: 문법 컴파일 검사 통과
- 001 데이터 생성, 002 데이터 구조 확인, 014 임계값 경보: 실행 확인
- 샘플 데이터: 300행, 9개 컬럼
- 합성 이상 구간: 220~234행
- 임계값 경보: 15건

## 실행 순서
```bat
conda env create -f environment.yml
conda activate semi-physical-ai
python verify_environment.py
python examples\ex001_generate_sensor_data.py
run_all_windows.bat
```

## PyMC 환경 주의
PyMC와 ArviZ는 서로 호환되는 버전이 함께 설치되어야 합니다.
기존 환경에 개별 패키지를 덮어 설치하지 말고 제공된 `environment.yml`로
새로운 conda-forge 환경을 생성하십시오.

제작 컨테이너의 전역 PyMC와 ArviZ는 상호 호환되지 않아 019~020의 샘플링
실행 검증에는 사용하지 않았습니다. 두 소스의 Python 문법과 모델 구성은
검사했으며, 깨끗한 Conda 환경에서 실행하도록 구성했습니다.
