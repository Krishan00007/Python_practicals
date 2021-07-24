import warnings
warnings.filterwarnings(action="ignore")
# Practical implementation of Linear Regression
# -----------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def get_data(filename):
    dataframe = pd.read_csv(filename)
    print( dataframe)
    x_parameters = []
    y_parameters = []
    for single_square_feet, single_price in zip(dataframe['square_feet'], dataframe['price'] ):
       
        x_parameters.append( [single_square_feet] )
        y_parameters.append( single_price )

        # once we got the data, return it to main program
    return x_parameters, y_parameters
#sandeepsingla sandeepsingla11:16 AM
def linear_model_main(x_parameters, y_parameters, quest_value):
    # create Linear Regression Object
    regr = LinearRegression()
    regr.fit(x_parameters, y_parameters)
    predicted_ans = regr.predict([[quest_value]])
    print("Output From Machine = ", predicted_ans)
    predictions = {}
    print("After Training via Sklearn : Model Parameters")
    print("m= ", regr.coef_)
    print("c= ", regr.intercept_)
    plt.scatter(x_parameters, y_parameters, color="m", s=30, marker="o")
    
    all_predicted_Y=regr.predict( x_parameters)
    plt.scatter(x_parameters, all_predicted_Y, color="b", s=30, marker="o")
    plt.plot(x_parameters, all_predicted_Y, color="g")
    plt.scatter(quest_value, predicted_ans, color="r")
    plt.show()
def startAIAlgorithm():
    #Collect the training data from external CSV file
    x, y = get_data('sample_data/LR_House_price.csv')
    print("Formatted Training Data  : ")
    print("x = ", x)
    print("y = ", y)
    question_value = 700   #This is the question data
    linear_model_main(x, y, question_value)

if __name__ == "__main__":
    startAIAlgorithm()