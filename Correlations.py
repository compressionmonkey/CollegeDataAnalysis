import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

fullData = pd.read_csv('/mnt/RTC/PredictionData/StudentPerformanceData.csv')
i=0
for var in list(fullData.columns.values):
   number = LabelEncoder()
   fullData[var] = number.fit_transform(fullData[var].astype('str'))
   print i
   print var
   i = i+1

correlations = fullData.corr()

import matplotlib.pyplot as plt
plt.imshow(correlations,interpolation='nearest')
plt.colorbar()
plt.show()

