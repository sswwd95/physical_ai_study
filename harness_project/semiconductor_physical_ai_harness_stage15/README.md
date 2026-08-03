# 반도체 Physical AI 하네스 엔지니어링 — 15단계

실습 071~075는 공정 능력지수와 규격 이탈 분석을 다룹니다.

## 포함 내용
- Cp, Cpu, Cpl, Cpk
- Pp, Ppu, Ppl, Ppk
- LSL·USL 규격 이탈 행
- 관측 이탈률과 PPM
- Lot별 공정 능력 비교
- HTML 공정 능력 대시보드
- 합성 온도 품질 데이터와 규격 JSON
- Antigravity 하네스 프롬프트
- 라인별 해설과 pytest 자동 테스트

## 실행

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_071_cp_cpk.py
python examples\example_072_pp_ppk.py
python examples\example_073_spec_violation_rate.py
python examples\example_074_lot_capability_comparison.py
python examples\example_075_capability_dashboard.py

pytest -q
```

모든 규격과 능력 기준은 교육용입니다. 실제 공정 적용 전 측정시스템 분석과 공정 안정성 검증이 필요합니다.
