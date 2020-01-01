#Read the total profit of each month and show it using the histogram to see most common profit ranges

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(data.total_profit, profit_range, label='Profit data')
plt.title("Profit data")
plt.xlabel("profit range in dollar")
plt.ylabel("Actual profit in dollar")
plt.xticks(profit_range)
plt.yticks(range(0, 6))
plt.legend(loc="upper left")
plt.show()
