from common.path_tracking import load_path,nearest_path_index,signed_cross_track_error
path=load_path("path_sine.csv")
for x,y in [(2,.8),(2,-.8),(7,.2)]:
    idx=nearest_path_index(path,x,y)
    print(x,y,signed_cross_track_error(path,idx,x,y))
