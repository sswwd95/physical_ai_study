# 반도체 Physical AI 하네스 엔지니어링
## 14단계: 261~280제 — 반도체 공정 조건별 품질 비교와 베이지안 실험분석

### 실행
```bat
cd semiconductor_physical_ai_stage14_261_280
conda env create -f environment.yml
conda activate semi-physical-ai-stage14
python verify_environment.py
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 261 | experiment_data_profile | 실험 조건별 품질 분포를 확인합니다. | `examples/ex261_experiment_data_profile.py` |
| 262 | recipe_ab_uniformity | 두 레시피의 균일도 차이를 베이지안 A/B로 비교합니다. | `examples/ex262_recipe_ab_uniformity.py` |
| 263 | recipe_ab_defect_rate | 두 레시피의 불량률을 베타-이항 모형으로 비교합니다. | `examples/ex263_recipe_ab_defect_rate.py` |
| 264 | three_recipe_means | 세 레시피 평균 균일도를 동시에 추정합니다. | `examples/ex264_three_recipe_means.py` |
| 265 | pairwise_superiority | 모든 레시피 쌍의 우월확률을 계산합니다. | `examples/ex265_pairwise_superiority.py` |
| 266 | effect_size_rope | 효과크기와 ROPE로 실질적 차이를 판단합니다. | `examples/ex266_effect_size_rope.py` |
| 267 | chamber_block_effect | 챔버 블록 효과를 포함한 품질 비교를 수행합니다. | `examples/ex267_chamber_block_effect.py` |
| 268 | pressure_level_effect | 압력 수준별 품질 효과를 추정합니다. | `examples/ex268_pressure_level_effect.py` |
| 269 | rf_level_effect | RF 수준별 균일도·식각률 효과를 추정합니다. | `examples/ex269_rf_level_effect.py` |
| 270 | recipe_pressure_interaction | 레시피와 압력의 교호작용을 추정합니다. | `examples/ex270_recipe_pressure_interaction.py` |
| 271 | recipe_chamber_interaction | 레시피와 챔버의 교호작용을 추정합니다. | `examples/ex271_recipe_chamber_interaction.py` |
| 272 | hierarchical_experiment_model | 챔버별 변동을 부분 풀링하는 계층 실험모형을 작성합니다. | `examples/ex272_hierarchical_experiment_model.py` |
| 273 | posterior_predictive_experiment | 사후예측검사로 품질 분포 재현성을 확인합니다. | `examples/ex273_posterior_predictive_experiment.py` |
| 274 | optimal_condition_probability | 각 조건이 최고 품질일 확률을 계산합니다. | `examples/ex274_optimal_condition_probability.py` |
| 275 | multiobjective_utility | 균일도·불량률·식각률을 결합한 효용을 계산합니다. | `examples/ex275_multiobjective_utility.py` |
| 276 | expected_regret | 조건 선택의 기대 후회를 계산합니다. | `examples/ex276_expected_regret.py` |
| 277 | sequential_experiment_update | 1차·2차 데이터로 사후분포 갱신을 비교합니다. | `examples/ex277_sequential_experiment_update.py` |
| 278 | loo_interaction_comparison | 교호작용 포함·제외 모형을 LOO로 비교합니다. | `examples/ex278_loo_interaction_comparison.py` |
| 279 | experiment_diagnostics | R-hat·ESS·Divergence와 사후그래프를 저장합니다. | `examples/ex279_experiment_diagnostics.py` |
| 280 | automated_bayesian_experiment_report | 조건 비교·우월확률·효용·추천 Excel 보고서를 생성합니다. | `examples/ex280_automated_bayesian_experiment_report.py` |

## 실험 설계
- 레시피 3수준
- 챔버 3수준
- 압력 3수준
- RF 출력 3수준
- 조건별 반복 8회
- 품질 응답: 균일도, 식각률, 불량률
