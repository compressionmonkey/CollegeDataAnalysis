import numpy as np
import pandas as pd
#from IPython import get_ipython
#import seaborn as sns
import matplotlib.pyplot as plt

data_train = pd.read_csv('/home/keldendraduldorji/Desktop/KDD/train.csv')
data_test = pd.read_csv('/home/keldendraduldorji/Desktop/KDD/test.csv')
#Picks up 3 random samples
data_train.sample(3)
#Create a barplot that has assigned x, y values and also legend title name "Sex"
#sns.barplot(x="Embarked", y="Survived", hue="Sex", data=data_train)
#plt.show() # Visualizing the data
#sns.pointplot(x="Pclass", y="Survived", hue="Sex", data=data_train,
              #palette={"male": "blue", "female": "pink"},
              #markers=["*", "o"], linestyles=["-", "--"])

#sns pointplot function creates a pointplot that estimates central tendency for
#a numeric variable. Your x and y values are assigned along with a legend title.
#Regarding data , palette assigns a color to a variable. Markers are the symbols of the
#legends in this case male and female. linestyles are used to specify whether a line in the graph looks like
# ----- or straight line.
#plt.show()


def simplify_ages(df):
    df.Age = df.Age.fillna(-0.5)
    # so you are just filling null values with -0.5
    bins = (-1, 0, 5, 12, 18, 25, 35, 60, 120)
    group_names = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
    categories = pd.cut(df.Age, bins, labels=group_names)
    # cut the age column dataset into bins of the given brackets and label them the group_names
    #name
    df.Age = categories
    return df
# we are simplifying and cleaning up the age column

def simplify_cabins(df):
    df.Cabin = df.Cabin.fillna('N')
    #Ok if the cabin column does not have any values add N to blank spaces
    df.Cabin = df.Cabin.apply(lambda x: x[0]) # We are going to apply the lamda function to the cabin column
    # Lamda is an alternative to defining a python function but we use it only once.
    #The apply function simply just uses a lamda or function defined
    return df
# we are simplifying and cleaning up the cabin column

def simplify_fares(df):
    df.Fare = df.Fare.fillna(-0.5)
    bins = (-1, 0, 8, 15, 31, 1000)
    group_names = ['Unknown', '1_quartile', '2_quartile', '3_quartile', '4_quartile']
    categories = pd.cut(df.Fare, bins, labels=group_names)
    df.Fare = categories
    return df
#we are simplifying and cleaning up the fares column

def format_name(df):
    df['Lname'] = df.Name.apply(lambda x: x.split(' ')[0]) # we have split the names into two: Last name as index 0
    df['NamePrefix'] = df.Name.apply(lambda x: x.split(' ')[1])  # and first name as index 1
    return df
# we want to have two names as their own features

def drop_features(df):
    return df.drop(['Ticket', 'Name', 'Embarked'], axis=1)
    # here we are removing the columns
def transform_features(df):
    df = simplify_ages(df)
    df = simplify_cabins(df)
    df = simplify_fares(df)
    df = format_name(df)
    df = drop_features(df)
    return df
# We are apply all the functions that we have created
data_train = transform_features(data_train)
#we now use it on our data set
data_test = transform_features(data_test)
data_train.head()
# we are taking out some of upper datasets
sns.barplot(x="Age", y="Survived", hue="Sex", data=data_train);
plt.show()
sns.barplot(x='Fare',y='Survived', hue='Sex', data=data_train)
plt.show()

from sklearn import preprocessing


def encode_features(df_train, df_test):
    features = ['Fare', 'Cabin', 'Age', 'Sex', 'Lname', 'NamePrefix']
    df_combined = pd.concat([df_train[features], df_test[features]]) # Concatenate the two csv files' features

    for feature in features:
        le = preprocessing.LabelEncoder()
        # we are normalising the data
        le = le.fit(df_combined[feature])
        df_train[feature] = le.transform(df_train[feature])
        df_test[feature] = le.transform(df_test[feature])
        # transform your features into individual indexes
    return df_train, df_test


data_train, data_test = encode_features(data_train, data_test)
data_train.head()
# The machine learning begins
from sklearn.model_selection import train_test_split

X_all = data_train.drop(['Survived', 'PassengerId'], axis=1)
#Remove columns that you don't need so that you can predict it!
y_all = data_train['Survived']

num_test = 0.20
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=num_test, random_state=23)
# Ok so the data sets are being split into a random rows of 23 which are ??
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import GridSearchCV

# Choose the type of classifier.
clf = RandomForestClassifier()

# Choose some parameter combinations to try
parameters = {'n_estimators': [4, 6, 9],
              'max_features': ['log2', 'sqrt','auto'],
              'criterion': ['entropy', 'gini'],
              'max_depth': [2, 3, 5, 10],
              'min_samples_split': [2, 3, 5],
              'min_samples_leaf': [1,5,8]
             }

# Type of scoring used to compare parameter combinations
acc_scorer = make_scorer(accuracy_score) #accuracy_score checks the accuracy rate of the

# Run the grid search
grid_obj = GridSearchCV(clf, parameters, scoring=acc_scorer)
grid_obj = grid_obj.fit(X_train, y_train)

# Set the clf to the best combination of parameters
clf = grid_obj.best_estimator_

# Fit the best algorithm to the data.
clf.fit(X_train, y_train)

from sklearn.cross_validation import KFold
 # this library is to pick segments of data to test and pick the one that performed the best!
def run_kfold(clf):
    kf = KFold(891, n_folds=10)
    outcomes = []
    fold = 0
    for train_index, test_index in kf:
        fold += 1
        X_train, X_test = X_all.values[train_index], X_all.values[test_index]
        y_train, y_test = y_all.values[train_index], y_all.values[test_index]
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        outcomes.append(accuracy)
        print("Fold {0} accuracy: {1}".format(fold, accuracy))
    mean_outcome = np.mean(outcomes)
    print("Mean Accuracy: {0}".format(mean_outcome))

run_kfold(clf)

ids = data_test['PassengerId']
predictions = clf.predict(data_test.drop('PassengerId', axis=1))


output = pd.DataFrame({ 'PassengerId' : ids, 'Survived': predictions })
# output.to_csv('titanic-predictions.csv', index = False)
output.head()

#troy's comment
#troy's  2nd comment
