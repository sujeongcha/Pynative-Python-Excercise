#Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list

#My Solution
def listex(numList):
  print("Original list ", numList)
  indexfour = numList.pop(4)
  print("List After removing element at index 4 ", numList)
  numList.insert(2, indexfour)
  print("List after Adding element at index 2 ", numList)
  numList.append(indexfour)
  print("List after Adding element at last ", numList)
  
listex([34, 54, 67, 89, 11, 43, 94])
  
