import csv
FIELDS=['sim_time','detected','center_x','center_y','area_ratio','confidence','lost_frames','state','safety_active','fps','detect_latency_ms','pipeline_latency_ms','drone_x','drone_y','drone_z','vx','vy','vz','yaw_rate']
class CsvLogger:
    def __init__(self,p):self.f=p.open('w',newline='',encoding='utf-8-sig'); self.w=csv.DictWriter(self.f,fieldnames=FIELDS); self.w.writeheader()
    def write(self,r):self.w.writerow({k:r.get(k,'') for k in FIELDS})
    def close(self):self.f.close()
