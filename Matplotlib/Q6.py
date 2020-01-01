#Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

plt.bar(data.month_number, data.bathingsoap, label='bathingsoap sales data')
plt.grid(linestyle='--')
plt.xticks(range(1, 13))
plt.title("bathingsoap sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.savefig("bathingsoap.png")
plt.show()
