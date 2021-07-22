import matplotlib.pyplot as plt
#plt.plot([1,2,3,4])  #values for y-axis
plt.plot([1,2,3,4,5],[0,2,3,4,5], 'go-', label ='line 1', linewidth='2')  #values for x-axis y-axis
plt.plot([0,2,3,4,5],[1,4,9,16,25], 'rs--', label ='line 2', linewidth='2')
plt.axis([0,6,0,26])
plt.legend(loc="upper left")
plt.show()
