# Filling a null values using replace() method

import pandas as pd
import numpy as np
data=pd.read_csv('employees_with_missing_data.csv')
#printing the first 10 to 24 rows of the data frame form visualization
#print( data[10:25] )
#Analyse the value of gender in RowIndex no 20 and 22
#Now we are going to fill all the null values in Gender column with "NO GENDER"
#filling a null values using replace()
df2=data.replace(to_replace=np.nan, value=-99)
df3=df2.replace(to_replace='Male', value='M')
df4=df3.replace(to_replace='Female', value='F')
print("\n\n\n", df4)
#df2 = df2.replace(to_replace=['Male','Female'], value=['M','F'])
