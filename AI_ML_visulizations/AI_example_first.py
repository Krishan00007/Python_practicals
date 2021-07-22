#Load CSV Files with NumPy
import numpy
filename =open("indians-diabetes.data.csv")
data =numpy.loadtxt(filename, delimiter=',')

filename.close

print("numpy load text size= ", data.shape)
print("Data  : ", data)
import pandas as pd
  
uploaded = files.upload()
import io 
  
df = pd.read_csv(io.BytesIO(uploaded['indians-diabetes.data.csv']))
import csv
filename =open("indians-diabetes.data.csv")
#filename= open("c:\aman\name of the file. extention)
reader = csv.reader(filename, delimiter=',')
lines=list(reader)
print("\n\n no of lines", len(lines), "\n\n")