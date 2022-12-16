import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor as dtr
import matplotlib.pyplot as ppt

data = pd.read_csv(r"iif.csv")
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

# Test Training Split
xtn,xtt,ytn,ytt = tts(x,y,test_size=0.25,random_state=4)

# Scaling the data
stsclr = StandardScaler()
sxtn,sxtt = stsclr.fit_transform(xtn),stsclr.transform(xtt)
