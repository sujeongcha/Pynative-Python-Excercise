#Read Bathing soap facewash of all months and display it using the Subplot

#My Solution
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("company_sales_data.csv")

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(data.month_number, data.bathingsoap, linewidth=3, color='black', marker='o')
axarr[0].set_title("Sales data of a Bathingsoap")
axarr[1].plot(data.month_number, data.facewash, linewidth=3, color='red', marker='o')
axarr[1].set_title("Sales data of a Facewash")
plt.xticks(range(1,13))
plt.xlabel("Month number")
plt.ylabel("Sales units in number")
plt.show()
