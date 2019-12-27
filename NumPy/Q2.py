#Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10

#My Solution
import numpy as np

print(np.arange(100, 200, 10).reshape([5,2]))

#Given Solution
import numpy

print("Creating 5X2 array using numpy.arange")
sampleArray = numpy.arange(100, 200, 10)
sampleArray = sampleArray.reshape(5,2)
print (sampleArray)
