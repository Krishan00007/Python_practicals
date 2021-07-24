import pandas as pd
import numpy as np
data=pd.read_csv('employees_with_missing_data.csv')
bool_series=data.isnull()
#bool_series=data["Gender"].isnull()
#creating bool series True for NaN values
#bool series = =pd.isnull(data["Gender"])  #this is also ok

print(bool_series)
