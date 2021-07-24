#2 Checking for missing using notnull()
# return dataframe of boolean values which are False for NaN

import pandas as pd
import numpy as np

dict={'First Score':[100,90,np.nan,95],'Second Score':[30,45,56,np.nan], 'Third Score':[np.nan, 40, 80,98]}
# creating a dataframe using dictionary
df=pd.DataFrame(dict)
df2=df.notnull()
print( df )
print( df2 )
