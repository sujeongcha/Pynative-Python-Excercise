#Following is the provided numPy array. return array of items in the second column from all rows

#My Solution
import numpy as np

sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
print("Printing Input Array")
print(sampleArray)

result = []
for i in sampleArray:
  result.append(i[1])
  
print("\nPrinting array of items in the 2nd column from all rows")
print(result)

#Given Solution
import numpy

sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]]) 
print("Printing Input Array")
print(sampleArray)

print("\n Printing array of items in the third column from all rows")
newArray = sampleArray[...,1]
print(newArray)
