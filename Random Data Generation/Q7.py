#Calculate mutiplication of two random float numbers
#First random float number must be between 0.1 and 1
#Second random float number must be between 9.5 and 99.5

#My Solution
import random

num1 = random.uniform(0.1, 1)
num2 = random.uniform(9.5, 99.5)

print("First Random float is ", num1)
print("Second Random float is ", num2)
print("Multiplication is ", num1 * num2)
