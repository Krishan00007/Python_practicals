import matplotlib.pyplot as plt
x1=[2,3,4]
y1=[5,5,5]
x2=[1,2,3,4,5]
y2=[2,3,2,3,4]
x3=[1,2,3,4,5]
y3=[6,8,7,8,7]
plt.scatter(x1,y1)
plt.scatter(x2,y2,marker='v',color='r')
plt.scatter(x3,y3,marker='^',color='m')
plt.title("Scatter PLot Example")
plt.xlabel("---------Months----------", fontsize=14, color='red')
plt.ylabel("----------Performance---------", fontsize=14, color='blue')
plt.legend()
plt.axis([0,8,0,10])
plt.grid(True)
#plt.annotate('Square of 5', xytext=(3,40), xy=(5,25),arrowprops=dict(facecolor='black',shrink=.1))
#plt.legend(loc="upper left")
plt.show()