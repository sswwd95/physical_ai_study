from common.load_data import load_vehicle_log

df = load_vehicle_log()
condition = (df["motor_temp_c"] > 31.5) & (df["battery_v"] < 12.3)
result = df.loc[condition, ["time_s", "battery_v", "motor_temp_c", "status"]]
print(result.head(20))
print("조건 충족 행 수:", len(result))
