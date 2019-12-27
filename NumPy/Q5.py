#Add the following two NumPy arrays and Modify a result array by calculating the square root of each element

#My Solution
import numpy as np

arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

print("addition of two array is\n")
print(arrayOne+arrayTwo)

print("\nResult array after calculating the square root of all elements\n")
print(np.square(arrayOne+arrayTwo))

#Given Solution
import numpy

arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

resultArray  = arrayOne + arrayTwo
print("addition of two arrays is \n")
print(resultArray)

for num in numpy.nditer(resultArray, op_flags = ['readwrite']):
   num[...] = num*num
print("\nResult array after calculating the square root of all elements\n")
print(resultArray)
