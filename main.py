import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r'SearchTrend.csv')
data.describe()

z = sns.relplot(x='cold', y='coronavirus', data=data)

# print(data.isnull().sum())
