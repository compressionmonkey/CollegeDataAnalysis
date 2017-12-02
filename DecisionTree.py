import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split

fullData = pd.read_csv('/mnt/RTC/PredictionData/data003.csv')

#ID_col = ['StudentID']
#target_col = ['Performance Type']
#cat_cols = ['Gender','Program','Cohort','Student Type','Section','High School']



print fullData.isnull().any()

ID_col = ['StudentID']
target_col = ['High School']
cat_cols = []
num_cols = ['Class12PercentGrade','Sem Avg']

other_col=['Type'] #Test and Train Data set identifier

analysisData = fullData[num_cols+cat_cols+target_col]

#Impute numerical missing values with mean
analysisData[num_cols] = analysisData[num_cols].fillna(analysisData[num_cols].mean(),inplace=True)
#Impute categorical missing values with -9999
analysisData[cat_cols] = analysisData[cat_cols].fillna(value = -9999)


#create label encoders for categorical features
for var in cat_cols:
    number = LabelEncoder()
    analysisData[var] = number.fit_transform(analysisData[var].astype('str'))

#Target variable is also a categorical so convert it
#fullData["Rising"] = number.fit_transform(fullData["Rising"].astype('str'))


features=num_cols+cat_cols

X = analysisData[features]
Y = analysisData[target_col]
targets = pd.Series(analysisData['High School'].get_values())
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

import graphviz
dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=features,
                         class_names=targets,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("/mnt/RTC/outfile")

print "done"
