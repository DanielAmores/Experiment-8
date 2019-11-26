import pandas as pd
cars = pd.read_csv('cars.csv')
# A
a=cars.iloc[:5,1:11:2]
# B
b = cars[cars['Model']=='Mazda RX4']
# C
c = cars.ix[cars['Model'] == 'Camaro Z28',['cyl']]
# D
e=cars.loc[cars['Model'] == 'Mazda RX4 Wag', ['cyl', 'gear']]
f=cars.loc[cars['Model'] == 'Ford Pantera L', ['cyl', 'gear']]
g=cars.loc[cars['Model'] == 'Honda Civic', ['cyl', 'gear']]
d = pd.concat([e,f,g])
 # print
print (a)
print (b)
print (c)
print (d)
