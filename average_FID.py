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
path = r'C:\Users\DATA\2021\2D tank\2nd\Experiments\FID'
df = pd.read_csv(path+'\2nd gas inj 1st het setup dry sand python.csv')
#  df = df.drop(['Time 1', 'Unnamed: 2'], axis = 1)

df['Time'] = pd.to_timedelta(df['Time'], unit='s')

s1 = df.set_index('Time').resample('S')["CH4 ppm"].mean()
# s2 = df.set_index('Time').resample('S')["CH4 ppm FID.1"].mean()

df = pd.concat([s1], axis=1)

df.to_csv('Averaged 2nd_FID.csv', index=True)







