#Read all product sales data and show it  using a multiline plot
#Display the number of units sold per month for each product using multiline plots. 
#i.e., Separate Plotline for each product for each product

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

for col in data.columns[1:7]:
    plt.plot(data.month_number, data[col], label=col+' Sales Data', linewidth=3, marker='o')
plt.title("Sales data")
plt.xticks(range(1, 13))
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.legend(loc="upper left")
plt.show()
