import pandas as pd
import numpy as np
data=pd.read_csv('employees_with_missing_data.csv')
#printing the first 10 to 24 rows of the data frame form visualization
print( data[10:25] )
#Analyse the value of gender in RowIndex no 20 and 22
#Now we are going to fill all the null values in Gender column with "NO GENDER"
#filling a null values using fillna()

df2=data["Gender"].fillna("No Gender")
df3=data[10:25]["Gender"].fillna("No Gender")
print("\n\n\n", data)
print("\n\n\n", df2)
print("\n\n\n", df3)