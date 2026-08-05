from common.feature_utils import load_data
df=load_data(); print(df.head()); print(df['anomaly_label'].value_counts()); print(df['anomaly_label'].mean())
