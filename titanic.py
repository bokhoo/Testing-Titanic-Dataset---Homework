import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
# python -m pip install -U pip
# python -m pip install -U matplotlib

import seaborn as sns
#conda install seaborn

# %matplotlib inline

titanic = pd.read_table('titanic.csv', header = 0, sep = ',')
print(titanic.head())

titanic.isnull().sum()

sns.countplot('Survived', data=titanic)
plt.show()

titanic.groupby(['Sex','Pclass']).mean()

mean_values = titanic.groupby(['Sex','Pclass']).mean()
mean_values['Survived'].plot(kind='bar')