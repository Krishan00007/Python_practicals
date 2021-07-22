# Normalize data (length of 1)
from sklearn.preprocessing import Normalizer
import pandas as pd
from pandas import read_csv
from numpy import set_printoptions
filename = 'sample_data/pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)
# summarize transformed data
set_printoptions(precision=1)
print(normalizedX[0:6,:])
df=pd.DataFrame(normalizedX)
