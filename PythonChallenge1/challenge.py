import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

################### WEEK 1 #######################

dataset = "interview.csv"

data = pd.read_csv(dataset)

# Remove empty columns and empty row
data = data.drop(['Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Name(Cand ID)'], axis=1)
data = data.drop(data.index[1233])

names = ['Date', 'Client', 'Industry', 'Location', 'Position', 'Skillset', 'Interview', 'Gender', 'Curr_Location', 'Job_Location', 'Venue', 'Nat_Location', 'Permission', 'Scheduled', 'Call', 'Alt_number', 'Printout', 'Clear', 'Shared', 'Expected', 'Observed', 'Marital_Status']

data.columns = names

# Dropping data that seems irrelevant or too dirty
data = data.drop(['Date', 'Skillset', 'Nat_Location', 'Curr_Location'], axis=1)

# Clean data by merging similar points
data.Client.replace(['Aon Hewitt', 'Aon hewitt Gurgaon', 'Hewitt'], 'Hewitt', inplace=True)
data.Client.replace(['Standard Chartered Bank', 'Standard Chartered Bank Chennai'], 'SCB', inplace=True)
data.Industry.replace(['IT Services', 'IT Products and Services', 'IT'], 'IT', inplace=True)
data.Location.replace(['Chennai', 'chennai', 'CHENNAI', 'chennai '], 'Chennai', inplace=True)
data.Location.replace(['Gurgaon', 'Gurgaonr'], 'Gurgaon', inplace=True)
data.Location.replace(['- Cochin- '], 'Cochin', inplace=True)
data.Interview.replace(['Scheduled Walkin', 'Scheduled Walk In', 'Sceduled walkin'], 'Scheduled Walkin', inplace=True)
data.Interview.replace(['Scheduled '], 'Scheduled', inplace=True)
data.Interview.replace(['Walkin', 'Walkin '], 'Walkin', inplace=True)
data.Job_Location.replace(['- Cochin- '], 'Cochin', inplace=True)
data.Venue.replace(['- Cochin- '], 'Cochin', inplace=True)
data.Permission.replace(['Na', 'NA'], 'NA', inplace=True)
data.Permission.replace(['No', 'Not yet', 'Yet to confirm', 'NO'], 'No', inplace=True)
data.Permission.replace(['Yes', 'yes'], 'Yes', inplace=True)
data.Scheduled.replace(['Na', 'No', 'Not Sure', 'cant Say', 'Not sure'], 0, inplace=True)
data.Scheduled.replace(['Yes', 'yes'], 1, inplace=True)
data.Call.replace(['Na'], 'NA', inplace=True)
data.Call.replace(['No', 'No Dont'], 'No', inplace=True)
data.Call.replace(['Yes', 'yes'], 'Yes', inplace=True)
data.Alt_number.replace(['na', 'Na'], 'NA', inplace=True)
data.Alt_number.replace(['No', 'No I have only thi number'], 'No', inplace=True)
data.Alt_number.replace(['Yes', 'yes'], 'Yes', inplace=True)
data.Printout.replace(['na', 'Na'], 'NA', inplace=True)
data.Printout.replace(['Yes', 'yes'], 'Yes', inplace=True)
data.Printout.replace(['No- will take it soon', 'Not yet', 'Not Yet'], 'No', inplace=True)
data.Clear.replace(['na', 'Na'], 'NA', inplace=True)
data.Clear.replace(['No', 'No- I need to check', 'no'], 'No', inplace=True)
data.Clear.replace(['Yes', 'yes'], 'Yes', inplace=True)
data.Shared.replace(['na', 'Na'], 'NA', inplace=True)
data.Shared.replace(['No', 'Havent Checked', 'Need To Check', 'Not sure', 'Yet to Check', 'Not Sure', 'Not yet', 'no'], 'No', inplace=True)
data.Shared.replace(['Yes', 'yes'], 'Yes', inplace=True)
data.Expected.replace(['No', 'NO'], 'No', inplace=True)
data.Expected.replace(['Yes', 'yes', '11:00 AM', '10.30 Am'], 'Yes', inplace=True)
data.Observed.replace(['No', 'no', 'NO', 'No ', 'no '], 0, inplace=True)
data.Observed.replace(['Yes', 'yes', 'yes '], 1, inplace=True)
data.Marital_Status.replace(['Married'], 1, inplace=True)
data.Marital_Status.replace(['Single'], 0, inplace=True)

sns.countplot(x=data.Shared, hue=data.Expected)
plt.show()

# Fill the null values with the usual for expected
index_nan_print = data['Printout'][data['Printout'].isnull()].index
for i in index_nan_print:

    if data.at[data.index[i], 'Expected'] == 'Yes':
        data.loc[i, 'Printout'] = 'Yes'
    else:
        data.loc[i, 'Printout'] = 'No'

index_nan_print = data['Clear'][data['Clear'].isnull()].index
for i in index_nan_print:

    if data.loc[i, 'Expected'] == 'Yes':
        data.loc[i, 'Clear'] = 'Yes'
    else:
        data.loc[i, 'Clear'] = 'No'

index_nan_print = data['Permission'][data['Permission'].isnull()].index
for i in index_nan_print:

    if data.loc[i, 'Expected'] == 'No':
        data.loc[i, 'Permission'] = 'No'
    else:
        data.loc[i, 'Permission'] = 'Yes'


index_nan_print = data['Scheduled'][data['Scheduled'].isnull()].index
for i in index_nan_print:

    if data.at[data.index[i], 'Expected'] == 'No':
        data.loc[i, 'Scheduled'] = 0
    else:
        data.loc[i, 'Scheduled'] = 1

index_nan_print = data['Call'][data['Call'].isnull()].index
for i in index_nan_print:

    if data.at[data.index[i], 'Expected'] == 'Yes':
        data.loc[i, 'Call'] = 'Yes'
    else:
        data.loc[i, 'Call'] = 'No'

index_nan_print = data['Alt_number'][data['Alt_number'].isnull()].index
for i in index_nan_print:

    if data.at[data.index[i], 'Expected'] == 'Yes':
        data.loc[i, 'Alt_number'] = 'Yes'
    else:
        data.loc[i, 'Alt_number'] = 'No'

index_nan_print = data['Shared'][data['Shared'].isnull()].index
for i in index_nan_print:

    if data.at[data.index[i], 'Expected'] == 'Yes':
        data.loc[i, 'Shared'] = 'Yes'
    else:
        data.loc[i, 'Shared'] = 'No'

# Now there are no null spaces in the data

# Create One-Hot Encoding columns.
data = pd.get_dummies(data, columns=list(
    ['Shared', 'Position', 'Client', 'Industry', 'Location', 'Interview', 'Job_Location', 'Venue', 'Printout',
     'Expected', 'Gender', 'Alt_number', 'Call', 'Permission', 'Clear', 'Printout', ]))

# Data can now be worked with

# Separate features and response variable
Y = data['Observed'].values
X = data
X = X.drop(['Observed'], axis=1)
X = X.values
