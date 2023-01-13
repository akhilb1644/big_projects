"""
My sources for this Decision Tree Regressio's Data:

https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-

https://fraser.stlouisfed.org/files/docs/publications/histstatus/pages/1975-1979/58477_1975-1979.pdf

https://www.migrationpolicy.org/programs/data-hub/charts/immigrant-population-over-time
WARNING: Foreign Born Populations in unmarked years are estimations based on average rate of change between marked years.

https://www.cdc.gov/nchs/data/statab/t1x0197.pdf
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as ppt

data = pd.read_csv(r"totalFertility.csv")
x = data.iloc[:,1:-1].values
y = data.iloc[:,-1].values

xtn,xtt,ytn,ytt = tts(x,y,test_size=0.25,random_state=4)

model = DecisionTreeRegressor(max_depth = 57)
model.fit(xtn,ytn) # R-Squared score of the model is 0.8894300622742276 (that's pretty good)

