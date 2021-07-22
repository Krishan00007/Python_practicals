import matplotlib.pyplot as plt
x=[2,3,4,5,6,7]
y=[4,9,16,25,36,49]

plt.plot(x,y, marker = 'o', markerfacecolor='red', markersize='10', linestyle='dashed', color='blue')
plt.title("Number with squared values")
plt.xlabel("----------Numbers----------", fontsize=14, color='red')
plt.ylabel("----------Some Numbers----------", fontsize=14, color='blue')
plt.axis([1,8,2,51])
plt.grid(True)
plt.annotate('Square of 5', xytext=(3,40), xy=(5,25),arrowprops=dict(facecolor='red',shrink=.3))
plt.legend(loc="upper left")
plt.show()
