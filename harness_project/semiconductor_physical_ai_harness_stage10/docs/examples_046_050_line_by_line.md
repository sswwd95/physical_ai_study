# 실습 046~050 라인별 해설

## 실습 046 시간 기반 분할
1. 시계열 데이터는 과거로 학습하고 미래로 평가해야 합니다.
2. 무작위 섞기는 미래 정보가 학습에 들어가는 원인이 될 수 있습니다.
3. 60/20/20 분할은 교육용 기본값입니다.
4. 각 구간의 시작·종료 시각을 저장해 재현성을 확보합니다.
5. Lot 경계와 Recipe 경계도 실제 프로젝트에서는 고려해야 합니다.
6. 분할 후 파일을 고정하면 실험 간 비교가 쉬워집니다.

## 실습 047 데이터 누출 검사
1. train 종료 시각은 validation 시작보다 앞서야 합니다.
2. validation 종료 시각은 test 시작보다 앞서야 합니다.
3. 동일 timestamp가 여러 데이터셋에 존재하면 누출 가능성이 있습니다.
4. timestamp·Lot·Recipe는 목적에 따라 메타데이터로만 사용할 수 있습니다.
5. 누출 검사는 모델 정확도보다 먼저 수행해야 합니다.
6. 실패 항목이 있으면 학습을 중단하는 것이 안전합니다.

## 실습 048 전처리 저장·복원
1. 전처리는 학습 데이터에만 fit합니다.
2. 중앙값 대체 값과 RobustScaler 파라미터가 객체에 저장됩니다.
3. joblib은 scikit-learn 객체 저장에 편리합니다.
4. 운영 환경에서는 저장된 객체를 다시 불러옵니다.
5. 테스트·운영 데이터에는 transform만 적용합니다.
6. 특징 순서가 달라지면 결과가 잘못되므로 메타데이터로 고정합니다.

## 실습 049 스키마 검증
1. 스키마는 열 이름과 자료형의 계약입니다.
2. 필수 열 누락은 분석을 즉시 중단해야 하는 오류입니다.
3. dtype mismatch는 문자열 숫자나 날짜 파싱 실패를 찾습니다.
4. 예상 밖 열은 버전 변경이나 원천 시스템 변화를 나타낼 수 있습니다.
5. JSON 리포트는 CI와 자동화 하네스에서 사용하기 쉽습니다.
6. 값 범위 검사는 스키마 검사와 별도로 수행합니다.

## 실습 050 데이터 품질 종합 리포트
1. 결측, 범위, 시간축, 중복을 한 화면에서 봅니다.
2. 센서별 통계는 문제가 집중된 센서를 찾게 합니다.
3. 품질 점수는 교육용 요약값일 뿐 원인을 대신하지 않습니다.
4. HTML은 비개발자와 결과를 공유하기 쉽습니다.
5. 점수 계산식은 조직 정책과 공정 위험도에 맞춰 변경해야 합니다.
6. 다음 단계의 공정 모니터링은 이 품질 검사를 통과한 데이터를 사용해야 합니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_046_time_based_split.py
python examples\example_047_data_leakage_check.py
python examples\example_048_save_and_restore_preprocessor.py
python examples\example_049_schema_validation.py
python examples\example_050_data_quality_report.py

pytest -q
```
