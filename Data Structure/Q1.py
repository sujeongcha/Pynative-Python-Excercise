#Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second

#My Solution
def thirdList(list1, list2):
  oddIndex = []
  for i in range(len(list1)):
    if i % 2 == 1:
      oddIndex.append(list1[i])
  evenIndex = []
  for i in range(len(list2)):
    if i % 2 == 0:
      evenIndex.append(list2[i])
  thirdlist = oddIndex + evenIndex
  return [oddIndex, evenIndex, thirdlist]

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
print("Element at odd-index positions from list one")
print(thirdList(listOne, listTwo)[0])
print("Element at even-index positions from list two")
print(thirdList(listOne, listTwo)[1])
print("Printing Final third list")
print(thirdList(listOne, listTwo)[2])

#Given Solution
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()

oddElements = listOne[1::2]
print("Element at odd-index positions from list one")
print(oddElements)

EvenElement = listTwo[0::2]
print("Element at odd-index positions from list two")
print(EvenElement)

print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)
