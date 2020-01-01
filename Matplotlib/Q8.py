#Calculate total sale data for last year for each product and show it using a Pie chart

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

salesdata = []
for col in data.columns[1:7]:
    salessum = data[col].sum()
    salesdata.append(salessum)
    
plt.pie(salesdata, labels=data.columns[1:7], autopct='%1.1f%%')
plt.axis("equal")
plt.legend(loc="lower right")
plt.title("Sales data")
plt.show()
