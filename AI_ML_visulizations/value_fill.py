# Filling a null values using interpolate() method
#using interpolate() functon to fill missing values using Linear method
import pandas as pd
# Creating the dataframe
df = pd.DataFrame(
                    {   "A": [12, 4, 5, None, 1],
                        "B": [None, 2, 54, 3, None],
                        "C": [20, 16, None, 3, 8],
                        "D": [14, 3, None, None, 6]
                    }
                )
# Print the dataframe
print( df )
#Let’s interpolate the missing values using Linear method.
# Note that Linear method ignore the index and treat the values as equally spaced.
# To interpolate the missing values
#df2 = df.interpolate(method ='linear', limit_direction ='forward')
#print( df2 )

#As we can see the output, values in the first row could not get filled as the direction  of filling
#  of values is forward and there is no previous value which could have been used in interpolation.

df3 = df.interpolate(method ='linear', limit_direction ='backward')
print( df3 )