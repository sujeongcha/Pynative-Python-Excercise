#Read all product sales data and show it using the stack plot

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

plt.stackplot(data.month_number, data.facecream, data.facewash, data.toothpaste, data.bathingsoap, 
              data.shampoo, data.moisturizer, colors=['m','c','r','k','g','y'], 
              labels=['face cream', 'face wash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer'])
plt.title("All product sales data using stack plot")
plt.xlabel("Month Number")
plt.ylabel("Sales units in Number")
plt.legend(loc="upper left")
plt.show()
