# 검증 보고서

## 검증 결과
- Python 예제: 20개
- 라인별 해설 가이드: 20개
- Python 문법 검사: 전체 통과
- 기본 센서 데이터: 300행 × 9열
- 관리도 그래프 출력 예제: 046, 047
- Excel 자동 보고서 예제: 060
- 하네스 프롬프트: 20개
- 환경 파일과 Windows 실행 배치 파일 포함

## 권장 실행 순서
```bat
conda env create -f environment.yml
conda activate semi-physical-ai-stage03
run_all_windows.bat
```

## 주의사항
관리한계와 규격한계는 서로 다른 기준입니다. 본 실습의 규격값과 관리도 상수는
교육용 예시이며 실제 반도체 공정에서는 승인된 공정 사양과 품질 기준을 사용해야 합니다.
