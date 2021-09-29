
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
path = r'D:\Dropbox\Dropbox\A_CESEP Ana Ilie\DATA\2021\Data validation FID CH4sensors\Figaro'
data = pd.read_csv(path+'\linear regression for calibrations python.csv')

data.info()


data['CH4 ppm_a_D1'] = 1527.5 * data['a_D1'] - 277.32

data['CH4 ppm_b_D1'] = 1450.9 * data['b_D1'] - 261.96

data['CH4 ppm_c_D1'] = 1480.3 * data['c_D1'] - 248.38

data['CH4 ppm_d_D1'] = 1477 * data['d_D1'] - 252.78

data['CH4 ppm_e_D1'] = 1431.8 * data['e_D1'] - 244.64

data['CH4 ppm_f_D1'] = 1421.5 * data['f_D1'] - 238.51

data['CH4 ppm_g_D2'] = 1493.7 * data['g_D2'] - 231.41

data['CH4 ppm_h_D2'] = 1478.8 * data['h_D2'] - 230.43

data['CH4 ppm_i_D2'] = 1391.9 * data['i_D2'] - 235.98

data['CH4 ppm_j_D2'] = 1414.2 * data['j_D2'] - 229.32

data['CH4 ppm_k_D2'] = 1532.6 * data['k_D2'] - 341.54

data['CH4 ppm_l_D2'] = 1464.3 * data['l_D2'] - 290.31

data['CH4 ppm_m_D3'] = 1428.4 * data['m_D3'] - 234.73

data['CH4 ppm_n_D3'] = 1450.7 * data['n_D3'] - 236.68

data['CH4 ppm_o_D3'] = 1436.6 * data['o_D3'] - 241.78




data.to_csv('methane obtained from voltages figaro.csv', index=False)
















