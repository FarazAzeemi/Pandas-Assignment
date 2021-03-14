import numpy as np
import pandas as pd
from glob import glob
import re
#from matplotlib import pyplot as plt

stock_files = sorted(glob('csvfiles/PIAIC-BATCH-35-Q2-main/states*.csv'))
print(stock_files)
us_census = pd.concat((pd.read_csv(file) for file in stock_files), ignore_index = True)
print(us_census)
print(us_census.dtypes)
print(us_census.columns)
print(us_census.head())
us_census1 = pd.DataFrame(us_census['GenderPop']. str.split('_', 1).tolist(), columns = ['Male', 'Female'])
us_census1['Male'] = us_census1['Male'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else str(x))
us_census1['Female'] = us_census1['Female'].apply(lambda x: str(x).replace('F','') if 'F' in str(x) else str(x))
us_census1['Female'] = pd.to_numeric(us_census1['Female'], errors='coerce')
us_census1['Male'] = pd.to_numeric(us_census1['Male'], errors='coerce')
print(us_census1[['Male', 'Female']])
#plt.scatter('Male', 'Female')
#plt.show()
us_census = pd.concat([ us_census,us_census1] ,axis=1)
a = us_census['TotalPop'] - us_census['Male']
us_census['Female'] = us_census['Female'].fillna(a)
print(us_census['Female'])
print(us_census.duplicated())
print(us_census.drop_duplicates())
#plt.scatter('Male', 'Female')
#plt.show()
print(us_census.columns)
#us_census.hist(column = 'State' ,by = 'TotalPop' )
#us_census.hist(column = 'Hispanic' ,by = 'White' )
#us_census.hist(column = 'Male' ,by = 'Female' )
us_census['Income'] = us_census['Income'].apply(lambda x : str(x).replace('$', '') if '$' in str(x) else str(x))
us_census1['Income'] = pd.to_numeric(us_census1['Income'], errors='coerce')














