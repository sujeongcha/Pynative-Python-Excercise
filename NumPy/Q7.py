#Sort following NumPy array 
#7.1 - by the second row and
#7.2 - by the second column

#My Solution
import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print("Printing Original array")
print(sampleArray)

print("\nSorting Original array by second row")
print(sampleArray[:, sampleArray[1,:].argsort()])

print("\nSorting Original array by second column")
print(sampleArray[sampleArray[:,1].argsort()])
