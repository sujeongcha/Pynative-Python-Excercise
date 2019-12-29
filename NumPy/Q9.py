#Following is the input NumPy array delete column two and insert following new column in its place.

#My Solution
import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
newColumn = np.array([[10,10,10]])

print("Printing Original array")
print(sampleArray)

newArray = np.delete(sampleArray, 1, axis=1)
print("\nArray after deleting column 2 on axis 1")
print(newArray)

print("\nArray after inserting column 2 on axis 1")
print(np.insert(newArray, 1, newColumn, axis=1))
