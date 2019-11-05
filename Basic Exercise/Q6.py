#Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

#My Solution
def Divisible(numList):
  for num in numList:
    if num % 5 == 0:
      print(num)

print("Finding divisible of 5")
Divisible([10, 20, 33, 46, 55])

#Given Solution
def findDivisible(numberList):
  for num in numberList:
    if (num % 5 == 0):
      print(num)

numList = [10, 20, 33, 46, 55]
print("Finding divisible of 5 in a list")
findDivisible(numList)
