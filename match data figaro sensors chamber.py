# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:50:31 2022

@author: anamc
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
import warnings                   # To ignore the warnings
warnings.filterwarnings("ignore")
import seaborn as sns
sns.set_style("white")
plt.style.use("seaborn")
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(14, 8)})
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.titleweight'] = 'bold'
# sns.set() # setting to default settings
# plt.rcParams # set default matplotlib settings

# finding the current directory
abs_path = os.getcwd()
abs_path

# change to desired folder where .csv file is present - Use forward backslash
path = r'D:\Dropbox\Dropbox\A_CESEP Ana Ilie\DATA\2022\3D tank\DATA\CH4 sensors\Flux chamber'

######        figaro sensor datalogger chamber      ##############
data_chamber = pd.read_csv(path + '\Datalogger_chamber_every_min.csv')

######        figaro sensors datalogger 3         ##############
data_D3 = pd.read_csv(path + '\Datalogger_D3_every_min.csv')


data_chamber.info()
data_D3.info()

# rename columns
data_chamber = data_chamber.rename(columns={'Datetime': 'DateTime'})
data_D3 = data_D3.rename(columns={'Datetime':'DateTime'})

# Timestamp needs to be converted to datetime object (for time series manipulations)
data_chamber['DateTime'] = pd.to_datetime(data_chamber['DateTime'])
data_D3['DateTime'] = pd.to_datetime(data_D3['DateTime'])

data_merged = pd.merge(data_D3, data_chamber, how='inner', on='DateTime')
data_merged.info()


# Linear Regression 
from sklearn.linear_model import LinearRegression
X = data_merged['Vb'].values
Y = data_merged['V chamber'].values
X = X.reshape(-1,1)
Y = Y.reshape(-1,1)

lin_regressor = LinearRegression()  # create object for the class
lin_regressor.fit(X, Y)  # perform linear regression
Y_pred = lin_regressor.predict(X)  # make predictions
r_sq = lin_regressor.score(X,Y) # R-square
coeff = lin_regressor.coef_
intercept = lin_regressor.intercept_

plt.scatter(X, Y, color = 'blue')
plt.plot(X, Y_pred, color='red')
plt.xlim(0)
plt.ylim(0)
plt.xlabel('Vb D3')
plt.ylabel('V chamber')
plt.title('Linear Regression - chamber vs figaro sensor')
plt.text(X.min(),Y.max(), 'Equation: y = %0.2f x + (%0.2f)'% (coeff, intercept), bbox=dict(facecolor='white', alpha=0.8))
plt.text(X.min(),Y.max()-2,'R-squared = %0.2f' % r_sq, bbox=dict(facecolor='white', alpha=0.8))
plt.show()
plt.savefig(path+'\Plot V_chamber&Vb_D3 - Linear Regression.png', dpi=300, bbox_inches='tight')

data_merged.to_csv(path + "\Output V_chamber&Vb_D3_Merged_Clean_File.csv")
path

























