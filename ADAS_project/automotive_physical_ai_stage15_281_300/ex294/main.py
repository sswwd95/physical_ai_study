from common.reliability_utils import load_rul,output_path
df=load_rul()
s=df[["age_h","health_score","vibration_g","temperature_c","internal_resistance_ohm","observed_rul_h"]].corr()
p=output_path("ex294_rul_feature_correlation.csv"); s.to_csv(p,encoding="utf-8-sig")
print(s.round(3))
