from common.path_tracking import load_path,nearest_path_index,signed_cross_track_error
path=load_path("path_sine.csv")
for x,y in [(1,.2),(3,2.4),(7,-2.0)]:
    idx=nearest_path_index(path,x,y)
    e=signed_cross_track_error(path,idx,x,y)
    mode="RECOVERY" if abs(e)>1.0 else "TRACKING"
    print(x,y,e,mode)
