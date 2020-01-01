#Read Total profit of all months and show it using a line plot

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

plt.plot(data.month_number, data.total_profit)
plt.title("Company profit per month")
plt.xticks(range(1, 13))
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.xlabel("Month number")
plt.ylabel("Total profit")
plt.show()

#Given Solution
import pandas as pd
import matplotlib.pyplot as plt  
df = pd.read_csv("D:\\Python\\Articles\\matplotlib\\sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()

plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
