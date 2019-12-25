#Create a 4X2 integer array and Prints its attributes (shape, dimension, length of each element in bytes)

#My Solution
import numpy as np

arr = np.empty([4,2], dtype = np.uint16)
print("Printing Array")
print(arr)

print("Printing numpy array Attributes")

print("1> Array Shape is: ", arr.shape)

print("2> Array dimensions are ", arr.ndim)

print("3> Length of each element of array in bytes is ", arr.itemsize)

