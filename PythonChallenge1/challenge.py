import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

dataset = "interview.csv"

data = pd.read_csv(dataset)

#Remove empty columns
data = data.drop(['Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Name(Cand ID)'], axis=1)
data = data.drop(data.index[1233])
#Taking a look at the data
print(data.shape)

names = ['Date', 'Client', 'Industry', 'Location', 'Position', 'Skillset', 'Interview', 'Gender', 'Curr_Location', 'Job_Location', 'Venue', 'Nat_Location', 'Permission', 'Scheduled', 'Call', 'Alt_number', 'Printout', 'Clear', 'Shared', 'Expected', 'Observed', 'Marital_Status']

data.columns= names
print(data.info())


#Dropping data that seems irrelevant or too dirty
data = data.drop(['Date', 'Skillset', 'Nat_Location'], axis=1)

#Clean data by merging similar points
data.Client.replace(['Aon Hewitt', 'Aon hewitt Gurgaon', 'Hewitt'], 'Hewitt', inplace=True)
data.Client.replace(['Standard Chartered Bank', 'Standard Chartered Bank Chennai'], 'SCB', inplace=True)
data.Industry.replace(['IT Services', 'IT Products and Services', 'IT'], 'IT', inplace=True)
data.Location.replace(['Chennai', 'chennai', 'CHENNAI', 'chennai '], 'Chennai', inplace=True)
data.Location.replace(['Gurgaon', 'Gurgaonr'], 'Gurgaon', inplace=True)
data.Location.replace(['- Cochin- '], 'Cochin', inplace=True)
data.Interview.replace(['Scheduled Walkin', 'Scheduled ', 'Scheduled Walk In', 'Sceduled walkin'], 'Scheduled', inplace=True)
data.Interview.replace(['Walkin', 'Walkin '], 'Walkin', inplace=True)
data.Curr_Location.replace(['Chennai', 'chennai', 'CHENNAI', 'chennai '], 'Chennai', inplace=True)
data.Curr_Location.replace(['- Cochin- '], 'Cochin', inplace=True)
data.Job_Location.replace(['- Cochin- '], 'Cochin', inplace=True)
data.Venue.replace(['- Cochin- '], 'Cochin', inplace=True)
data.Permission.replace(['No', 'Not yet', 'Yet to confirm', 'NO', 'Na'], 0, inplace=True)
data.Permission.replace(['Yes', 'yes'], 1, inplace=True)
data.Scheduled.replace(['Na', 'No', 'Not Sure', 'cant Say', 'Not sure'], 0, inplace=True)
data.Scheduled.replace(['Yes', 'yes'], 1, inplace=True)
data.Call.replace(['No', 'No Dont', 'Na'], 0, inplace=True)
data.Call.replace(['Yes', 'yes'], 1, inplace=True)
data.Alt_number.replace(['No', 'No I have only thi number', 'na', 'Na'], 0, inplace=True)
data.Alt_number.replace(['Yes', 'yes'], 1, inplace=True)
data.Printout.replace(['No', 'na', 'Na'], 'No', inplace=True)
data.Printout.replace(['Yes', 'yes'], 'Yes', inplace=True)
data.Printout.replace(['No- will take it soon', 'Not yet', 'Not Yet'], 'Not yet', inplace=True)
data.Clear.replace(['No', 'No- I need to check', 'na', 'Na', 'no'], 0, inplace=True)
data.Clear.replace(['Yes', 'yes'], 1, inplace=True)
data.Shared.replace(['No', 'Havent Checked', 'Need To Check', 'Not sure', 'Yet to Check', 'Not Sure', 'Not yet', 'no', 'na', 'Na'], 0, inplace=True)
data.Shared.replace(['Yes', 'yes'], 1, inplace=True)
data.Expected.replace(['No', 'NO'], 'No', inplace=True)
data.Expected.replace(['Yes', 'yes', '11:00 AM', '10.30 Am'], 'Yes', inplace=True)
data.Observed.replace(['No', 'no', 'NO', 'No ', 'no '], 0, inplace=True)
data.Observed.replace(['Yes', 'yes', 'yes '], 1, inplace=True)

# Check information in the data
# for column in data.columns:
#    print(column, data[column].unique())
#    print('#'*50)

sns.countplot(x=data.Clear, hue=data.Expected)

index_nan_print = data['Printout'][data['Printout'].isnull()].index
for i in index_nan_print:

    if data.at[data.index[i], 'Expected'] == 'No':
        data.loc[i, 'Printout'] = 0
    else:
        data.loc[i, 'Printout'] = 1

index_nan_print = data['Clear'][data['Clear'].isnull()].index
for i in index_nan_print:

    if data.loc[i,'Expected'] == '0':
        data.loc[i,'Clear'] = '0'
    else:
        data.loc[i],'Clear'] = '1'

# index_nan_print = data['Permission'][data['Permission'].isnull()].index
# for i in index_nan_print:
#
#     if data.iloc[[i],['Expected']] == '0':
#         data.iloc[[i],['Permission']] = '0'
#     else:
#         data.iloc[[i],['Permission']] = '1'
#
print(data.info())
