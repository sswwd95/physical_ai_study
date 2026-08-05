from common.load_data import load_vehicle_log
from common.paths import OUTPUT_DIR

df = load_vehicle_log()

df["speed_kph"] = df["speed_mps"] * 3.6
df["risk"] = (df["front_distance_m"] < 3.0) | (df["motor_temp_c"] > 32.2)
risk_rows = df.loc[df["risk"]].copy()

print("=== 자동차 센서 진단 리포트 ===")
print("전체 샘플:", len(df))
print("평균 속도(km/h):", round(df["speed_kph"].mean(), 2))
print("최소 전방 거리(m):", round(df["front_distance_m"].min(), 2))
print("최대 모터 온도(C):", round(df["motor_temp_c"].max(), 2))
print("위험 샘플:", len(risk_rows))

output_path = OUTPUT_DIR / "ex040_risk_rows.csv"
risk_rows.to_csv(output_path, index=False, encoding="utf-8-sig")
print("저장:", output_path)
