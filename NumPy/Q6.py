#Split the array into four equal-sized sub-arrays

#My Solution
import numpy as np

array = np.arange(10, 34, 1).reshape((8,3))
print("Creating 8X3 array using numpy.arange\n")
print(array)

print("\nDividing 8X3 array into 4 sub array\n")
print(np.split(array, 4))

#Given Solution
import numpy

print("Creating 8X3 array using numpy.arange")
sampleArray = numpy.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8,3)
print (sampleArray)

print("\nDividing 8X3 array into 4 sub array\n")
subArrays = numpy.split(sampleArray, 4) 
print(subArrays)
