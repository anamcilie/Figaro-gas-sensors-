# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
from pandas import Series        # To work on series
import statsmodels
import warnings                   # To ignore the warnings
warnings.filterwarnings("ignore")
import seaborn as sns
sns.set_style("white")
plt.style.use("seaborn")
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(14, 8)})

# sns.set() # setting to default settings
# plt.rcParams # set default matplotlib settings


# finding the current directory
abs_path = os.getcwd()
abs_path

# change to desired folder where .csv file is present - Use forward backslash
path = r'C:\Users\ailie_a\Dropbox\A_CESEP Ana Ilie\DATA\2021\2D tank\2nd\Experiments'
data = pd.read_csv(path + '/Avg min 1st het setup1st 2nd gas injections comparison.csv')


# Exploratory Data Analysis
data.dtypes # find the datatypes of all variables
data.columns # list of all column names - original list
data.shape # Dimensions of original dataset (rows, columns)
print(data.head(10)) # first 10 rows of dataset
data.index # index - number of rows and columns
data.info() # information on datatypes and number of elements

# Convert the datatype of certain columns to float type 
#data[['Time D1 S1', 'Time D1 S2', 'Time D1 S3', 'Time D1_S5 1st','Time D1_S6 1st']] = data[['Time D1_S1', 'Time D1_S2', 'Time D1_S3 1st', 'Time D1_S5 1st','Time D1_S6 1st']].apply(pd.to_numeric)

# Missing Value Analysis
# list number of missing values for each column
print (data.isnull().sum())
null_counts = data.isnull().sum()

# Run following 6 lines together for plot
plt.figure(figsize=(14,8))
plt.xticks(np.arange(len(null_counts)), null_counts.index, rotation='vertical')
plt.xlabel('Columns')
plt.ylabel('Number of Attributes with Missing Data')
plt.bar(np.arange(len(null_counts)), null_counts)
plt.title('Missing Value Analysis')

# replacing all the zeros with NaN
#data = data[data.columns].replace(0, np.nan)
# dropping all the rows with NaN in the columns 
#data.dropna(inplace=True)
# recheck the shape of dataframe if values changed
#data.shape

# Continous Variables in the dataset
print(data)
data_cont = data.iloc[:,:].reset_index() 
data_cont = data_cont.drop(['index'], axis = 1)
data_cont.shape
data_cont.columns


# Function to remove outliers using IQR (Inter Quartile Range)
def remove_outlier(df_in, col_name):
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 # Interquartile range
    # assume the factor of 2.0 for the ranges
    low_lim  = q1 - 2*iqr
    high_lim = q3 + 2*iqr
    df_out = df_in.loc[(df_in[col_name] > low_lim) & (df_in[col_name] < high_lim)]
    return df_out

# Executing the function to remove outliers
data_cont = remove_outlier(data_cont, 'S1 1st')
data_cont = remove_outlier(data_cont, 'S2 1st')
data_cont = remove_outlier(data_cont, 'S3 1st')
data_cont = remove_outlier(data_cont, 'S5 1st')
data_cont = remove_outlier(data_cont, 'S6 1st')
data_cont = remove_outlier(data_cont, 'S7 1st')
data_cont = remove_outlier(data_cont, 'S8 1st')
data_cont = remove_outlier(data_cont, 'S1 2nd')
data_cont = remove_outlier(data_cont, 'S2 2nd')
data_cont = remove_outlier(data_cont, 'S3 2nd')
data_cont = remove_outlier(data_cont, 'S5 2nd')
data_cont = remove_outlier(data_cont, 'S6 2nd')
data_cont = remove_outlier(data_cont, 'S7 2nd')
data_cont = remove_outlier(data_cont, 'S8 2nd')


# save the cleaned data file to another .csv, in the same folder
data.to_csv(path + "\Cleaned_Data_File.csv")



# store descriptive statistics in a different dataframe and .csv file
desc_stat = data.describe()
desc_stat.to_csv(path+'\Descriptive_Stats.csv')



# Boxplot Analysis to see presence of outliers
sns.boxplot(y=data_cont["S1 1st"], data=data)
sns.boxplot(y=data_cont["S1 2nd"], data=data)
sns.boxplot(y=data_cont["S2 1st"], data=data)
sns.boxplot(y=data_cont["S2 2nd"], data=data)
sns.boxplot(y=data_cont["S3 1st"], data=data)
sns.boxplot(y=data_cont["S3 2nd"], data=data)
sns.boxplot(y=data_cont["S5 1st"], data=data)
sns.boxplot(y=data_cont["S5 2nd"], data=data)
sns.boxplot(y=data_cont["S6 1st"], data=data)
sns.boxplot(y=data_cont["S6 2nd"], data=data)
sns.boxplot(y=data_cont["S7 1st"], data=data)
sns.boxplot(y=data_cont["S7 2nd"], data=data)
sns.boxplot(y=data_cont["S8 1st"], data=data)
sns.boxplot(y=data_cont["S8 2nd"], data=data)

# Basic Plots
data_cont.boxplot()



# Variable Correlation - Heatmap
corr = data_cont.corr() # Calculating the correlations between variables

# Correlation
df_num_corr = data_cont.corr()['S1 1st'] 
features_list = df_num_corr[abs(df_num_corr) > 0.1].sort_values(ascending=False)
print("These are {} correlation values of variables with S1 1st:\n{}".format(len(features_list), features_list))

# plot the heatmap for correlations
plt.figure(figsize=(20,10))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns,
            annot = True, annot_kws={"size": 11})


# Pair Plot
sns.pairplot(data_cont)



# Line Plot - continous variables
CH4_conc = ['S1 1st','S2 1st','S3 1st','S5 1st','S6 1st','S7 1st','S8 1st']
plt.plot(data_cont[CH4_conc])
plt.xlabel('Time D1 S1')
plt.ylabel('CH4 ppm')
plt.show()

# Line Plot - continous variables
CH4_conc = ['S1 2nd','S2 2nd','S3 2nd','S5 2nd','S6 2nd','S7 2nd','S8 2nd']
plt.plot(data_cont[CH4_conc])
plt.xlabel('Time D1 S1 2nd')
plt.ylabel('CH4 ppm')
plt.show()

# Histogram
data_cont.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)



# Distribution Plot
plt.figure(figsize=(20,10))
sns.distplot(data_cont['S1 1st'], label='S1 1st')
sns.distplot(data_cont['S2 1st'], label='S2 1st')
sns.distplot(data_cont['S3 1st'], label='S3 1st')
plt.xlabel('Variable Estimate')
plt.title('Distribution Plot - Kernel Density Estimate')
plt.legend()


# Time Series Analysis
data2 = data.set_index('S1 1st')
data2.head(3)

#data2['Month'] = data2.index.month
#data2['Year'] = data2.index.year
#data2['Weekday Name'] = data2.index.weekday_name
#data2.sample(5, random_state = 0)


# time slicing
data_September = data2.loc['2021-09-30':'2021-09-30'] # September Data
data_September2 = data2.loc['2021-09']  # September Data

data_September['Avg S1 1st'].plot(linewidth = 0.5)

cols_plot = ['Avg S1 1st', 'Avg S1 1st', 'Avg S1 1st']
axes = data_September[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:
    ax.set_ylabel('CH4 ppm')
    
    

# slicing and plotting at the same time
data2.loc['2021-09-30 14:28:00':'2021-09-30 16:30:00', 'Avg S1 1st'].plot()



# number of observations per timestamp
data2.groupby(level=0).count()



# mean values on a daily basis
data2.resample('D').mean()
