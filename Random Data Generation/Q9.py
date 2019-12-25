#Roll dice in such a way that every time you get the same number
#Dice has 6 number(from 1 to 6). Roll dice in such a way that every time you must get same output number. do this 5 times.

#Given Solution
import random

dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))
