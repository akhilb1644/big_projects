"""
As a disclaimer, I originally envisioned this as a Neural Network. But, I got much less data than I need for a neural network. Therefore, I had to use a 
linear regression.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('TeachingResults.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=6)

dataset = pd.read_csv('data2predict4.csv')

fourth_one = dataset.iloc[:, :-1].values

fourth_pred = regressor.predict(fourth_one)

xv = list(range(15,41))

xp = np.array(xv)
yp = fourth_pred

plt.plot(xp, yp)

dataset = pd.read_csv('data2predict10.csv')
tenth_one = dataset.iloc[:, :-1].values

tenth_pred = regressor.predict(tenth_one)
yp = tenth_pred

plt.title("Predicted Individualized Learning Rating vs Class Size\nfor 10th Grade(lower) vs 4th Grade(higher) in core subjects")
plt.xlabel("Class Size")
plt.ylabel("Predicted Individualized Learning Rating(1-10)")

plt.plot(xp, yp)
plt.savefig('tenth.png')
