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

num_cat_cols = num_cols+cat_cols # Combined numerical and Categorical variables

#Create a new variable for each variable having missing value with VariableName_NA
# and flag missing value with 1 and other with 0

for var in num_cat_cols:
    if fullData[var].isnull().any()==True:
        #Let's normalize data and assign it to a new variable
        fullData[var+'_NA'] = fullData[var].isnull()*1

    # Impute numerical missing values with mean
    fullData[num_cols] = fullData[num_cols].fillna(fullData[num_cols].mean(), inplace=True)
    print fullData
    # Impute categorical missing values with -9999
    fullData[cat_cols] = fullData[cat_cols].fillna(value=-9999)

    # create label encoders for categorical features
    for var in cat_cols:
        number = LabelEncoder()
        # we will start labeling data
        fullData[var] = number.fit_transform(fullData[var].astype('str'))
        # tranforming centers the data i.e zero mean and unit standard error. x' = (x - standarderror)/ SD
        # fit_transform finds x' while fit finds SE and SD but requires transform()
    # Target variable is also a categorical so convert it
    fullData["Class12PercentGrade"] = number.fit_transform(fullData["Class12PercentGrade"].astype('int32'))

    train = fullData[fullData['Type'] == 'Train']
    test = fullData[fullData['Type'] == 'Test']

    train['is_train'] = np.random.uniform(0, 1, len(train)) <= .75
    Train, Validate = train[train['is_train'] == True, train[train['is_train'] == False]

    features = list(set(list(fullData.columns)) - set(ID_col) - set(target_col) - set(other_col))
    x_train = Train[list(features)].values
    y_train = Train["Class12PercentGrade"].values
    x_validate = Validate[list(features)].values
    y_validate = Validate["Class12PercentGrade"].values
    x_test = test[list(features)].values
    random.seed(100)
    rf = RandomForestClassifier(n_estimators=1000)
    rf.fit(x_train, y_train)

    status = rf.predict_proba(x_validate)
    fpr, tpr, _ = roc_curve(y_validate, status[:, 1])
    roc_auc = auc(fpr, tpr)
    print roc_auc
and
    final_status = rf.predict_proba(x_test)
    test["Class12PercentGrade"] = final_status[:, 1]
    test.to_csv('model_output.csv', columns=[ID_col, target_col])
# A predictive model can be boosted in two ways: Using feature engineering or boosting algorithms right away. Boosting
#algorithms is faster than the other. Gradient Boosting, XGBoost, AdaBoost, GentleBoost etc are just some types of boosting
# Algorithm. The answers can deviate abit as according.

#Two key words you should look into while using boosting algorithms.
#Bagging: It is an approach where you take random samples of data, build learning algorithms and take simple means
#to find bagging probabilities.
#Boosting: Boosting is similar, however the selection of sample is made more intelligently. We subsequently
#give more and more weight to hard to classify observations.

# In estimation of performance we will use a k-fold with k =7 as the best initial bet.