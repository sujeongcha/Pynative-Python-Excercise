#Generate a random Password which meets the following conditions
#Password length must be 10 characters long.
#It must contain at least 2 upper case letter, 2 digits, and 2 special symbols.

#My Solution
import random
import string

source = string.ascii_letters + string.digits + string.punctuation
password = random.choices(string.ascii_uppercase, k=2)
password += random.choices(string.digits, k=2)
password += random.choices(string.punctuation, k=2)

for i in range(4):
  password += random.choice(source)

random.SystemRandom().shuffle(password)
password = ''.join(password)
print(password)
