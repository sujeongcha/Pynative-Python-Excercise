#Find each company’s Higesht price car

#My Solution
df6 = df[['company', 'price']]
df6.iloc[df6.groupby('company').price.idxmax(), :]

#Given Solution
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company','price'].max()
priceDf
