#Working with Missing data in Pandas dataset to used for machine learning
#In Pandas missing data is represented by two value:

#1) None:  None is a python singelton object that is often used for missing data in python code
#2) NaN: NaN (an accronym for NOt a Number) is a special floating point value recognized by all system

#Pandas treat None and Nan as essentitaly interchangeable for indicating missing or null values
#useful functions in pandas are
# isnull()
# notnull()
# dropna()
# fillna()
# replace()
# interpolate()

#1 Checking for missing using isnull()
# return dataframe of boolean values which are true for NaN

import pandas as pd
import numpy as np

dict={'First Score':[100,90,np.nan,95],'Second Score':[30,45,56,np.nan], 'Third Score':[np.nan, 40, 80,98]}
df=pd.DataFrame(dict)
df2=df.isnull()
print( df )
print( df2 )