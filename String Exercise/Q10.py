#Given a two list of ints create a third list such that should contain 
#only odd numbers from the first list and even numbers from the second list

#My Solution
def mergeList(list1, list2):
  result = []
  for num in list1:
    if num % 2 == 1:
      result.append(num)
  for num in list2:
    if num % 2 == 0:
      result.append(num)
  return result

listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]
print("Merged List is")
print(mergeList(listOne, listTwo))

#Given Solution
def mergeList(listOne, listTwo):
  thirdList = []
  for num in listOne:
    if(num % 2 != 0):
      thirdList.append(num)
  for num in listTwo:
    if(num % 2 == 0):
      thirdList.append(num)
  return thirdList
    
print("Merged List is")
listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

print(mergeList(listOne, listTwo))
