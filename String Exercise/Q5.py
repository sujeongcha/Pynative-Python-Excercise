#Given a list of ints, return True if first and last number of a list is same

#My Solution
def sameInt(list):
  return list[0] == list[-1]
  
print("the first and last number of a list is same")
print("result is", sameInt([10, 20, 30, 40, 10]))

#Given Solution
def isFirst_And_Last_Same(numberList):
  firstElement = numberList[0]
  lastElement =  numberList[-1]
  if(firstElement == lastElement):
    return True
  else:
    return False

numList = [10, 20, 30, 40, 10]

print("The first and last number of a list is same")
print("result is", isFirst_And_Last_Same(numList))
