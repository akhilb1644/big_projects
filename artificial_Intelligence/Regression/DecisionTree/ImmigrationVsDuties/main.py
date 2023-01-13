"""
My sources for this Decision Tree Regressio's Data:

https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-
https://fraser.stlouisfed.org/files/docs/publications/histstatus/pages/1975-1979/58477_1975-1979.pdf
https://www.migrationpolicy.org/programs/data-hub/charts/immigrant-population-over-time

WARNING: Foreign Born Populations in unmarked years are estimations based on average rate of change between marked years.
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
model.fit(xtn,ytn) # R-Squared value is 0.9695022095831883

# I will make a graph for import duties (predicted) by this model from 1970 as data doesn't exist in the source
topred = pd.read_csv(r"2pred.csv")
topred = topred.iloc[:,:].values
years = list(range(1971,2022))

ppt.title('Year vs Predicted Tariff Rate')
ppt.xlabel('Year')
ppt.ylabel('Predicted Tariff Rate')
ppt.plot(years,model.predict(topred),color='cyan')
ppt.savefig('fig.png')
ppt.clf()

"""
As we can see, the model is not correct(as the 1990s and 2000s were times of extremely low tariffs). However, it gives a good insight into the future of 
America as becoming more isolationist. I will update the model to be more accurate possibly by adding a religiousness percentage or some other statistic.
I would also like to say that this machine learning model was pretty accurate on the data set, so it is a start. Or maybe my model is so accurate that the 
presidents just messed up so badly with their economic policy in the 1990s(it saw the degredation of the standard of living for many with the only option of
maintaining those standards being debt). 
"""

# Making a graph from the actual data(no immigration because it is pretty much just a downward sloping straight line on the graph).
ppt.title('Year vs Tariff & Inflation Rates')
ppt.xlabel('Year')
ppt.ylabel('Tariff & Inflation Rates')
ppt.plot(list(range(1914,1971)),y,color='blue')
ppt.plot(list(range(1914,1971)),x[:,:-1],color='red')
ppt.legend(['Tariff Rate','Inflation Rate'])
ppt.savefig('fig2.png')
