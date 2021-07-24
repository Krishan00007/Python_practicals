import pandas as pd
import numpy as np

#filling missing value with previous ones
dict={'First Score':[100,90,np.nan,95],'Second Score':[30,45,56,np.nan], 'Third Score':[np.nan, 40, 80,98]}
df=pd.DataFrame(dict)
#filling a missing with previous ones
df2=df.fillna(method='pad')
#filling a missing with next ones
df3=df.fillna(method='bfill')
print( df )
print(df2)
print( df3 )

