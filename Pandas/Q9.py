#Concatenate two data frames using the following conditions
#Create two data frames using the following two Dicts, Concatenate those two data frames and create a key for each data frame.

#My Solution
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

data1 = pd.DataFrame(GermanCars)
data2 = pd.DataFrame(japaneseCars)

pd.concat([data1, data2], keys=['Germany', 'Japan'])
