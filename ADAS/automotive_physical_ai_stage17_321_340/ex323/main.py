from common.path_tracking import load_path, nearest_path_index
path=load_path("path_sine.csv")
for point in [(1.0,.8),(4.5,-.2),(9.0,1.5)]:
    idx=nearest_path_index(path,*point)
    print(point,"->",idx,path.iloc[idx].to_dict())
