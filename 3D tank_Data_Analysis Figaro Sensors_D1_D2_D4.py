
"""
Spyder Editor

"""
# @author: Ana MC Ilie
# Citation: Ilie et. al, 2022. Influence of Soil Heterogeneity and Soil Moisture on the Migration of Methane Gas, an Intermediate-Scale Laboratory Investigation. Geosciences Journal, Springer.  
"""
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
path = r'C:\Users\ailie_a\Dropbox\A_CESEP Ana Ilie\DATA\2022\3D tank\DATA\CH4 sensors'
data = pd.read_csv(path + '/Datalogger_D1_D2_D4_feb 7th-11th PipeA.csv')

# Exploratory Data Analysis
data.dtypes # find the datatypes of all variables
data.columns # list of all column names - original list
data.shape # Dimensions of original dataset (rows, columns)
print(data.head(10)) # first 10 rows of dataset
data.index # index - number of rows and columns
data.info() # information on datatypes and number of elements

# Convert the datatype of certain columns to float type 
data[['Datetime_D1', 'Datetime_D2', 'Datetime_D4']] = data[['Datetime_D1', 'Datetime_D2', 'Datetime_D4']].apply(pd.to_datetime)

data_d1 = data.iloc[:, 0:6]
data_d1['Datetime_D1'] = data_d1['Datetime_D1'].apply(pd.to_datetime)
data_d1 = data_d1.set_index(['Datetime_D1'])
data_d1.info()

# replace negative with 0
data_d1[data_d1['B2'] < 0] = 0
data_d1[data_d1['B6'] < 0] = 0
data_d1[data_d1['A1'] < 0] = 0
data_d1[data_d1['A3'] < 0] = 0
data_d1[data_d1['A4'] < 0] = 0

# avg every 1 min
data_d1_every_min = data_d1.resample('1min').mean()
data_d1_every_min.to_csv(path+'\Datalogger_d1_every_min.csv')

# avg every 30 mins
data_d1_every_30min = data_d1.resample('30min').mean()
data_d1_every_30min.to_csv(path+'\Datalogger_d1_every_30min.csv')





# ---------------------------------------

data_d2 = data.iloc[:, 6:10]
data_d2['Datetime_D2'] = data_d2['Datetime_D2'].apply(pd.to_datetime)
data_d2 = data_d2.set_index(['Datetime_D2'])
data_d2.info()

# replace negative with 0
data_d2[data_d2['A5'] < 0] = 0
data_d2[data_d2['A6'] < 0] = 0
data_d2[data_d2['D2'] < 0] = 0


# avg every 1 min
data_d2_every_min = data_d2.resample('1min').mean()
data_d2_every_min.to_csv(path+'\Datalogger_d2_every_min.csv')

# avg every 30 mins
data_d2_every_30min = data_d2.resample('30min').mean()
data_d2_every_30min.to_csv(path+'\Datalogger_d2_every_30min.csv')






# -----------------------------------------

data_d4 = data.iloc[:, 10:13]
data_d4['Datetime_D4'] = data_d4['Datetime_D4'].apply(pd.to_datetime)
data_d4 = data_d4.set_index(['Datetime_D4'])
data_d4.info()

# replace negative with 0
data[data['D9'] < 0] = 0
data[data['E5'] < 0] = 0
data[data['E3'] < 0] = 0


# avg every 1 min
data_d4_every_min = data_d4.resample('1min').mean()
data_d4_every_min.to_csv(path+'\Datalogger_d4_every_min.csv')

# avg every 30 mins
data_d4_every_30min = data_d4.resample('30min').mean()
data_d4_every_30min.to_csv(path+'\Datalogger_d4_every_30min.csv')


#------------------------------------



# save the cleaned data file to another .csv, in the same folder
data.to_csv(path + "\Cleaned_Data_File.csv")


# store descriptive statistics in a different dataframe and .csv file
desc_stat = data.describe()
desc_stat.to_csv(path+'\Descriptive_Stats.csv')
print(desc_stat)


# mean values on a daily basis
data.resample('D').mean()
