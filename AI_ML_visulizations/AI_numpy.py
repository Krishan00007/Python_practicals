import numpy
import urllib.request
#Load CSV files with PANDAS

import pandas
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_column', None)
pandas.set_option('display.width', 1000)
filename ="indians-diabetes.data.csv"
hnames=['preg', 'plas', 'pres','skin','test', 'mass', 'pedi', 'age', 'class']
df=pandas.read_csv(filename, names=hnames)
print("Size of Training data = ", df.shape)
print(df.dtypes)
print(df)
print(df.iloc[:,0:2])
print(df.iloc[:,[0,3,5]])
print(df.desc)