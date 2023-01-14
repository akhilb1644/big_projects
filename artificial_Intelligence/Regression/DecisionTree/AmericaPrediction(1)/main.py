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

ppt.title('Year v.s. Duties / Fertility / Inflation / Foreign Born Percent')
ppt.xlabel('Year')
ppt.ylabel('Foreign born percent / Inflation / Duty & Fertility Rates\n(per 1000 women from ages 15-44)')
years = data.iloc[:,0].values

ppt.plot(years,x[:,2],color='green')
ppt.plot(years,y,color='blue')
ppt.plot(years,x[:,0],color='red')
ppt.plot(years,x[:,1],color='cyan')
ppt.legend(['Tariff Rate','Fertility Rate','Inflation Rate','Foreign Born Percent'])
ppt.savefig('plot1.png')

# With the previous model for duties, can we make a model out of that plotting another potential "fertility cycle"

data1 = pd.read_csv('iif.csv')
x1 = data1.iloc[:,:-1].values
y1 = data1.iloc[:,-1].values

xtn1,xtt1,ytn1,ytt1 = tts(x1,y1,test_size=0.25,random_state=4)

model1 = DecisionTreeRegressor(max_depth = 57)
model1.fit(xtn1,ytn1) # R-Squared value is 0.9698673465963251

topred = pd.read_csv(r"2pred.csv")
topred = topred.iloc[:,:].values
years = list(range(1971,2022))

duties = model1.predict(topred)
topred = np.column_stack((topred,duties))

ferts = model.predict(topred)

ppt.clf()
ppt.xlabel('Year')
ppt.ylabel('Predicted Fertility Rate\n(newborns per 1,000 women from ages 15-44)')
ppt.title('Year vs Predicted Fertility Rate')
ppt.plot(years,ferts,color='cyan')
ppt.savefig('plot2.png')

# This is a combined plot
ppt.ylabel('Past & Projected Fertility Rate\n(newborns per 1,000 women from ages 15-44)')
ppt.title('Year vs Past & Projected Fertility Rate')
ppt.plot(list(range(1914,1971)),y,color='blue')
ppt.legend(['Past Fertility Rate','Projected Fertility Rate'])
ppt.savefig('plot3.png')

"""
Overall, the modern predictions of the model aren't very accurate. However, this is partially because the duty data comes from the predicted duties(in
ImmigrationvsDuties folder). Overall, instead of predicted how many children a certain age group will put into the world, it predicts the overall "health"
of American civilization. To be fair, the early 2000s was pretty tumultuous(it saw the start and main part of an event called the Great Recession), which is a 
dip in plot 3 graph. However, I don't really get the peak we are in now. However, either the model is incorrect, or it has figured out what is coming a few years 
down the line(maybe a revival in isolationism and increase in births due to the work from home trend).
"""
