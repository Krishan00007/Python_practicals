#using simple csv standard library
import numpy
import csv
filename =open("indians-diabetes.data.csv")
#filename= open("c:\aman\name of the file. extention)
reader = csv.reader(filename, delimiter=',')
lines=list(reader)
print("\n\n no of lines", len(lines), "\n\n")
print("list of data ", lines)
#data = numpy.array(reader).astype('float')
#print(data.shape)
for line in lines:
    print( line )