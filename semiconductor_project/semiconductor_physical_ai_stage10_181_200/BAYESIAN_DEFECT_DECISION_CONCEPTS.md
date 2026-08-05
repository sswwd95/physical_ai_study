# 베이지안 불량률·의사결정 핵심

## 베타-이항
- p ~ Beta(alpha, beta)
- defect_count ~ Binomial(wafer_count, p)

## 비교 지표
- 절대 차이: p_B - p_A
- 상대위험도: p_B / p_A
- 목표 초과확률: P(p > target)

## 비용 기반 의사결정
- 행동별 비용함수를 정의
- 각 사후표본에서 행동별 비용 계산
- 기대비용이 가장 작은 행동 선택
- 단, 안전·품질 승인 절차가 우선
