
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
path = r'C:\Users\ailie_a\Dropbox\A_CESEP Ana Ilie\DATA\2021\2D tank\2nd\Experiments'
data = pd.read_csv(path+'\tableau CH4 ppm 1st het setup 1st gas inj sept 30th D1 D2 D3.csv')

data.info()


data_mean = data[["CH4 A0_D1", "CH4 A1_D1"]].mean()

data.to_csv(path+'\CH4 A0_D1 avg CH4 A1_D1.csv')
















