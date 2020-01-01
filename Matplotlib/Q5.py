#Read face cream and facewash product sales data and show it using the bar chart
#Bar chart should display the number of units sold per month for each product. 
#Add a separate bar for each product in the same chart.

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

plt.bar([a-0.25 for a in data.month_number], data.facecream, label='Face Cream sales data', align='edge', width=0.25)
plt.bar([a for a in data.month_number], data.facewash, label='Face Wash sales data', align='edge', width=0.25)
plt.grid(linestyle='--')
plt.xticks(range(1, 13))
plt.title("Facewash and facecream sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.legend(loc="upper left")
plt.show()
