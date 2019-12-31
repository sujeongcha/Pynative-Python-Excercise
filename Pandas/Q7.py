#Find the average mileage of each car making company

#My Solution
df7 = df.groupby('company')
df7['company', 'average-mileage'].mean()

#Given Solution
car_Manufacturers = df.groupby('company')
mileageDf = car_Manufacturers['company','average-mileage'].mean()
mileageDf
