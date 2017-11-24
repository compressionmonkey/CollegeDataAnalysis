import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

fullData = pd.read_csv('/mnt/RTC/PredictionData/data001.csv')
print fullData.shape
fullData = fullData.drop(fullData[fullData.Diff_SemAvgClass12 > 0.1].index)
print fullData.shape
ID_col = ['StudentID']
target_col = ['PerformanceType']
cat_cols = ['Gender','Program','Cohort','StudentType','Section','HighSchool']

#create label encoders for categorical features
for var in cat_cols+target_col:
   number = LabelEncoder()
   fullData[var] = number.fit_transform(fullData[var].astype('str'))

features=cat_cols

x_train = fullData[list(features)].values
y_train = fullData[target_col].values

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(x_train, y_train)
# summarize scores
np.set_printoptions(precision=3)
scores = fit.scores_
for feature, score in zip(features,scores) :
    print feature, score

