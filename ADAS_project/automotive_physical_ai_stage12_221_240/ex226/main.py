from common.feature_utils import load_data,output_path
df=load_data(); s=int(len(df)*.7); df.iloc[:s].to_csv(output_path('ex226_train.csv'),index=False); df.iloc[s:].to_csv(output_path('ex226_test.csv'),index=False); print(s,len(df)-s)
