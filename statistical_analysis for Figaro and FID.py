######
@author: Ana MC Ilie

Citation: Ilie et. al, 2022. Influence of Soil Heterogeneity and Soil Moisture on the Migration of Methane Gas, an Intermediate-Scale Laboratory Investigation. Geosciences Journal, Springer.  

#######



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
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
path = r'C:\DATA\2021\Data validation FID CH4sensors\Figaro sensors'
data = pd.read_csv(path+'\Datalogger1.csv')

data.info()

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

x1 = data['A1']
x2 = data['A2']
x3 = data['A3']
x4 = data['A4']
x5 = data['A5']
ref_port = data['REF_FID']

# list to store results
results_df = [None] * 30

import scipy
def rsquared(x, y):
    """ Return R^2 where x and y are array-like."""
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
    return r_value**2

# r2
results_df[0] = rsquared(x1, ref_port)
results_df[1] = rsquared(x2, ref_port)
results_df[2] = rsquared(x3, ref_port)
results_df[3] = rsquared(x4, ref_port)
results_df[4] = rsquared(x5, ref_port)

print('\n Coefficient of Determination - R2 for A1: ', results_df[0])
print('\n Coefficient of Determination - R2 for A2: ', results_df[1])
print('\n Coefficient of Determination - R2 for A3: ', results_df[2])
print('\n Coefficient of Determination - R2 for A4: ', results_df[3])
print('\n Coefficient of Determination - R2 for A5: ', results_df[4])

# mean squared error - mse
results_df[5] = mean_squared_error(x1, ref_port)
results_df[6] = mean_squared_error(x2, ref_port)
results_df[7] = mean_squared_error(x3, ref_port)
results_df[8] = mean_squared_error(x4, ref_port)
results_df[9] = mean_squared_error(x5, ref_port)
print('\n Mean Squared Error - MSE for A1: ', results_df[5])
print('\n Mean Squared Error - MSE for A2: ', results_df[6])
print('\n Mean Squared Error - MSE for A3: ', results_df[7])
print('\n Mean Squared Error - MSE for A4: ', results_df[8])
print('\n Mean Squared Error - MSE for A5: ', results_df[9])

# root mean squared error - rmse
results_df[10] = sqrt(mean_squared_error(x1, ref_port))
results_df[11] = sqrt(mean_squared_error(x2, ref_port))
results_df[12] = sqrt(mean_squared_error(x3, ref_port))
results_df[13] = sqrt(mean_squared_error(x4, ref_port))
results_df[14] = sqrt(mean_squared_error(x5, ref_port))
print('\n Root Mean Squared Error - RMSE for A1: ', results_df[10])
print('\n Root Mean Squared Error - RMSE for A2: ', results_df[11])
print('\n Root Mean Squared Error - RMSE for A3: ', results_df[12])
print('\n Root Mean Squared Error - RMSE for A4: ', results_df[13])
print('\n Root Mean Squared Error - RMSE for A5: ', results_df[14])

# mean absolute error - mae
results_df[15] = mean_absolute_error(x1, ref_port)
results_df[16] = mean_absolute_error(x2, ref_port)
results_df[17] = mean_absolute_error(x3, ref_port)
results_df[18] = mean_absolute_error(x4, ref_port)
results_df[19] = mean_absolute_error(x5, ref_port)
print('\n Mean Absolute Error - MAE for A1: ', results_df[15])
print('\n Mean Absolute Error - MAE for A2: ', results_df[16])
print('\n Mean Absolute Error - MAE for A3: ', results_df[17])
print('\n Mean Absolute Error - MAE for A4: ', results_df[18])
print('\n Mean Absolute Error - MAE for A5: ', results_df[19])

# absolute mean bias error - mbe
results_df[20] = abs(np.mean(x1) - np.mean(ref_port))
results_df[21] = abs(np.mean(x2) - np.mean(ref_port))
results_df[22] = abs(np.mean(x3) - np.mean(ref_port))
results_df[23] = abs(np.mean(x4) - np.mean(ref_port))
results_df[24] = abs(np.mean(x5) - np.mean(ref_port))
print('\n Mean Bias Error - MBE for A1:', results_df[20])
print('\n Mean Bias Error - MBE for A2:', results_df[21])
print('\n Mean Bias Error - MBE for A3:', results_df[22])
print('\n Mean Bias Error - MBE for A4:', results_df[23])
print('\n Mean Bias Error - MBE for A5:', results_df[24])

def nrmse(actual, reference):
    """ Normalized Mean Squared Error """
    return np.sum(np.square(actual-reference))/np.sum(np.square(actual - actual.mean()))

results_df[25] = nrmse(x1,ref_port)
results_df[26] = nrmse(x2,ref_port)
results_df[27] = nrmse(x3,ref_port)
results_df[28] = nrmse(x4,ref_port)
results_df[29] = nrmse(x5,ref_port)
print('\n Normalized Mean Square Error - NMSE for A1:', results_df[25])
print('\n Normalized Mean Square Error - NMSE for A2:', results_df[26])
print('\n Normalized Mean Square Error - NMSE for A3:', results_df[27])
print('\n Normalized Mean Square Error - NMSE for A4:', results_df[28])
print('\n Normalized Mean Square Error - NMSE for A5:', results_df[29])

#df = pd.DataFrame(results_df, columns=['r2_A1', 'r2_A2', 'r2_A3', 'r2_A4', 'r2_A5'])
df = pd.DataFrame(results_df)
df = df.T
df.to_csv('results.csv', index=False)
























