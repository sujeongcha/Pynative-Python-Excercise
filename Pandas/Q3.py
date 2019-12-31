#Find the most expensive car company name

#My Solution
df[['company', 'price']][df.price == df.price.max()]
