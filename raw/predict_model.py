import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#from flow import report

#Ignoring warnings
import warnings
warnings.filterwarnings("ignore")

									# Part - 1 Algorithms

# Data-Preprocessing
data = pd.read_csv('final_features.csv')
print(len(data.columns))
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

print(data.columns)
# Spliting Data 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)



#Random Forest
from sklearn.ensemble import RandomForestRegressor
lm6 = RandomForestRegressor(n_estimators=1000)
lm6.fit(X_train, y_train)
print("r fit")

predictions_rfr = lm6.predict(X_test)
predictions_rfr = np.reshape(predictions_rfr, (3000, ))
print("r pre")

g = lm6.predict([[0,41,0,2,9,0,3017170,1,2,8,486,3,14,6,1,15,8,9,1,1,3,2,0]])
print("hello",g)

# Calculating the Result in terms of errors
from sklearn import metrics
result = list()
result.append(metrics.mean_squared_error(y_test, predictions_rfr))	
result = np.array(result)

# Part 2 Visualizations
import os
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def display(r1, r2, st):
    fig1 = plt.figure()
    fig1 = plt.scatter(r1, r2)
    plt.title(st)
    plt.xlabel(namestr(r1, globals())[0])
    plt.ylabel(namestr(r2, globals())[0])
    fig3 = plt.figure()
    fig3 = sns.distplot(r2-r1)
    plt.title(st)
    plt.ylabel("Density")
    plt.xlabel("Values")
    plt.show()

while True:
    os.system('cls') 							
    print("Hi there! Here is the prediction RFR Algorithm\n\n")					
    print("Select a choice\n1.Visualization of Algorithms efficiency\n2.Visualization of Final Result\n3.Exit")
    choice = int(input())
    if choice == 1:
        choice_algo = 0
        while choice_algo!=7:
            os.system('cls')
            print("Select an algo to visualize:\n1.Linear Regression\n2.Polynomial Regression\n3.Support Vector Regression\n4.Decision Regression\n5.Random Forest Regression\n6.All Algorithms\n7.Previous Menu\n") 
            choice_algo = int(input())
            
            if choice_algo==1:
                # Visualization of LR
                display(predictions_lin, y_test, "Linear Regression")
            
            elif choice_algo==2:
                # Visualization of PR - 3
                display(predictions_poly, y_test, "Polynomial Regression")
            
            elif choice_algo==3:
                # Visualization of SVR
                display(predictions_svr, y_test, "Support Vector Regression")
            
            elif choice_algo==4:
                # Visualization of Decision Regresssion
                display(predictions_dr, y_test, "Decision Tree Regression")
            
            elif choice_algo==5:
                # Visualization of Random Forest Regression
                display(predictions_rfr, y_test, "Random Forest Regression")
            
            elif choice_algo==6:
                # All Algos
                display(predictions_lin, y_test, "Linear Regression")
                display(predictions_poly, y_test, "Polynomial Regression")
                display(predictions_svr, y_test, "Support Vector Regression")
                display(predictions_dr, y_test, "Decision Tree Regression")
                display(predictions_rfr, y_test, "Random Forest Regression")
            
            elif choice_algo==7:
                # Previous Menu
                continue
            
            else:
                # Invalid input
                print("Please enter a valid option", choice_algo, "is not valid. Press Enter to continue")
                temp = input()

    elif choice==2:
        # Visualizing the Result in terms of errors
        fig13 = plt.figure()
        objects = ('RFR')
        y_pos = np.arange(len(objects))
        fig13 = plt.bar(y_pos, result)
        plt.title("The Final Result")
        plt.xticks(y_pos, objects)
        fig_txt = 'Least ErrorRate in RFR, It is the best for the dataset'
        plt.text(0.75, 0.23, fig_txt)
        plt.show()

    elif choice == 3:
        exit()

    else:
        # Invalid input
        print("Please enter a valid option.", choice, "is not valid. Press Enter to continue")
        temp = input()