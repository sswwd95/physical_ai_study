from common.feature_utils import load_data,FEATURES,output_path
c=load_data()[FEATURES].corr(); c.to_csv(output_path('ex225_feature_correlation.csv')); print(c.round(3))
