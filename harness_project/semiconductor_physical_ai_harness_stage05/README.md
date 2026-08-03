# 반도체 Physical AI 하네스 엔지니어링 — 5단계

실습 021~025는 반도체 장비 센서 데이터의 결측값 탐지와 처리 품질 검증을 다룹니다.

## 포함 내용
- 센서별 결측 개수·결측률
- 결측 센서 조합과 연속 결측 블록
- 전방·후방 채우기
- 선형 보간
- 중앙값 채우기를 포함한 처리 품질 비교
- 완전 데이터와 결측 주입 데이터
- Antigravity용 생성·검증 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_021_detect_missing_values.py
python examples\example_022_analyze_missing_patterns.py
python examples\example_023_forward_backward_fill.py
python examples\example_024_linear_interpolation.py
python examples\example_025_compare_imputation_quality.py

pytest -q
```

## 주의
결측 처리 결과는 교육용 합성 데이터에서 비교합니다. 실제 설비 데이터에서는 결측 발생 원인, 공정 단계, 센서 응답속도와 안전 기준을 함께 검토해야 합니다.
