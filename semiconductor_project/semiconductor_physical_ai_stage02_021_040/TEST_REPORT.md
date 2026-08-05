# 검증 보고서

## 패키지 검증 결과
- Python 예제: 20개
- 예제별 라인 해설 가이드: 20개
- Python 문법 검사: 전체 통과
- 기본 센서 데이터: 300행 × 9열
- 오류 연습 데이터: 302행
- 압력 결측값: 4건
- RF 전력 결측값: 3건
- 잘못된 공정 상태: 2건
- 완전 중복: 2건

## 검증 방식
제작 환경의 전체 예제를 별도 프로세스로 연속 실행하는 과정은 실행 시간 제한으로
완료하지 못했습니다. 대신 다음 항목을 확정 검증했습니다.

1. 021~040 모든 Python 파일의 문법 컴파일
2. 예제 파일과 라인별 가이드의 개수 일치
3. 기본 데이터 스키마와 행 수
4. 실습 025에서 의도한 결측·범주 오류·중복 건수
5. Windows 실행 배치 파일과 Conda 환경 파일 포함

## 권장 실행 순서
```bat
conda env create -f environment.yml
conda activate semi-physical-ai-stage02
python generate_base_data.py
run_all_windows.bat
```
