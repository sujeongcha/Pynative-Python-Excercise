#Generate  random String of length 5

#My Solution
import random
import string

def randomString(stringlength):
  strings = string.ascii_letters
  return ''.join(random.choice(strings) for i in range(stringlength))
  
print("Random String is ", randomString(5))
