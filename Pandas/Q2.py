#Clean data and update the CSV file
#Replace all column values which contain ‘?’ and n.a with NaN.

#My Solution
for col in data.columns:
    for instance in data[col]:
        if '?' or 'n.a' in str(instance):
            instance = 'NaN'

display(data)

data.to_csv("Automobile_data.csv")

#Given Solution
df = pd.read_csv(Automobile_data.csv", na_values={'price':["?","n.a"],
                                                  'stroke':["?","n.a"],
                                                  'horsepower':["?","n.a"],
                                                  'peak-rpm':["?","n.a"],
                                                  'average-mileage':["?","n.a"]})
print(df)
df.to_csv("Automobile_data.csv")
