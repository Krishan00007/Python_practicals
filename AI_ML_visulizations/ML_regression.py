import numpy as np
import matplotlib.pyplot as plt
# Implementation of Linear Regression
def estimate_coef( x, y):
    # number of observations or points or training data  7
    n = np.size(x)
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
    SS_xy = np.sum(x * y) - n * m_x * m_y
    SS_xx = np.sum(x * x) - n * m_x * m_x
    # Calculating regression coefficients
    m = SS_xy / SS_xx
    c = m_y - m * m_x  # c=y-mx
    return (m, c)
def plot_regression_line(x,y,b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="r", marker="o", s=30)
    y_pred = b[1] * x + b[0]
    plt.scatter(x, y_pred, color="g", marker="o", s=30)
    plt.plot(x,y_pred,color="b")
    # putting labels
    plt.xlabel("--------X-Axis------->")
    plt.ylabel("--------Y-Axis------->")
    # function to show the plot
    plt.show()
def startAIAlgorithm():
   print("AI algorithm started.....")
   #x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ])
   #y = np.array([5, 7, 4, 8, 9, 6, 5, 8, 10, 12, 14])
   x = np.array([150, 200, 250, 300, 350, 400, 600])
   y = np.array([6450, 7450, 8450, 9450, 11450, 15450, 18450])

   # estimating coefficients
   m, c = estimate_coef(x,y)   # Sender Values
   print("Estimated Coefficients: \n")
   print("Slope m =", m)
   print("Y-intercept c = ",c)
   print("Model : y = ", m, "* x  +", c)
   plot_regression_line(x,y,[c,m])

if __name__ == "__main__":
    startAIAlgorithm()

  