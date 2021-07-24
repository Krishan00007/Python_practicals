import pandas as pd
import numpy as np

dict={'First Score':[100,90,np.nan,95],'Second Score':[30,45,56,np.nan], 'Third Score':[np.nan, 40, 80,98]}
df=pd.DataFrame(dict)
#filling missing value using fillna()
df2=df.fillna(999999)
print( df )
print( df2 )