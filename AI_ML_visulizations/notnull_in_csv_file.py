import pandas as pd
import numpy as np
data=pd.read_csv('sample_data/employees_with_missing_data.csv')
bool_series=data.isnull()
bool_series=data["Gender"].notnull()
#creating bool series True for NaN values
#bool series = =pd.notnull(data["Gender"])
print(bool_series)
#filtering data
# displaying data only with Gender = not NaN
result1 = data[bool_series]
result2 = data["Gender"][bool_series]
print(result1)
print(result2)