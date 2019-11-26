import pandas as pd
cars = pd.read_csv('cars.csv')
firstlast=pd.concat([cars.head(),cars.tail()]) 
print (firstlast)
