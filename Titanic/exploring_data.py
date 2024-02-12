import pandas as pd
import numpy as np
import os

# print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(__file__))
raw_data_path_file = os.path.join(os.path.dirname(__file__), "data", "raw")
train_path_file = os.path.join(raw_data_path_file, "train.csv")
test_path_file = os.path.join(raw_data_path_file, "test.csv")

train_df = pd.read_csv(train_path_file, index_col='PassengerId')
test_df = pd.read_csv(test_path_file, index_col='PassengerId')

train_df.info()

test_df['Survived'] = -888

df = pd.concat((train_df, test_df),axis=0)
df.head()
df.tail()
# Column selecion
df.Name
df['Name']
# Multiple column selecion
# df['Name','Age']
# Label indexing. Below selecting 5 to 10 rows and all columns
df.loc[5:10,]
df.loc[5:10,'Age' : 'Ticket']
# Selecting discrete column
df.loc[5:10,['Age','Ticket']]
# Position indexing (0 based index). Below selecting 6 to 10 rows and all columns
df.iloc[5:10,]

male_passengers = df.loc[df.Sex == 'male',]
print('Number of male passengers : {0}'.format(len(male_passengers)))

male_passengers_first_class = df.loc[((df.Sex == 'male') & (df.Pclass == 1)),]
print('Number of male passengers in first class : {0}'.format(len(male_passengers_first_class)))

# Summary Statistic
df.describe()

# Average. Con's : affected by extreme value
# Median
# Spread/Dispersion Measure : how spread out values are from central value. Variability
## Range : diff between maximum and min value. Con's : affected by extreme value
## Percentiles : x percentile is y means x% of values are below y (25th, 50th, 75th). Box-Whisker plot
## Inter-quartile range (IQR) : from 25th to 75th. Outliers : beyond 1.5 x IQR
## Variance : how far each value in list from mean value. Con's : affected by extreme value
## Standard deviation = square root of variance

print('Mean fare : {0}'.format(df.Fare.mean()))
print('Median fare : {0}'.format(df.Fare.median()))
print('Max fare : {0}'.format(df.Fare.max()))
print('Min fare : {0}'.format(df.Fare.min()))
print('Fare range : {0}'.format(df.Fare.max() - df.Fare.min()))
print('25 percentile : {0}'.format(df.Fare.quantile(.25)))
print('50 percentile : {0}'.format(df.Fare.quantile(.50)))
print('75 percentile : {0}'.format(df.Fare.quantile(.75)))
print('Variance fare : {0}'.format(df.Fare.var()))
print('Standard deviation fare : {0}'.format(df.Fare.std()))

# df.Fare.plot(kind='box')
df.describe(include='all')

print(df.Sex.value_counts())
df.Sex.value_counts(normalize=True)

print(df[df.Survived != -888].Survived.value_counts())


df.Age.plot.hist(bins=10)