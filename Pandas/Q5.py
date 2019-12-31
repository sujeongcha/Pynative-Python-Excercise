#Count total cars per company

#My Solution
df.groupby('company').count()

#Given Solution
df['company'].value_counts()
