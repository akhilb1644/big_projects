"""
My sources for this Decision Tree Regressio's Data:

https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-
https://fraser.stlouisfed.org/files/docs/publications/histstatus/pages/1975-1979/58477_1975-1979.pdf
https://www.migrationpolicy.org/programs/data-hub/charts/immigrant-population-over-time
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.tree import DecisionTreeRegressor as dtr
import matplotlib.pyplot as ppt

data = pd.read_csv(r"iif.csv")
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

# Test Training Split
xtn,xtt,ytn,ytt = tts(x,y,test_size=0.25,random_state=4)

# Making the model
model = DecisionTreeRegressor(max_depth = 57)
model.fit(xtn,ytn) # R-Squared value is 0.969563701289449

# I will make a graph for import duties (predicted) by this model from 1970 as data doesn't exist in the source
topred = pd.read_csv(r"2pred.csv")
topred = topred.iloc[:,:]
years = list(range(1971,2022))

ppt.title('Year vs Predicted Tariff Rate')
ppt.xlabel('Year')
ppt.ylabel('Predicted Tariff Rate')
ppt.plot(years,model.predict(topred),color='cyan')
ppt.savefig('fig.png')

"""
As we can see, the model is not correct(as the 1990s and 2000s were times of extremely low tariffs). However, it gives a good insight into the future of 
America as becoming more isolationist. I will update the model to be more accurate possibly by adding a religiousness percentage or some other statistic.
"""
