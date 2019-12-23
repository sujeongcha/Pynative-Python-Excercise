#Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element

#My Solution
def countNum(numList):
  numDict = {}
  for i in numList:
    if i in numDict.keys():
      numDict[i]+=1
    else:
      numDict[i]=1
  return numDict

sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sampleList)
print("Printing count of each item ", countNum(sampleList))

#Given Solution
sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sampleList)

countDict = dict()
for item in sampleList:
  if(item in countDict):
    countDict[item] += 1
  else:
    countDict[item] = 1
  
print("Printing count of each item  ",countDict)
