import numpy as np
from sklearn.utils.class_weight import compute_class_weight
from common.feature_utils import load_data
df=load_data(); c=np.array([0,1]); w=compute_class_weight('balanced',classes=c,y=df['anomaly_label']); print(dict(zip(c,w)))
