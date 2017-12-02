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
target_col = ['Performance Type']
cat_cols = ['Gender','Program','Subject Code','Cohort','Student Type','Major','Section','High School',
            'Status2017Sept']
num_cols = ['Class12PercentGrade','English','Accounting','Dzongkha',
            'Commerce','Maths','Computer','Chemistry','Geography','Art','Physics',
            'Biology','Economics','Psychology','EVS','History','Semester1Grade','Semester2Grade',
            'Semester3Grade','Semester4Grade','Semester5Grade','Semester6Grade',
            'Semester7Grade','Semester8Grade','Cumulative Attendance','Sem Avg','Diff SemAvgClass12']

other_col=['Type'] #Test and Train Data set identifier

num_cat_cols = num_cols+cat_cols # Combined numerical and Categorical variables
for var in num_cat_cols:
    if fullData[var].isnull().any()==True:
        fullData[var+'_NA']=fullData[var].isnull()*1

#Impute numerical missing values with mean
fullData[num_cols] = fullData[num_cols].fillna(fullData[num_cols].mean(),inplace=True)
#Impute categorical missing values with -9999
fullData[cat_cols] = fullData[cat_cols].fillna(value = -9999)
#convert negatives
fullData['Diff SemAvgClass12'] = fullData['Diff SemAvgClass12'].abs()


#create label encoders for categorical features
for var in cat_cols+target_col:
 number = LabelEncoder()
 fullData[var] = number.fit_transform(fullData[var].astype('str'))

#Target variable is also a categorical so convert it
#fullData["Rising"] = number.fit_transform(fullData["Rising"].astype('str'))

train=fullData[fullData['Type']=='Train']
test=fullData[fullData['Type']=='Test']


features=cat_cols

x_train = train[list(features)].values
y_train = train["Performance Type"].values

x_test = test[list(features)].values
y_test = test["Performance Type"].values

random.seed(100)
rf = RandomForestClassifier(n_estimators=1000)
rf.fit(x_train, y_train)

status = rf.predict_proba(x_test)
fpr, tpr, _ = metrics.roc_curve(y_test, status[:,1])
roc_auc = metrics.auc(fpr, tpr)
print roc_auc

final_status = rf.predict_proba(x_test)
test["Performance Type (pred)"]=final_status[:,1]
test.to_csv('/mnt/RTC/PredictionData/model_output.csv',columns=['StudentID','Performance Type (pred)'])



