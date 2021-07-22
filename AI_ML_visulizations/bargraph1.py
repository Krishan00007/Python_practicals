import matplotlib.pyplot as plt
x1=[1,3,4,5,6,7,9]
y1=[4,7,2,4,7,8,3]
x2=[2,4,6,8,10]
y2=[5,6,2,6,2]
#bar width
#width=1
plt.bar(x1,y1,label='blue bar',color='b')
plt.bar(x2,y2,label='red bar',color='r')
plt.plot(x1,y1,'go-')
plt.title("Bar Chart")
plt.xlabel("---------Bar Numbers----------", fontsize=14, color='red')
plt.ylabel("----------Bar Height---------", fontsize=14, color='blue')
plt.legend()
plt.show()
