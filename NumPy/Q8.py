#Following is the 2-D array. Print max from axis 0 and min from axis 1

#My Solution
import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

print("Printing Original array")
print(sampleArray)

print("\nPrinting amin of Axis 1")
print(np.min(sampleArray, axis=1))

print("\nPrinting amax of Axis 0")
print(np.max(sampleArray, axis=0))
