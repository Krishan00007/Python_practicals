import matplotlib.pyplot as plt
x1=[1,2,3]
y1=[1,2,3]
x2=[1,2,3]
y2=[1,4,9]
plt.plot(x1,y1,x2,y2,'go-', linewidth='3')  #values for x-axis y-axis
#plt.plot(x1,y1)
#plt.plot(x2,y2)
plt.axis([0,4,0,10])
plt.legend(loc="upper center")
plt.show()