#Read toothpaste sales data of each month and show it using a scatter plot
#Also, add a grid in the plot. gridline style should “–“

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

plt.scatter(data.month_number, data.toothpaste, label='Tooth paste Sales data')
plt.grid(linestyle='--')
plt.xticks(range(1, 13))
plt.title("Tooth paste Sales data")
plt.xlabel("Month Number")
plt.ylabel("Number of units sold")
plt.legend(loc="upper left")
plt.show()
