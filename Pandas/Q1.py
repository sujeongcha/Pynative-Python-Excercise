#From given data set print first and last five rows

#My Solution
import pandas as pd

data = pd.read_csv("Automobile_data.csv")

display(data.head(5))
display(data.tail(5))
