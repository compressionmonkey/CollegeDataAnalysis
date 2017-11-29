# the essential components of predictive analysis are:
# 1. Descriptive analysis
# 2. Data Treatment(Missing value and outlier fixing)
# 3. Data Modelling
# 4. Estimation of performance

# In descriptive analysis you will need to know the missing values and big features
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

fullData  = pd.read_csv('Test.csv')
# In Data Treatment you will  and change missing values with mean/other easiest method. Mean works fine for first
# iteration.

# In Data modelling, we will use guide boosting methods. If we have an obervation cases more than 100,000 then we will
# use a random forest.

ID_col = ['StudentID']
target_col = ["Class12PercentGrade"]
cat_cols = ['StudentType','Gender','Program','HighSchool']
# We will remove the ID_col, target_col, cat_cols from fullData
num_cols= list(set(list(fullData.columns))-set(cat_cols)-set(ID_col)-set(target_col))
other_col=['Type'] #Test and Train Data set identifier
fullData[num_cols].mean(), inplace=True

num_cat_cols = num_cols+cat_cols # Combined numerical and Categorical variables

#Create a new variable for each variable having missing value with VariableName_NA
# and flag missing value with 1 and other with 0

for var in num_cat_cols:
    if fullData[var].isnull().any()==True:
        #Let's normalize data and assign it to a new variable
        fullData[var+'_NA'] = fullData[var].isnull()*1

# Impute numerical missing values with mean
fullData[num_cols] = fullData[num_cols].fillna(fullData[num_cols].mean(), inplace=True)
# Impute categorical missing values with -9999
fullData[cat_cols] = fullData[cat_cols].fillna(value=-9999)

# A predictive model can be boosted in two ways: Using feature engineering or boosting algorithms right away. Boosting
#algorithms is faster than the other. Gradient Boosting, XGBoost, AdaBoost, GentleBoost etc are just some types of boosting
# Algorithm. The answers can deviate abit as according.

#Two key words you should look into while using boosting algorithms.
#Bagging: It is an approach where you take random samples of data, build learning algorithms and take simple means
#to find bagging probabilities.
#Boosting: Boosting is similar, however the selection of sample is made more intelligently. We subsequently
#give more and more weight to hard to classify observations.

# In estimation of performance we will use a k-fold with k =7 as the best initial bet.