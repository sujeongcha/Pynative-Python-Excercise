#2 Get Total profit of all months and show line plot with the following Style properties
# Generated line plot must include following Style properties: –
# Line Style dotted and Line-color should be red
# Show legend at the lower right location.
# X label name = Month Number
# Y label name = Sold units number
# Add a circle marker.
# Line marker color as read
# Line width should be 3

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

plt.plot(data.month_number, data.total_profit, label='Profit data of last year', 
         linestyle='--', linewidth=3, color='red', marker='o', markerfacecolor='black')
plt.title("Company Sales data of last year")
plt.xticks(range(1, 13))
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.legend(loc="lower right")
plt.show()

#Given Solution
import pandas as pd
import matplotlib.pyplot as plt  
df = pd.read_csv("D:\\Python\\Articles\\matplotlib\\sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()

plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
