########
@author: Ana MC Ilie

Citation: Ilie et. al, 2022. Influence of Soil Heterogeneity and Soil Moisture on the Migration of Methane Gas, an Intermediate-Scale Laboratory Investigation. Geosciences Journal, Springer.  
    
###########


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
path = r'D:\DATA\2021\Data validation FID CH4sensors\Figaro'
data = pd.read_csv(path+'\linear regression for calibrations python.csv')

data.info()

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

x1 = data['a_D1']
x2 = data['b_D1']
x3 = data['c_D1']
x4 = data['d_D1']
x5 = data['e_D1']
x6 = data['f_D1']
x7 = data['g_D2']
x8 = data['h_D2']
x9 = data['i_D2']
x10 = data['j_D2']
x11 = data['k_D2']
x12 = data['l_D2']
x13 = data['m_D3']
x14 = data['n_D3']
x15 = data['o_D3']
ref_port = data['CH4 ppm']

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
results_df[5] = rsquared(x6, ref_port)
results_df[6] = rsquared(x7, ref_port)
results_df[7] = rsquared(x8, ref_port)
results_df[8] = rsquared(x9, ref_port)
results_df[9] = rsquared(x10, ref_port)
results_df[10] = rsquared(x11, ref_port)
results_df[11] = rsquared(x12, ref_port)
results_df[12] = rsquared(x13, ref_port)
results_df[13] = rsquared(x14, ref_port)
results_df[14] = rsquared(x15, ref_port)





print('\n Coefficient of Determination - R2 for a_D1: ', results_df[0])
print('\n Coefficient of Determination - R2 for b_D1: ', results_df[1])
print('\n Coefficient of Determination - R2 for c_D1: ', results_df[2])
print('\n Coefficient of Determination - R2 for d_D1: ', results_df[3])
print('\n Coefficient of Determination - R2 for e_D1: ', results_df[4])
print('\n Coefficient of Determination - R2 for f_D1: ', results_df[5])
print('\n Coefficient of Determination - R2 for g_D2: ', results_df[6])
print('\n Coefficient of Determination - R2 for h_D2: ', results_df[7])
print('\n Coefficient of Determination - R2 for i_D2: ', results_df[8])
print('\n Coefficient of Determination - R2 for j_D2: ', results_df[9])
print('\n Coefficient of Determination - R2 for k_D2: ', results_df[10])
print('\n Coefficient of Determination - R2 for l_D2: ', results_df[11])
print('\n Coefficient of Determination - R2 for m_D3: ', results_df[12])
print('\n Coefficient of Determination - R2 for n_D3: ', results_df[13])
print('\n Coefficient of Determination - R2 for o_D3: ', results_df[14])





#df = pd.DataFrame(results_df, columns=['r2_a', 'r2_b', 'r2_c', 'r2_d', 'r2_e', 'r2_f', 'r2_g','r2_h','r2_i','r2_j','r2_k','r2_l','r2_m','r2_n','r2_o',])
df = pd.DataFrame(results_df)
df = df.T
df.to_csv('figaro sensors calibration results.csv', index=False)
















