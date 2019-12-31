#Sort all cars by Price column

#My Solution
df.sort_values(by = 'price', ascending=False)

#Given Solution
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
carsDf.head(5)
