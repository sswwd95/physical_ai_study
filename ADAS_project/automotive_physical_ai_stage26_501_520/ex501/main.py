from common.tb3_burger_utils import find_repo_root,tb3_dir,scene_path,model_path
print("repository:",find_repo_root())
print("tb3 directory:",tb3_dir())
print("scene:",scene_path())
print("model:",model_path())
print("scene exists:",scene_path().exists())
print("model exists:",model_path().exists())
