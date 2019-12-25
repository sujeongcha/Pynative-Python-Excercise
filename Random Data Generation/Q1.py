#Generate 3 random integers between 100 and 999 which is divisible by 5

#My Solution
import random

for num in range(3):
  print(random.randrange(100, 999, 5), end=', ')

#random.randrange generates integers
