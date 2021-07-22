# Rescale data (between 0 and 1)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
filename = 'sample_data/pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
ss = MinMaxScaler(feature_range=(0, 5))
rescaledX = ss.fit_transform(X)
# summarize transformed data
set_printoptions(precision=2)
print(rescaledX[0:5,0:2])