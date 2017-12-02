import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

fullData = pd.read_csv('/mnt/RTC/PredictionData/data002.csv')
print fullData.shape
#fullData = fullData.drop(fullData[fullData.Diff_SemAvgClass12 > 0.1].index)
#print fullData.shape
ID_col = ['StudentID']
target_col = ['Performance Type']
cat_cols = ['Gender','Program','Subject Code','Cohort','Student Type','Major','Section','High School',
            'Status2017Sept']
num_cols = ['Class12PercentGrade','English','Accounting','Dzongkha',
            'Commerce','Maths','Computer','Chemistry','Geography','Art','Physics',
            'Biology','Economics','Psychology','EVS','History','Semester1Grade','Semester2Grade',
            'Semester3Grade','Semester4Grade','Semester5Grade','Semester6Grade',
            'Semester7Grade','Semester8Grade','Cumulative Attendance','Sem Avg','Diff SemAvgClass12']

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


features=num_cat_cols

x_train = fullData[list(features)].values
y_train = fullData[target_col].values

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
test = SelectKBest(score_func=chi2)
fit = test.fit(x_train, y_train)
# summarize scores
np.set_printoptions(precision=3)
scores = fit.scores_
for feature, score in zip(features,scores) :
    print feature, score



import matplotlib.pyplot as plt

plt.rcdefaults()
objects = features
y_pos = np.arange(len(objects))
performance = scores

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xticks(rotation=90)
plt.ylabel('Score')
plt.title('KBest Feature')

plt.show()
