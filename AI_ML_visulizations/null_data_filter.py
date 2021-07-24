#filtering data
# displaying data only with Gender = NaN
import pandas as pd
import numpy as np
data=pd.read_csv('employees_with_missing_data.csv')
#bool_series=data["Gender"].isnull()
bool_series=data.isnull()
result1 = data[bool_series]
#result2 = data["Gender"][bool_series]
print(result1)
#print(result2)