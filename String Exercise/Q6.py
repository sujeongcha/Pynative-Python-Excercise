#Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

#My Solution
def divisibleFive(list):
  for a in list:
    if a % 5 == 0:
      print(a)
      
print("Finding divisible of 5")
divisibleFive([10, 20, 33, 46, 55])

#Given Solution
def findDivisible(numberList):
  for num in numberList:
    if (num % 5 == 0):
      print(num)

numList = [10, 20, 33, 46, 55]
print("Finding divisible of 5 in a list")
findDivisible(numList)
