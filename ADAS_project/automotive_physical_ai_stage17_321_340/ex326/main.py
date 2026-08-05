from common.path_tracking import load_path,lookahead_index
path=load_path("path_sine.csv")
for start in [0,50,120,220]:
    print(start,"->",lookahead_index(path,start,.8))
