from common.path_tracking import load_path, path_heading
path=load_path("path_sine.csv")
for idx in [0,40,100,180,240]:
    print(idx,path_heading(path,idx))
